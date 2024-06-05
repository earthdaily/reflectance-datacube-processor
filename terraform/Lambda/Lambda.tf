terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.48.0"
    }
  }
}

############################## activate and specify where your config file is stored for sso connection ##############################
/*
provider "aws" {
  region              = "us-east-1" # Specify your desired AWS region
  shared_config_files = ["C:/Users/xxx/.aws/config"]   
  profile             = "PowerUserAccess-dev" # Specify the profile name from your AWS credentials file
}
*/


############################## activate if you use secret id and secret key ##############################
provider "aws" {
  region              = "us-east-1" # Specify your desired AWS region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
}


############################## specify your repository name ##############################
variable "ecr_repository_name" {
  description = "Name of the ECR repository"
  default     = "ecr-p3-aws-github"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "lambda-p3-aws-github"
}

############################## specify your account # ##############################
variable "account_number" {
  description = "# AWS account"
  default     = "xxx"
}

variable "region_east" {
  description = "AWS region"
  default     = "us-east-1"
}


############################## specify the name of the ECR docker registry image ##############################
# Create Lambda function
resource "aws_lambda_function" "create_lambda" {
  function_name = var.lambda_function_name
  package_type  = "Image"
  image_uri     = "${var.account_number}.dkr.ecr.${var.region_east}.amazonaws.com/${var.ecr_repository_name}:latest"
  role          = aws_iam_role.lambda_role.arn
  memory_size   = 512
  timeout       = 120
}


############################## activate if the role doesn't exist ##############################
resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })

############################## upddate arn for the AWSLambdaBasicExecutionRole policy ##############################
  // Attach AWSLambdaBasicExecutionRole managed policy
  managed_policy_arns = ["arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"]
}


resource "aws_lambda_function_url" "test_latest" {
  function_name      = aws_lambda_function.create_lambda.arn
  authorization_type = "NONE"
}


# IAM policy document for ECR access with conditions
resource "aws_ecr_repository_policy" "ecr_policy_attachment" {
  repository = var.ecr_repository_name

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action    = [
          "ecr:BatchGetImage",
          "ecr:DeleteRepositoryPolicy",
          "ecr:GetDownloadUrlForLayer",
          "ecr:GetRepositoryPolicy",
          "ecr:SetRepositoryPolicy",
        ],
        Condition = {
          StringLike = {
            "aws:sourceArn" = "arn:aws:lambda:${var.region_east}:${var.account_number}:function:${aws_lambda_function.create_lambda.function_name}"
          }
        }
      }
    ]
  })
}