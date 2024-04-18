---
layout: default
title: AWS ECS Deployment
parent: Deployment
nav_order: 1
---


# AWS ECS Deployment guide

The following sections will guide you through the steps to setup a GitAction workflow to deploy the Reflectance Datacube processor on AWS ECS.

## Github repo configuration
Before configuring the deployment workflow, set the deployment variables in the GitHub repository secrets for actions. The workflow requires these variables in order to successfully push the image.

![Github repository action secrets](../images/repo_secret.png "Github repository action secrets").



| Secret  | Description   |
|---|---|
|  AWS_REGION | This is the AWS region you are targeting for deployment  |
|  CONTAINER_NAME | Name of the container |
| ECR_REPOSITORY  | Container registry to publish your image  |
| ECS_CLUSTER  | ECS Cluster for container deployment   |
| ECS_SERVICE  | ECS Service for container deployment  |
| ECS_TASK_DEFINITION  | ECS Task definition for container deployment   |
|  EDS_API_URL | Base URL to access EarthData Store  |
|  EDS_AUTH_URL |  Base authentication URL to access EarthData Store |

## Deployment workflow
Whithin the Github repository, in the '.github/workflows, you will find a file ECS_deploy.yml

Edit the file by adding the branch name you want to deploy.

![Deployment workflow](../images/ECSDeploy_workflow_edit2.png "Deployment workflow").


The file should be as below:

```yaml
name: Deploy to Amazon ECS

on:
  push:
    branches:
      - main

env:
  AWS_REGION: ${{ secrets.AWS_REGION }}
  ECR_REPOSITORY: ${{ secrets.ECR_REPOSITORY }}
  ECS_SERVICE: ${{ secrets.ECS_SERVICE }}
  ECS_CLUSTER: ${{ secrets.ECS_CLUSTER }}
  CONTAINER_NAME: ${{ secrets.CONTAINER_NAME }}
  EDS_API_URL_SECRET: ${{ secrets.EDS_API_URL }}
  EDS_AUTH_URL_SECRET: ${{ secrets.EDS_AUTH_URL }}

permissions:
  id-token: write # This is required for requesting the JWT
  contents: read

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    environment: production

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Create envfile
        uses: SpicyPizza/create-envfile@v2.0
        with:
          envkey_EDS_API_URL: ${{ secrets.EDS_API_URL }}
          envkey_EDS_AUTH_URL: ${{ secrets.EDS_AUTH_URL }}
          envkey_INPUT_JSON_PATH: "data/processor_input_example.json"
          file_name: .env
          fail_on_empty: false
          sort_keys: false

      - name: configure aws credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::489065051964:role/GitHubActionProcessor-AssumeRoleWithAction #change to reflect your IAM role’s ARN
          role-session-name: GitHub_to_AWS_via_gitaction_devOps
          aws-region: ${{ env.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build, tag, and push image to Amazon ECR
        id: build-image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          # Build a docker container and
          # push it to ECR so that it can
          # be deployed to ECS.      
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          # docker tag $ECR_REPOSITORY:latest $ECR_REGISTRY/$ECR_REPOSITORY:latest
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          echo "image=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG" >> $GITHUB_OUTPUT

      - name: Download task definition
        run: |
          aws ecs describe-task-definition --task-definition fastapiprocessor --query taskDefinition > task-definition.json
          echo $(cat task-definition.json | jq 'del(
                    .taskDefinitionArn,
                    .requiresAttributes,
                    .compatibilities,
                    .revision,
                    .status,
                    .registeredAt,
                    .registeredBy
                )') > task-definition.json
          cat task-definition.json

      - name: Fill in the new image ID in the Amazon ECS task definition
        id: task-def
        uses: aws-actions/amazon-ecs-render-task-definition@v1
        with:
          task-definition: task-definition.json
          container-name: ${{ env.CONTAINER_NAME }}
          image: ${{ steps.build-image.outputs.image }}

      - name: updating task-definition file
        run: cat ${{ steps.task-def.outputs.task-definition }}

      - name: Deploy Amazon ECS task definition
        uses: aws-actions/amazon-ecs-deploy-task-definition@v1
        with:
          task-definition: ${{ steps.task-def.outputs.task-definition }}
          service: ${{ env.ECS_SERVICE }}
          cluster: ${{ env.ECS_CLUSTER }}
          wait-for-service-stability: true1

```

Finally commit changes and ensure that workflow is executed as planned. Go to the actions sections of the repository and you should see the execution steps and status.

![Workflow execution](images/workflow_execution.png "Workflow execution").

## More resources

Here is additional content related deployment:
   - [Deploying to ECS with GitActions](https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service)
   - [ECS Deployments](https://medium.com/@octavio/ecs-deployments-with-github-actions-dd34beed6528)