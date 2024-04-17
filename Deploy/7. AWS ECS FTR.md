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


## Architecture diagrams


## Security




## Costs



## Sizing

## Deployment assets

## Health Check

## Back up and recovery
  
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