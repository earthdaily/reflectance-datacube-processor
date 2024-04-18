---
layout: default
title: AWS ECS FTR
parent: Deployment
nav_order: 2
---

# Customer-Deployed Foundational Technical Review

This is the summary of the Reflectance Processor FTR for ECSreview based on [AWS guidelines](https://apn-checklists.s3.amazonaws.com/foundational/customer-deployed/customer-deployed/C0hfGvKGP.html)

## Introduction

<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">INT-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Introductory material must contain use cases for the software.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is covered in the Introduction section</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">INT-002</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Introductory material contains an overview of a typical customer deployment, including lists of all resources that are set up when the deployment is complete.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is covered in the Introduction section</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">INT-003</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Introductory material contains a description of all deployment options discussed in the user guide (e.g. single-AZ, multi-AZ or multi-region), if applicable.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>There is only one deployment method documented at this point. Please let us know if you need support to create new deployment pipelines.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">INT-004</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Introductory material contains the expected amount of time to complete the deployment.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Code packaging and publication to ECS is usually completed in less than 5 min. More info available in the ECS deployment section</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">INT-005</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Introductory material contains the regions supported.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>There is no limitation on region supported for this service.</p>
            </td>
        </tr>
    </tbody>
</table>

## Pre requisites and requirements
<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">PRQ-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>All technical prerequisites and requirements to complete the deployment process are listed (e.g. required OS, database type and storage requirements).</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is covered in the Prerequisites section.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">PRQ-002</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide lists all prerequisite skills or specialized knowledge (for example, familiarity with AWS, specific AWS services, or a scripting or programming language).</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is covered in the Prerequisites section.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">PRQ-003</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide lists the environment configuration that is needed for the deployment (e.g. an AWS account, a specific operating system, licensing, DNS).</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is covered in the Prerequisites section.</p>
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

<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">DSEC-002</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The application does not require the use of AWS account root privileges for deployment or operation.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>As detailed in the <a href="Prerequisite.html#aws">prerequisites section</a>, access to AWS ressoures is based on OIDC &nbsp;with specific role and specific trust relationship.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-003</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides prescriptive guidance on following the policy of least privilege for all access granted as part of the deployment.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>As defined in the <a href="Provisioning.html#configure-openid-connect">provisioning section</a>, deployment and execution is based on a specific roles enforcing the least priviliege principle.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-004</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide clearly documents any public resources (e.g. Amazon S3 buckets with bucket policies allowing public access).</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide is not using public resources.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-006</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide describes the purpose of each AWS Identity and Access Management (IAM) role and IAM policy the user is instructed to create.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide includes a specific chapter on <a href="Provisioning.html#configure-openid-connect">IAM configuration and OIDC setup.</a></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-007</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides clear instruction on maintaining any stored secrets such as database credentials stored in AWS Secrets Manager.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide is not leveraging AWS Secrets Manager but Github &nbsp;repository secrets as detailed <a href="Deploy/AWS%20ECS%20Deployment.html#github-repo-configuration">here</a>.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-008</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide includes details on where customer sensitive data are stored</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide is enforcing AWS security guideline for Gitaction deployments and is only leveraging &nbsp;private resources,</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-009</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide must explain all data encryption configuration (for example. Amazon Simple Storage Service (Amazon S3) server-side encryption, Amazon Elastic Block Store (Amazon EBS) encryption, and Linux Unified Key Setup (LUKS))</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Asset published by the Reflectance datacube processor are not encrypted. The non sensitive nature of the data (pixel from satellite images) does not require to leverage encryption</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-010</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>For deployments involving more than a single element, include network configuration (for example, VPCs, subnets, security groups, network access control lists (network ACLs), and route tables) in the deployment guide.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The proposed service is a single container deployment. The only specific VPC configuration is detailed in the</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">DSEC-011</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The solution must support the ability for the customer to disable Instance Metadata Service Version 1 (IMDSv1).</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>AWS Fargate does not offer direct control over the Instance Metadata Service (IMDS). To mitigate risk linked with IMDS &nbsp;we are using the least privilege principle with a specific role for task execution and specific security group and VPC to control network access to Fargate tasks.</p>
            </td>
        </tr>
    </tbody>
</table>

## Costs

<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">CST-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide includes a list of billable services and guidance on whether each service is mandatory or optional.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><a href="6.Lifecycle_management.html#costs">This is detailed in the lifecycle management sections.</a></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">CST-002</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide includes the cost model and licensing costs.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><a href="https://earthdailyagro-my.sharepoint.com/personal/vincent_lelandais_earthdaily_com/Documents/6.Lifecycle_management.html#costs">This is detailed in the lifecycle management sections.</a></p>
            </td>
        </tr>
    </tbody>
</table>


## Sizing

## Deployment assets
<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 62.75pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 194.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 210.05pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 62.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">DAS-001</span></p>
            </td>
            <td style="width: 194.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides step-by-step instructions for deploying the workload on AWS according to the typical deployment architecture.</p>
            </td>
            <td style="width: 210.05pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide includes step by step procedure to <a href="Provisioning.html">provision AWS resources</a> and a <a href="Deploy/AWS%20ECS%20Deployment.html">script to automatically deploy &nbsp;assets to AWS</a></p>
            </td>
        </tr>
        <tr>
            <td style="width: 62.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">DAS-004</span></p>
            </td>
            <td style="width: 194.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide contains prescriptive guidance for testing and troubleshooting.</p>
            </td>
            <td style="width: 210.05pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide contains a <a href="User%20guide.html">user guide section.</a></p>
            </td>
        </tr>
    </tbody>
</table>

## Health Check

<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">HLCH-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides step-by-step instructions for how to assess and monitor the health and proper function of the application.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is detailed in the <a href="https://earthdaily.github.io/reflectance-datacube-processor/6.Lifecycle_management.html">lifecycle management</a> sections.</p>
            </td>
        </tr>
    </tbody>
</table>

## Back up and recovery
  
<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">BAR-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Identify the data stores and the configurations to be backed up. If any of the data stores are proprietary, provide step-by-step instructions for backup and recovery.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>This is detailed in the <a href="Lifecycle_management.html#backup-and-recovery">lifecycle management</a> sections.</p>
            </td>
        </tr>
    </tbody>
</table>

## Routine Maintenance  


## Emergency Maintenance

## Support

<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 71.8pt;border: 1pt solid windowtext;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Req code</strong></p>
            </td>
            <td style="width: 395.7pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Requirement description</strong></p>
            </td>
            <td style="width: 409.2pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0in 5.4pt;height: 22pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><strong>Content</strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;background:white;'><span style="font-family:Roboto;color:#16191F;">SUP-001</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides details on how to receive support.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>User support is described <a href="../5.%20User%20guide.html#support">here</a></p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;height: 49.9pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">SUP-002</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 49.9pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides details on technical support tiers.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;height: 49.9pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Processor update will be delivered on the public GitHub repo. It is strongly recommended for customers to run regression testing before deploying this release.</p>
            </td>
        </tr>
        <tr>
            <td style="width: 71.8pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'><span style="font-family:Roboto;color:#16191F;">SUP-003</span></p>
            </td>
            <td style="width: 395.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>The deployment guide provides prescriptive guidance on managing licenses.</p>
            </td>
            <td style="width: 409.2pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0in 5.4pt;vertical-align: top;">
                <p style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;line-height:normal;font-size:16px;font-family:"Aptos",sans-serif;'>Users need to comply with EarthDaily EULA and services quotas on data access based on service agreement executed between parties.</p>
            </td>
        </tr>
    </tbody>
</table>