---
layout: default
title: Introduction
nav_order: 1
---


# Welcome to the Earthdaily Reflectance Datacube documentation

Earthdaily is offering sereral open processor showcasing how to levarage Earthdaily Agro content and combine it with your business logic and adapt it to your business workflows.

Each processor can be deployed on your infrastructure, using some available templates  or you can also use your own CI/CD pipelines.

The documentation will guide you through all the steps to get, customize and deploy the Reflectance Datacube processor including:

 - Provision AWS resources
    - Set up an identity provider for Github
    - Set up ECR in AWS
    - Create an ECS cluster, a service and a task definition in AWS
 - Configure depplyment workflow
    - Build and publish the docker image to ECR
    - Download and update a task definition
    - Update service with latest release

Please note that multiple other open processor are also available:
    - Analytic datacube to generate vegetation index ND objects based on geometries.
    - Agro warning processor to generate warning on small ag region based on weather and vegetation health.
    - Impacted area to analyze impact of an event with a before/after analysis.
    - Sub entity analysis to qualify the behavior of a sub area of an entity versus the entire area.
    
If you have any question, feel free to contact us Api.Support@earthdaily.com 
