---
layout: default
title: Reflectance Datacube Processor
nav_order: 2
---

# Reflectance Datacube Processor
Processors can be deployed on your infrastructure, using optimized easy-to-use templates.
You can also choose to use your own CI/CD pipelines.

The following documentation will guide you through, step-by-step, to get, customize and deploy the Reflectance Datacube processor including:

 - Provision AWS resources
    - Set up an identity provider for Github
    - Set up ECR in AWS
    - Create an ECS cluster, a service and a task definition in AWS
 - Configure depplyment workflow
    - Build and publish the docker image to ECR
    - Download and update a task definition
    - Update service with latest release

## Use cases

Earth Observation Image serves as a vital dataset for many applications including regenerative agriculture, insurance or food security and overall agriculture digitization.   Many models and decision support tools leverage cloud free pixel to remotely to extract information and knowledge on the status of the soil or the crop using a variety of spectral bands. 

The reflectance Datacube Processor will ease deployment of analysis ready pixel pipeline supporting modeling effort either at early stage with model design and training but also model serving with fresh and up to date pixels.

The reflectance datacube processor will ease the creation of multi dimensional dataset based on geometries of interest, without the need to download the full satellite images. The processor is leveraging cloud native geospatial capabilities to:

- Select pixels of interest based on temporal (date range) and spatial criterias (geometry)
- Select pixel within several image collections
    - Sentinel 2
    - Landsat 8/9
    - [Venµs](https://aws.amazon.com/marketplace/pp/prodview-qzaib3z674dbu)
    - soon [EarthDaily](https://earthdaily.com/constellation/)
 - Select band of interest
 - Apply cloud filter to get only clear pixels and leverage our [premium cloud mask](https://github.com/earthdaily/Studies-and-Analysis/tree/main/Auto-Cloud-Mask-Accuracy)  
 - Merge and cross calibrate data from several sources (for example Landsat and Sentinel)
 - Format data as Zarr asset
 - Publication to cloud storage
 
 >In geospatial data analysis, [Zarr](https://zarr.dev/) is one of these newly adopted data formats specifically for N-Dimensional arrays. It is an effective way to store large N-dimensional data in the cloud and access chunks.

Here are two examples of study leveraging pixel selection over fields:
  - for [sustainable practice qualification](https://www.mdpi.com/2072-4292/16/5/834)
  - for [yield modeling](https://www.sciencedirect.com/science/article/pii/S0168169923001953)

## Architecture

### AWS ECS

This is the reference architecture for a deployment on ECS. 

![ECS Architecture](images/ECS_Architecture.png "ECS Architecture")

### AWS Lambda

This is the reference architecture for a deployment on Lambda. 

![Lambda Architecture](images/Lambda_architecture.png "Lambda Architecture")