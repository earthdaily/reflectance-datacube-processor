---
layout: default
title: Lifecycle management
nav_order: 8
---


# Processor lifecycle management

## Health check

### Run ECR image locally

Please make sure to have docker and Python installed locally (see [Pre requisites](https://earthdaily.github.io/reflectance-datacube-processor/2.%20Prerequisite.html))

Open terminal and get [AWS CLI](https://pypi.org/project/awscli/)

1. Get authenticated to your AWS account (you will need to get an access key ID and Secret Access Key) using the command `aws configure`

2. ECR authentication

    ```shell
    aws ecr get-login-password --region <AWS REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS REGION>.amazonaws.com
    ```
3. Pull image from ECR 

    ```shell
    docker pull <AWS_ACCOUNT_ID>.dkr.ecr.<AWS REGION>.amazonaws.com/<ECR)REPOSITORY>:<CONTAINER_TAG>
    ```

4. Once image is available locally, please follow [user guide](https://earthdaily.github.io/reflectance-datacube-processor/5.%20User%20guide.html) to run the procossor

### Get access to API from ECS

Open your AWS Console and select ECS service. Navigate to your cluster, then service and finally task running your container. On configuration section of the screen you will find the public IP to access the service. 

![Get public IP](images/Get_public_IP.png "Get public IP").

Use this public IP and add  "/docs" to access the Open API page.

![Get public IP](images/ReflectanceDataCube_API2.png "Get public IP").

Then you can use the API as described [here](5.%20User%20guide.html#api-mode)

## Maintenance


### Routine maintenance


### Emergency maintenance






## Backup and recovery
For backup,please be sure to keep the various images of your service in the configured ECR repository. We recommend that you tag your images using the git SHA for the git commit that was used to build the image.

ECR repo will enable restoration of any version of your service.

## Costs

The use of this processor is free but it will rely on infrastructure to run.

If you are using the ECS deployment model, it will leverage the following billable AWS sercices:
 - Identity and Access Management (IAM)
 - Elastic Container Registry (ECR)
 - Elastic Container Service (ECS)
 - Virtual Private Cloud (VPC)
 - Cloud watch 
 - Simple Storage Service (S3)


### Additional Information

For any additional information, please contact our [support team](Api.Support@geosys.com)

The following link might provide interesting information:
- ...









