---
layout: default
title: AWS Customer Hosted FTR
parent: Deployment
nav_order: 3
---

# Customer-Deployed Foundational Technical Review

This is the summary of the Reflectance Processor FTR for ECSreview based on [AWS guidelines](https://apn-checklists.s3.amazonaws.com/foundational/customer-deployed/customer-deployed/C0hfGvKGP.html)

## Introduction

<table>
	<tbody>
		<tr>
			<td width="96">
				<p><strong>Req code</strong></p>
			</td>
			<td width="528">
				<p><strong>Requirement description</strong></p>
			</td>
			<td width="546">
				<p><strong>Content</strong></p>
			</td>
		</tr>
		<tr>
			<td width="96">
				<p>INT-001</p>
			</td>
			<td width="528">
				<p>Introductory material must contain use cases for the software.</p>
			</td>
			<td width="546">
				<p>This is covered in the <a href="Reflectance_processor.html">Reflectance Datacube processor</a> section.</p>
			</td>
		</tr>
		<tr>
			<td width="96">
				<p>INT-002</p>
			</td>
			<td width="528">
				<p>Introductory material contains an overview of a typical customer deployment, including lists of all resources that are set up when the deployment is complete.</p>
			</td>
			<td width="546">
				<p>This is covered in the <a href="Reflectance_processor.html">Reflectance Datacube processor</a> section on the architecture diagram.</p>
			</td>
		</tr>
		<tr>
			<td width="96">
				<p>INT-003</p>
			</td>
			<td width="528">
				<p>Introductory material contains a description of all deployment options discussed in the user guide (e.g. single-AZ, multi-AZ or multi-region), if applicable.</p>
			</td>
			<td width="546">
				<p>There is only one deployment method documented at this point. Please let us know if you need support to create new deployment pipelines.</p>
			</td>
		</tr>
		<tr>
			<td width="96">
				<p>INT-004</p>
			</td>
			<td width="528">
				<p>Introductory material contains the expected amount of time to complete the deployment.</p>
			</td>
			<td width="546">
				<p>Code packaging and publication to ECS is usually completed in less than 5 min. More info available in the <a href="Deploy/AWS%20ECS%20Deployment.html">ECS deployment section</a></p>
			</td>
		</tr>
		<tr>
			<td width="96">
				<p>INT-005</p>
			</td>
			<td width="528">
				<p>Introductory material contains the regions supported.</p>
			</td>
			<td width="546">
				<p>There is no limitation on region supported for this service.</p>
			</td>
		</tr>
	</tbody>
</table>

## Pre requisites and requirements

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>PRQ-001</p>
</td>
<td width="528">
<p>All technical prerequisites and requirements to complete the deployment process are listed (e.g. required OS, database type and storage requirements).</p>
</td>
<td width="546">
<p>This is covered in the <a href="Prerequisite.html">Prerequisites</a> section.</p>
</td>
</tr>
<tr>
<td width="96">
<p>PRQ-002</p>
</td>
<td width="528">
<p>The deployment guide lists all prerequisite skills or specialized knowledge (for example, familiarity with AWS, specific AWS services, or a scripting or programming language).</p>
</td>
<td width="546">
<p>This is covered in the <a href="Prerequisite.html">Prerequisites</a> section.</p>
</td>
</tr>
<tr>
<td width="96">
<p>PRQ-003</p>
</td>
<td width="528">
<p>The deployment guide lists the environment configuration that is needed for the deployment (e.g. an AWS account, a specific operating system, licensing, DNS).</p>
</td>
<td width="546">
<p>This is covered in the Prerequisites section.</p>
</td>
</tr>
</tbody>
</table>

## Architecture diagrams

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>ARCH-001</p>
</td>
<td width="528">
<p>Architecture diagrams must include all AWS services and resources deployed by the solution and illustrate how the services and resources connect with each other in a typical customer environment.</p>
</td>
<td width="546">
<p>This is covered in the <a href="Reflectance_processor.html#architecture">Reflectance Datacube processor section</a></p>
</td>
</tr>
<tr>
<td width="96">
<p>ARCH-004</p>
</td>
<td width="528">
<p>Architecture diagrams use official AWS Architecture Icons.</p>
</td>
<td width="546">
<p><a href="Reflectance_processor.html#architecture">Reflectance Datacube processor section</a> includes a diagram with official AWS Icon coming from <a href="https://aws.amazon.com/fr/architecture/icons/">here</a></p>
</td>
</tr>
<tr>
<td width="96">
<p>ARCH-005</p>
</td>
<td width="528">
<p>Network diagrams demonstrate virtual private clouds (VPCs) and subnets.</p>
</td>
<td width="546">
<p><a href="https://earthdailyagro-my.sharepoint.com/personal/vincent_lelandais_earthdaily_com/Documents/Reflectance_processor.html#architecture">Reflectance Datacube processor section</a> includes a diagram with VPC</p>
</td>
</tr>
<tr>
<td width="96">
<p>ARCH-006</p>
</td>
<td width="528">
<p>Architecture diagrams show integration points, including third-party assets/APIs and on-premises/hybrid assets.</p>
</td>
<td width="546">
<p><a href="https://earthdailyagro-my.sharepoint.com/personal/vincent_lelandais_earthdaily_com/Documents/Reflectance_processor.html#architecture">Reflectance Datacube processor section</a> includes a diagram with link to EarthPlatform (third party data infrastructure running on AWS)</p>
</td>
</tr>
</tbody>
</table>


## Security

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-002</p>
</td>
<td width="528">
<p>The application does not require the use of AWS account root privileges for deployment or operation.</p>
</td>
<td width="546">
<p>As detailed in the <a href="Prerequisite.html#aws">prerequisites section</a>, access to AWS ressoures is based on OIDC with specific role and specific trust relationship.</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-003</p>
</td>
<td width="528">
<p>The deployment guide provides prescriptive guidance on following the policy of least privilege for all access granted as part of the deployment.</p>
</td>
<td width="546">
<p>As defined in the <a href="Provisioning.html#configure-openid-connect">provisioning section</a>, deployment and execution is based on a specific role enforcing the least privilege principle.</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-004</p>
</td>
<td width="528">
<p>The deployment guide clearly documents any public resources (e.g. Amazon S3 buckets with bucket policies allowing public access).</p>
</td>
<td width="546">
<p>The deployment guide is not using public resources.</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-006</p>
</td>
<td width="528">
<p>The deployment guide describes the purpose of each AWS Identity and Access Management (IAM) role and IAM policy the user is instructed to create.</p>
</td>
<td width="546">
<p>The deployment guide includes a specific chapter on <a href="Provisioning.html#configure-openid-connect">IAM configuration and OIDC setup.</a></p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-007</p>
</td>
<td width="528">
<p>The deployment guide provides clear instruction on maintaining any stored secrets such as database credentials stored in AWS Secrets Manager.</p>
</td>
<td width="546">
<p>The deployment guide is not leveraging AWS Secrets Manager, but Github repository secrets as detailed <a href="Deploy/AWS%20ECS%20Deployment.html#github-repo-configuration">here</a>.</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-008</p>
</td>
<td width="528">
<p>The deployment guide includes details on where customer sensitive data are stored</p>
</td>
<td width="546">
<p>The deployment guide is enforcing AWS security guideline for Gitaction deployments and is only leveraging private resources,</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-009</p>
</td>
<td width="528">
<p>The deployment guide must explain all data encryption configuration (for example. Amazon Simple Storage Service (Amazon S3) server-side encryption, Amazon Elastic Block Store (Amazon EBS) encryption, and Linux Unified Key Setup (LUKS))</p>
</td>
<td width="546">
<p>Asset published by the Reflectance datacube processor are not encrypted. The non sensitive nature of the data (pixel from satellite images) does not require to leverage encryption</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-010</p>
</td>
<td width="528">
<p>For deployments involving more than a single element, include network configuration (for example, VPCs, subnets, security groups, network access control lists (network ACLs), and route tables) in the deployment guide.</p>
</td>
<td width="546">
<p>The proposed service is a single container deployment. The only specific VPC configuration is detailed in the</p>
</td>
</tr>
<tr>
<td width="96">
<p>DSEC-011</p>
</td>
<td width="528">
<p>The solution must support the ability for the customer to disable Instance Metadata Service Version 1 (IMDSv1).</p>
</td>
<td width="546">
<p>AWS Fargate does not offer direct control over the Instance Metadata Service (IMDS). To mitigate risk linked with IMDS we are using the least privilege principle with a specific role for task execution and specific security group and VPC to control network access to Fargate tasks.</p>
</td>
</tr>
</tbody>
</table>

## Costs

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>CST-001</p>
</td>
<td width="528">
<p>The deployment guide includes a list of billable services and guidance on whether each service is mandatory or optional.</p>
</td>
<td width="546">
<p><a href="6.Lifecycle_management.html#costs">This is detailed in the lifecycle management sections.</a></p>
</td>
</tr>
<tr>
<td width="96">
<p>CST-002</p>
</td>
<td width="528">
<p>The deployment guide includes the cost model and licensing costs.</p>
</td>
<td width="546">
<p><a href=".Lifecycle_management.html#costs">This is detailed in the lifecycle management sections.</a></p>
</td>
</tr>
</tbody>
</table>


## Sizing

<table>
<tbody>
<tr>
<td width="84">
<p><strong>Req code</strong></p>
</td>
<td width="260">
<p><strong>Requirement description</strong></p>
</td>
<td width="280">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="84">
<p>DAS-001</p>
</td>
<td width="260">
<p>The deployment guide provides step-by-step instructions for deploying the workload on AWS according to the typical deployment architecture.</p>
</td>
<td width="280">
<p>The deployment guide includes step by step procedure to <a href="Provisioning.html">provision AWS resources</a> and a <a href="Deploy/AWS%20ECS%20Deployment.html">script to automatically deploy assets to AWS</a></p>
</td>
</tr>
<tr>
<td width="84">
<p>DAS-004</p>
</td>
<td width="260">
<p>The deployment guide contains prescriptive guidance for testing and troubleshooting.</p>
</td>
<td width="280">
<p>The deployment guide contains a <a href="User%20guide.html">user guide section.</a></p>
</td>
</tr>
</tbody>
</table>

## Deployment assets

<table>
<tbody>
<tr>
<td width="84">
<p><strong>Req code</strong></p>
</td>
<td width="260">
<p><strong>Requirement description</strong></p>
</td>
<td width="280">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="84">
<p>DAS-001</p>
</td>
<td width="260">
<p>The deployment guide provides step-by-step instructions for deploying the workload on AWS according to the typical deployment architecture.</p>
</td>
<td width="280">
<p>The deployment guide includes step by step procedure to <a href="Provisioning.html">provision AWS resources</a> and a <a href="Deploy/AWS%20ECS%20Deployment.html">script to automatically deploy assets to AWS</a></p>
</td>
</tr>
<tr>
<td width="84">
<p>DAS-004</p>
</td>
<td width="260">
<p>The deployment guide contains prescriptive guidance for testing and troubleshooting.</p>
</td>
<td width="280">
<p>The deployment guide contains a <a href="User%20guide.html">user guide section.</a></p>
</td>
</tr>
</tbody>
</table>

## Health Check

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>HLCH-001</p>
</td>
<td width="528">
<p>The deployment guide provides step-by-step instructions for how to assess and monitor the health and proper function of the application.</p>
</td>
<td width="546">
<p>This is detailed in the <a href="Lifecycle_management.html#backup-and-recovery">lifecycle management</a> section.</p>
</td>
</tr>
</tbody>
</table>

## Back up and recovery
  
<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>BAR-001</p>
</td>
<td width="528">
<p>Identify the data stores and the configurations to be backed up. If any of the data stores are proprietary, provide step-by-step instructions for backup and recovery.</p>
</td>
<td width="546">
<p>This is detailed in the <a href="Lifecycle_management.html#backup-and-recovery">lifecycle management</a> section.</p>
</td>
</tr>
</tbody>
</table>

## Routine Maintenance  

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>RM-001</p>
</td>
<td width="528">
<p>The deployment guide provides step-by-step instructions for rotating programmatic system credentials and cryptographic keys.</p>
</td>
<td width="546">
<p>Deployment pipeline is using OIDC with short term tokens. Regarding EarthPlatform authentication we are using OAuth 2.0 with short term tokens. Credentials will be updated based on EarthPlatform security guidelines.</p>
</td>
</tr>
<tr>
<td width="96">
<p>RM-002</p>
</td>
<td width="528">
<p>The deployment guide provides prescriptive guidance for software patches and upgrades.</p>
</td>
<td width="546">
<p>Processor update will be delivered on the public GitHub repo. It is strongly recommended for customers to run regression testing before deploying this release.</p>
</td>
</tr>
<tr>
<td width="96">
<p>RM-003</p>
</td>
<td width="528">
<p>The deployment guide provides prescriptive guidance on managing licenses.</p>
</td>
<td width="546">
<p>Users need to comply with EarthDaily EULA and services quotas on data access based on service agreement executed between parties.</p>
</td>
</tr>
<tr>
<td width="96">
<p>RM-004</p>
</td>
<td width="528">
<p>The deployment guide provides prescriptive guidance on managing AWS service limits.</p>
</td>
<td width="546">
<p>&nbsp;This is detailed in the <a href="Lifecycle_management.html#backup-and-recovery">lifecycle management</a> section.</p>
</td>
</tr>
</tbody>
</table>

## Emergency Maintenance

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>EMER-001</p>
</td>
<td width="528">
<p>The deployment guide provides step-by-step instructions on handling fault conditions.</p>
</td>
<td width="546">
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td width="96">
<p>EMER-002</p>
</td>
<td width="528">
<p>The deployment guide provides step-by-step instructions on how to recover the software.</p>
</td>
<td width="546">
<p>&nbsp;</p>
</td>
</tr>
</tbody>
</table>

## Support

<table>
<tbody>
<tr>
<td width="96">
<p><strong>Req code</strong></p>
</td>
<td width="528">
<p><strong>Requirement description</strong></p>
</td>
<td width="546">
<p><strong>Content</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p><strong>&nbsp;</strong></p>
</td>
<td width="528">
<p><strong>&nbsp;</strong></p>
</td>
<td width="546">
<p><strong>&nbsp;</strong></p>
</td>
</tr>
<tr>
<td width="96">
<p>SUP-001</p>
</td>
<td width="528">
<p>The deployment guide provides details on how to receive support.</p>
</td>
<td width="546">
<p>User support is described <a href="User%20guide.html#support">here</a></p>
</td>
</tr>
<tr>
<td width="96">
<p>SUP-002</p>
</td>
<td width="528">
<p>The deployment guide provides details on technical support tiers.</p>
</td>
<td width="546">
<p>Processor update will be delivered on the public GitHub repo. It is strongly recommended for customers to run regression testing before deploying this release.</p>
</td>
</tr>
<tr>
<td width="96">
<p>SUP-003</p>
</td>
<td width="528">
<p>The deployment guide provides prescriptive guidance on managing licenses.</p>
</td>
<td width="546">
<p>Users need to comply with EarthDaily EULA and services quotas on data access based on service agreement executed between parties.</p>
</td>
</tr>
</tbody>
</table>