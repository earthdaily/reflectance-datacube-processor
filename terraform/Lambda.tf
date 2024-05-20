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



variable "ecr_repository_name" {
  description = "Name of the ECR repository"
  default     = "ecr-p3-aws-github"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "lambda-p3-aws-github"
}

variable "api_gateway_name" {
  description = "Name of the API Gateway"
  default     = "api-p3-aws-github"
}

############################## specify your account # ##############################
variable "account_number" {
  description = "# AWS account"
  default     = "489065051964"
}

variable "region_east" {
  description = "AWS region"
  default     = "us-east-1"
}

# Create ECR repository
resource "aws_ecr_repository" "create_repo" {
  name                 = var.ecr_repository_name
  image_tag_mutability = "MUTABLE" # Ensure that existing images cannot be overwritten
  image_scanning_configuration {
    scan_on_push = false # Disable image scanning
  }

  # Repository is private by default
}

############################## specify the name of the ECR docker registry image ##############################
# Create Lambda function
resource "aws_lambda_function" "create_lambda" {
  function_name = var.lambda_function_name
  package_type  = "Image"
  image_uri     = "${var.account_number}.dkr.ecr.${var.region_east}.amazonaws.com/${var.ecr_repository_name}:latest"
  role          = aws_iam_role.lambda_role.arn
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

  // Attach policies including AWSLambda_FullAccess
  inline_policy {
    name = "lambda-policy"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Effect    = "Allow",
          Action    = "lambda:*",
          Resource  = "*"
        },
        {
          Effect    = "Allow",
          Action    = "iam:PassRole",
          Resource  = "*",
          Condition = {
            StringEquals = {
              "iam:PassedToService" = "lambda.amazonaws.com"
            }
          }
        }
      ]
    })
  }

  // Attach AWSLambda_FullAccess managed policy
  managed_policy_arns = ["arn:aws:iam::aws:policy/AWSLambda_FullAccess"]
}


resource "aws_lambda_function_url" "test_latest" {
  function_name      = aws_lambda_function.create_lambda.arn
  authorization_type = "NONE"
}


# IAM policy document for ECR access with conditions
resource "aws_ecr_repository_policy" "ecr_policy_attachment" {
  repository = aws_ecr_repository.create_repo.name

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


// API Gateway
resource "aws_api_gateway_rest_api" "create_api" {
  name = var.api_gateway_name

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

// Root Resource
resource "aws_api_gateway_resource" "root" {
  rest_api_id = aws_api_gateway_rest_api.create_api.id
  parent_id   = aws_api_gateway_rest_api.create_api.root_resource_id
  path_part   = "{proxy+}"
}

// ANY Method for Root Resource
resource "aws_api_gateway_method" "any_method_root" {
  rest_api_id = aws_api_gateway_rest_api.create_api.id
  resource_id = aws_api_gateway_rest_api.create_api.root_resource_id
  http_method = "ANY"
  authorization = "NONE"
}

// ANY Method for Proxy Resource
resource "aws_api_gateway_method" "any_method_proxy" {
  rest_api_id = aws_api_gateway_rest_api.create_api.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = "ANY"
  authorization = "NONE"
}

// Integration for ANY Method on Root Resource
resource "aws_api_gateway_integration" "any_integration_root" {
  rest_api_id             = aws_api_gateway_rest_api.create_api.id
  resource_id             = aws_api_gateway_rest_api.create_api.root_resource_id
  http_method             = aws_api_gateway_method.any_method_root.http_method
  integration_http_method = "ANY"
  type                    = "AWS"
  uri                     = aws_lambda_function.create_lambda.invoke_arn
}

// Integration for ANY Method on Proxy Resource
resource "aws_api_gateway_integration" "any_integration_proxy" {
  rest_api_id             = aws_api_gateway_rest_api.create_api.id
  resource_id             = aws_api_gateway_resource.root.id
  http_method             = aws_api_gateway_method.any_method_proxy.http_method
  integration_http_method = "ANY"
  type                    = "AWS"
  uri                     = aws_lambda_function.create_lambda.invoke_arn
}

// Lambda Permission for API Gateway trigger
resource "aws_lambda_permission" "api_gateway_trigger" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.create_lambda.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.create_api.execution_arn}/*/*"
}

// Lambda Permission for API Gateway trigger on {proxy+} resource
resource "aws_lambda_permission" "api_gateway_trigger_proxy" {
  statement_id  = "AllowAPIGatewayInvokeProxy"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.create_lambda.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.create_api.execution_arn}/*/*/*"
}

// Deployment
resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.create_api.id
  stage_name  = "v1"

  depends_on = [
    aws_api_gateway_integration.any_integration_root,
    aws_api_gateway_integration.any_integration_proxy,
  ]
}