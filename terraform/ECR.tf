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