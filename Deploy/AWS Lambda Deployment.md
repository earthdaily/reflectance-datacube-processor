---
layout: default
title: AWS Lambda Deployment
parent: Deployment
nav_order: 1
---


# AWS Lambda Deployment guide

The following sections will guide you through the steps to setup a GitAction workflow to deploy the Reflectance Datacube processor on [AWS Lambda](https://aws.amazon.com/fr/pm/lambda/?gclid=Cj0KCQjw0MexBhD3ARIsAEI3WHKHFIwpgJl1S8X0Brj35ffpgeqoxbbMuqzSE_5beUpN6smZBPArjosaApH_EALw_wcB&trk=e0e0d4be-47fe-4336-ab69-7eece7f3d36e&sc_channel=ps&ef_id=Cj0KCQjw0MexBhD3ARIsAEI3WHKHFIwpgJl1S8X0Brj35ffpgeqoxbbMuqzSE_5beUpN6smZBPArjosaApH_EALw_wcB:G:s&s_kwcid=AL!4422!3!652240143523!e!!g!!amazon%20lambda!19878797032!147151597893).

Before starting the deployment configuration, please make sure to check the [prerequisite section](Prerequisite.html).

Infrastructure setup is detailed on the [provisioning section](Provisioning.html).

## Clone repository

Please clone the Reflectance Datacube Processor on your Github account. 

Detailed process is available [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## Github repo configuration
Before configuring the deployment workflow, set the deployment variables in the GitHub repository secrets for actions. The workflow requires these variables in order to successfully push the image.

![Github repository action secrets](../images/repo_secret.png "Github repository action secrets").


| Secret  | Description   |
|---|---|
| AWS_REGION | This is the AWS region you are targeting for deployment  |
| CONTAINER_NAME | Name of the container |
| ECR_REPOSITORY  | Container registry to publish your image  |
| ECS_CLUSTER  | ECS Cluster for container deployment   |
| ECS_SERVICE  | ECS Service for container deployment  |
| ECS_TASK_DEFINITION  | ECS Task definition for container deployment   |
| EDS_API_URL | Base URL to access EarthData Store  |
| EDS_AUTH_URL |  Base authentication URL to access EarthData Store |
| AWS_ACCESS_KEY_ID  |  S3 Access key to push datacube assets |
| AWS_SECRET_ACCESS_KEY |  S3 Secret Access key to push datacube assets |
| DEPLOY_LAMBDA |  Boolean value to enable Lambda deployment (deplyoed to Lambda if True) |

## Deployment workflow
Whithin the Github repository, in the '.github/workflows, you will find a file AWS_deploy.yml

Edit the file by adding the branch name you want to deploy.

![Deployment workflow](../images/ECSDeploy_workflow_edit2.png "Deployment workflow").


## Deployment workflow execution

On every commit change, workflow is triggered and executed. Go to the actions sections of the repository and you should see the execution steps and status.

![Workflow execution](../images/workflow_execution.png "Workflow execution").

## More resources

Here is additional content related deployment:
   - [Deploying to Lambda  with GitActions](https://github.com/int128/deploy-lambda-action)
   - [Step by step guide for AWS Lambda with Docker ](https://medium.com/@denissedamian/step-by-step-guide-to-ci-cd-for-aws-lambda-with-docker-and-github-actions-c02a9726fd44)
   - [Deployment with AWS Lambda and ECS](https://dev.to/eldritchideen/fastapi-container-deployment-with-aws-lambda-and-amazon-ecs-5a2o)