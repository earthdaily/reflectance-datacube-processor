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
