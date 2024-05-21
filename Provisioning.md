---
layout: default
title: Resources provisioning
nav_order: 4
---


# AWS Resources provisioning

Within code snippets, variables will be between <>. For example '<AWS_REGION>' will be the AWS region code, you are using for the deployment.

## Manual setup

Resources provisioning is following Amazon [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) for the AWS credentials used in GitHub Actions workflows, including:

 - not storing credentials in your repository's code. You may use GitHub Actions secrets to store credentials and redact credentials from GitHub Actions workflow logs.
- using an individual IAM user with an access key for use in GitHub Actions workflows, preferably one per repository. Do not use the AWS account root user access key.
- granting least privilege to the credentials used in GitHub Actions workflows. Grant only the permissions required to perform the actions in your GitHub Actions workflows (see below).
- Rotating the credentials used in GitHub Actions workflows regularly.
- Monitoring the activity of the credentials used in GitHub Actions workflows.

### Configure OpenID Connect
OpenID Connect (OIDC) allows your GitHub Actions workflows to access resources in Amazon Web Services (AWS), without needing to store the AWS credentials as long-lived GitHub secrets.

>❗Note: Support for custom claims for OIDC is unavailable in AWS.

#### Add identity provider to AWS IAM
To add the GitHub OIDC provider to IAM, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

 - For the provider URL, use `https://token.actions.githubusercontent.com`
 - For the "Audience": use `sts.amazonaws.com` if you are using the official action.

#### Configure role and trust policy

To configure the role and trust in IAM, see the AWS documentation ["Configure AWS Credentials for GitHub Actions"](https://github.com/aws-actions/configure-aws-credentials#configure-aws-credentials-for-github-actions) and ["Configuring a role for GitHub OIDC identity provider"](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create_GitHub)

Edit the trust policy, adding the `sub` field to the validation conditions and use `StringLike` with a wildcard operator (*) to allow any branch, pull request merge branch, or environment from the earthdaily/reflectance-datacube-processor organization and repository to assume a role in AWS. For example:

```json

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam:: require'<AWS_ACCOUNT_ID>' :oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:earthdaily/reflectance-datacube-processor:*"
                },
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}
```

>❗Note: AWS Identity and Access Management (IAM) recommends that users evaluate the IAM condition key, `token.actions.githubusercontent.com:sub`, in the trust policy of any role that trusts GitHub’s OIDC identity provider (IdP). Evaluating this condition key in the role trust policy limits which GitHub actions are able to assume the role.

#### Configure role

This action requires the following minimum set of permissions:

```json
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"RegisterTaskDefinition",
         "Effect":"Allow",
         "Action":[
            "ecs:RegisterTaskDefinition"
         ],
         "Resource":"*"
      },
      {
         "Sid":"PassRolesInTaskDefinition",
         "Effect":"Allow",
         "Action":[
            "iam:PassRole"
         ],
         "Resource":[
            "arn:aws:iam::<aws_account_id>:role/<task_definition_task_role_name>",
            "arn:aws:iam::<aws_account_id>:role/<task_definition_task_execution_role_name>"
         ]
      },
      {
         "Sid":"DeployService",
         "Effect":"Allow",
         "Action":[
            "ecs:UpdateService",
            "ecs:DescribeServices"
         ],
         "Resource":[
            "arn:aws:ecs:<region>:<aws_account_id>:service/<cluster_name>/<service_name>"
         ]
      }
   ]
}
```

This configuration follows the principle of the least privilege.

### Create a container registry
First sign in to your AWS console and select Elastic Container Register and Create a new private repository. 

![Create ECR repository](images/ECR_create_repo.png "ECR Repository creation")

You can also use the Terraform script below:
```tf
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


# Create ECR repository
resource "aws_ecr_repository" "create_repo" {
  name                 = var.ecr_repository_name
  image_tag_mutability = "MUTABLE" # Ensure that existing images cannot be overwritten
  image_scanning_configuration {
    scan_on_push = false # Disable image scanning
  }

  # Repository is private by default
}
```
>❗Note: if you are using a secret_id/secret_key as authentification method, please use the file aws_credentials.tfvars (in the terraform folder). Below the command to apply terraform script using credentials file:

```cmd
terraform apply -var-file="aws_credentials.tfvars"
```

>💡You can also use AWS CLI please see [documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html).

#### Load image to registry

Use the following steps to authenticate and push an image to your repository. For additional registry authentication methods, including the Amazon ECR credential helper, see [Registry Authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html).

   1. Retrieve an authentication token and authenticate your Docker client to your registry.
    Use the AWS CLI:

```yaml
aws ecr get-login-password --region **us-east-1** | docker login --username AWS --password-stdin xxx.dkr.ecr.us-east-1.amazonaws.com
```

>Note: If you receive an error using the AWS CLI, make sure that you have the latest version of the AWS CLI and Docker installed.

  2. Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:
```yaml
docker build -t processordemo .
```
  3. After the build completes, tag your image so you can push the image to this repository:

```yaml
docker tag processordemo:latest xxx.dkr.ecr.us-east-1.amazonaws.com/processordemo:latest
```

  4. Run the following command to push this image to your newly created AWS repository:

```yaml
docker push xxx.dkr.ecr.us-east-1.amazonaws.com/processordemo:latest
```

## Option 1: Lambda

In the AWS console and select Lambda and Create a function. 
![Create Lambda](images/Lambda.png "Lambda Function creation")

Please select image previously loaded.

![Create Lambda](images/Lambda_select_image.png "Lambda Function creation")

Within the advanced setting section, select *Enable function URL*
![Create Lambda](images/Lambda_function.png "Lambda Function creation")

## Option 2: ECS

### Create an ECS Cluster

Sign in to your AWS console and select Elastic Container Service and create a new Cluster.

An ECS cluster is a grouping of EC2 instances or AWS Fargate tasks on which we’ll deploy and run our containers. Pick the name you want and left the default settings.

![Create ECS Cluster](images/ECS_create_cluster.png "ECS Cluster")

### Create a task definition

A task definition defines the containers and resources required for the application to run. 

In the container details section give a name to the container, then grab the URI of the image in ECR. 

The name given will be needed later in the GitHub Actions workflow so keep it in mind. 

Another important note is to give the correct ports (I used port 8000) that are required for the application.

### Create a service 
Within ECS, start by navigating to the clusters tab in ECS and create a service using the task definition. For compute configuration, choose “Launch type” and leave the default option for Fargate. For the deployment configuration, choose “Service” and then, choose the task definition with the latest revision. Then, navigate to the Networking section and ensure public IP is chosen (You can modify this later if you have specific networking requirements). Finally, create the service.

![Create ECS Service](images/ECS_create_service.png "ECS Service creation")

### VPC and Network configuration for external access

A default VPC is automatically provisionned on every AWS account. It comes with a public subnet in each Availability Zone, an internet gateway, and settings to enable DNS resolution. For more information please see [here](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html).

This VPC also comes with default Security group. Please make sure to have the following configuration to enable external access to your processor. 

![Security group inbound](images/VPC_securitygroup_configuration_inbound.png "Security group inbound")

![Security group outbound](images/VPC_securitygroup_configuration_outbound.png "Security group outbound")

### CloudWatch
In other to monitor and troubleshoot any issue with your processor, it is recommended to enabled [Container Insight]() while creating your ECS Cluster. 

![Container Insight](images/ConteinerInsigth_configuration.png "Container Insight")

For more information please see [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html) 


## Automatic setup using Terraform script

This script will create the AWS ressources

### Option 1: Lambda deployment.

Here is the script for Lambda resource provisioning, it is also available in the Github repository.

```tf
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
```
>❗Note: if you are using a secret_id/secret_key as authentification method, please use the file aws_credentials.tfvars (in the terraform folder). Below the command to apply terraform script using credentials file:

```cmd
terraform apply -var-file="aws_credentials.tfvars"
```

### Option 2: ECS deployment.

Here is the script for Lambda resource provisioning, it is also available in the Github repository.

```tf
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

############################## specify your account # ##############################
variable "account_number" {
  description = "# AWS account"
  default     = "xxx"
}

variable "region_east" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "ecs-cluster-p3-aws-github"
}

variable "ecs_task_name" {
  description = "Name of the task definition"
  default     = "ecs-task-p3-aws-github"
}

variable "ecs_service_name" {
  description = "Name of the service"
  default     = "ecs-service-p3-aws-github"
}


resource "aws_vpc" "vpc_us_east_1" {
  cidr_block = "10.6.0.0/16"

  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
      Name = "vpc-p3-aws-github"
  }
}

resource "aws_subnet" "us_east_subnet1" {
  vpc_id = aws_vpc.vpc_us_east_1.id
  cidr_block = "10.6.4.0/24"

  tags = {
      Name = "subnet-p3-aws-github-1"
  }
}

resource "aws_subnet" "us_east_subnet2" {
  vpc_id = aws_vpc.vpc_us_east_1.id
  cidr_block = "10.6.5.0/24"

  tags = {
      Name = "subnet-p3-aws-github-2"
  }
}

resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = aws_vpc.vpc_us_east_1.id
  tags = {
    Name = "internet-gtw-p3-aws-github"
  }
}

resource "aws_route_table" "route_table" { 
  vpc_id = aws_vpc.vpc_us_east_1.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.internet_gateway.id
  }
    tags = {
      Name = "rt-p3-aws-github"
    }
}

resource "aws_route_table_association" "subnet_route" {
  subnet_id      = aws_subnet.us_east_subnet1.id
  route_table_id = aws_route_table.route_table.id
}

resource "aws_route_table_association" "subnet2_route" {
  subnet_id      = aws_subnet.us_east_subnet2.id
  route_table_id = aws_route_table.route_table.id
}

resource "aws_security_group" "security_group" {
  name   = "p3-aws-github-sg"
  vpc_id = aws_vpc.vpc_us_east_1.id
  description = "Shared security group."

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "allow_all_internal" {
  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  security_group_id = aws_security_group.security_group.id
  source_security_group_id = aws_security_group.security_group.id
}

/*
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })

  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
    "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
  ]
}
*/

resource "aws_ecs_cluster" "ecs_cluster" {
  name     = var.ecs_cluster_name

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}


############################## specify the name of the ECR docker registry image ##############################
resource "aws_ecs_task_definition" "ecs_task_definition" {
  family              = var.ecs_task_name
  network_mode        = "awsvpc"
  execution_role_arn  = "arn:aws:iam::${var.account_number}:role/ecsTaskExecutionRole"
  cpu                 = "256"
  memory              = "512"
  requires_compatibilities = ["FARGATE"]
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }
  container_definitions = jsonencode([
    {
      name      = "${var.ecs_task_name}"
      #image     = "${var.account_number}.dkr.ecr.${var.region_east}.amazonaws.com/${var.ecr_repository_name}:latest"
      image = "489065051964.dkr.ecr.us-east-1.amazonaws.com/ecr-p3-aws-github:782eb61ab99c5376ca485681772df91211fc5bfc"
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
          protocol      = "tcp"
        }
      ]
      log_configuration = {
        log_driver = "awslogs"
        options = {
          "awslogs-group" = "/ecs/my-service"
          "awslogs-region" = "${var.region_east}"
          "awslogs-stream-prefix" = "ecs"
        }
      }
    }
  ])
}


resource "aws_ecs_service" "ecs_service" {
  name            = var.ecs_service_name
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.ecs_task_definition.arn
  desired_count   = 1
  launch_type = "FARGATE"

  network_configuration {
    subnets         = [aws_subnet.us_east_subnet1.id, aws_subnet.us_east_subnet2.id]
    security_groups = [aws_security_group.security_group.id]
    assign_public_ip = true
  }

  triggers = {
    redeployment = timestamp()
  }
}

```
>❗Note: if you are using a secret_id/secret_key as authentification method, please use the file aws_credentials.tfvars (in the terraform folder). Below the command to apply terraform script using credentials file:

```cmd
terraform apply -var-file="aws_credentials.tfvars"
```

## Sizing
In order to keep, cost under control, we strongly encourage to implement service quotas using [AWS capabilities](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).


## More resources 

The following link might provide interesting information:
- [Security hardening with OpenbID Connect](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) 
- [Self-Service Provisioning of Terraform]https://aws.amazon.com/fr/blogs/aws/new-self-service-provisioning-of-terraform-open-source-configurations-with-aws-service-catalog/)
- [AWS Provisioning with Terraform]https://medium.com/avmconsulting-blog/provisioning-aws-infrastructure-with-terraform-6ab885fb3fcb)


