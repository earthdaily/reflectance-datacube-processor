<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br>
<div align="center">
  <a href="https://github.com/GEOSYS">
    <img src="https://earthdailyagro.com/wp-content/uploads/2022/01/Logo.svg" alt="Logo" width="400" height="200">
  </a>
  
  <h1>EarthDaily Data Processor</h1>

  <p>
    Learn how to use &lt;geosys/&gt; platform capabilities in your own business workflow! Build your processor and learn how to run them on your platform.
    <br>
    <a href="https://earthdailyagro.com/"><strong>Who we are</strong></a>
  </p>

  <p>
    <a href="https://github.com/GEOSYS/earthdaily-data-processor/issues">Report Bug</a>
    ·
    <a href="https://github.com/GEOSYS/earthdaily-data-processor/issues">Request Feature</a>
  </p>
</div>

<div align="center"></div>

<div align="center">
  
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]
[![Youtube][youtube-shield]][youtube-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>


<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisite](#prerequisite)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run the processor in a Docker container](#run-the-processor-in-a-docker-container)
  - [Leverage datacube to generate analytics within a Jupyter Notebook](#leverage-datacube-to-generate-analytics-within-a-jupyter-notebook)
- [Project Organization](#project-organization)
- [Resources](#resources)
- [Support development](#support-development)
- [License](#license)
- [Contact](#contact)
- [Copyrights](#copyrights)
   
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<p> The aim of this project is to help our customers valuing our data platform capabilities to build their own analytics. </p>

The purpose of this example is to demonstrate how to extract pixel of interest from our EarthData Store based on a geometry and data selection criterias like sensors and band of interest, access to standard of premium cloud mask and publish results as a n dimension object (zarr file) on cloud storage location. Extracted data can be used to support analysis and analytic creation like in the notebook showcasing how to generate a vegatation index for non cloudy dates leveraging spatial dimensions of the dataset or how to plot vegetation index evolution over time.

It highlights the ability to quickly create pixel pipeline and generate n dimension reflectance objects in [xarray](https://docs.xarray.dev/en/stable/) format. 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisite

 <p align="left">
Use of this project requires valids credentials from the &ltgeosys/&gt platform . If you need to get trial access, please register <a href=https://earthdailyagro.com/geosys-registration/>here</a>.
</p>

To be able to run this example, you will need to have following tools installed:

1. Install Conda: please install Conda on your computer. You can download and install it by following the instructions provided on the [official Conda website](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

2. Install Docker Desktop: please install Docker Desktop on your computer. You can download and install it by following the instructions provided on the [official Docker Desktop website](https://docs.docker.com/desktop/)

3. Install Jupyter Notebook: please install jupyter Notebook on your computer following the instructions provided on the [official Jupyter website](https://jupyter.org/install)

4. Install Git: please install Github on your computer. You can download and install it by visiting <a href=https://desktop.github.com/>here</a> and following the provided instructions


This package has been tested on Python 3.9.7.

<p align="right">(<a href="#top">back to top</a>)</p>


### Installation

To set up the project, follow these steps:

1. Clone the project repository:
    
    ```
    git clone https://github.com/GEOSYS/earthdaily-data-processor

    ```

2. Change the directory:

    ```
    cd earthdaily-data-processor
    ```
3. Fill the environment variable (.env)

Ensure that you populate the .env file with your credentials. If you haven't acquired the credentials yet, please [click](https://earthdailyagro.com/geosys-registration) here to obtain them.

```
API_CLIENT_ID = <your client id>
API_CLIENT_SECRET = <your client id>
API_USERNAME = <your username>
API_PASSWORD = <your password>
```

To access and use our Catalog STAC named "Skyfox," please ensure that you have the following environment variables set in your .env file:

```
SKYFOX_URL = https://api.eds.earthdaily.com/archive/v1/stac/v1
SKYFOX_AUTH_URL = <skyfox auth url>
SKYFOX_CLIENT_ID =  <your client id>
SKYFOX_SECRET = <your client id>
```

To publish results on cloud storage, please add your credentials allowing the processor to write outputs:

```
AWS_ACCESS_KEY_ID = <...>
AWS_SECRET_ACCESS_KEY = <...>
AWS_BUCKET_NAME = <...>

AZURE_ACCOUNT_NAME = <...>
AZURE_BLOB_CONTAINER_NAME = <...>
AZURE_SAS_CREDENTIAL = <...>
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE -->
## Usage

### Run the processor in a Docker container

To set up and run the project using Docker, follow these steps:

1. Build the Docker image locally:

    ```
    docker build --tag example1 .
    ```

2. Run the Docker container:
    
    ```
    docker run -d --name example1_container -p 8081:80 example1
    ```

3. Access the API by opening a web browser and navigating to the following URL:
    
    ```
    http://127.0.0.1:8081/docs
    ```


This URL will open the Swagger UI documentation, click on the "Try it out" button under each POST endpoint and enter the request parameters and body

#### POST /earthdaily-data-processor:

Parameters:
  - Cloud storage repo, ex: "AWS_S3"
  - Collections, ex: "Venus-l2a"
  - Assets, ex: "red"
  - Cloud mask, ex: "native"
  - Sensor cross calibration, ex: "yes"

Body Example:

```json
{
  "geometry": "POLYGON ((1.26 43.427, 1.263 43.428, 1.263 43.426, 1.26 43.426, 1.26 43.427))",
  "startDate": "2019-05-01",
  "endDate": "2019-05-31",
  "EntityID": "entity_1"
}
```

### Leverage datacube to generate analytics within a Jupyter Notebook

To use Jupyter Notebook of the project, please follow these steps:


1. Create a Conda environment:

    ```
    conda create -y --name demo
    ```


2. Activate the Conda environment:

    ```
    conda activate demo
    ```


3. Install the project dependencies. You can do this by running the following command in your terminal:

    ```
    conda install -y pip
    pip install -r requirements.txt
    pip install ipykernel
    ```
4. Set up the Jupyter Notebook kernel for the project:

    ```
    python -m ipykernel install --user --name demo --display-name example1
    ```
5. Open the example notebook (datacube-sustainable-practices.ipynb) by clicking on it.



6. Select the "Kernel" menu and choose "Change Kernel". Then, select "example1" from the list of available kernels.


7. Run the notebook cells to execute the code example and plot results. 

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- PROJECT ORGANIZATION -->
## Project Organization


    ├── README.md         
    ├── notebooks    
    │   ├───datacube-sustainable-practices.ipynb 
    ├── requirements.txt    
    ├── environment.yml   
    │── Dockerfile
    │── .env
    │── LICENSE
    │── VERSION
    ├── setup.py         
    ├───src                
    │   ├───main.py 
    │   ├───test.py 
    │   ├───api
    │   │   ├── files
    │   │   │   └── favicon.svg
    │   │   ├── __init__.py
    │   │   └── api.py
    │   └───analytics_datacube
    │       ├── __init__.py
    │       ├── utils.py
    │       ├── processor.py
    │       ├── metacube.py
    └── test_environment.py         

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- RESOURCES -->
## Resources 
The following links will provide access to more information:
- [EarthDaily agro developer portal  ](https://developer.geosys.com/)
- [Pypi package](https://pypi.org/project/earthdaily/)
- [Analytic processor template](https://github.com/GEOSYS/Analytic-processor-template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Support development

If this project has been useful, that it helped you or your business to save precious time, don't hesitate to give it a star.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the [MIT License](https://github.com/GEOSYS/earthdaily-data-processor/blob/main/LICENSE). 

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

For any additonal information, please [email us](mailto:sales@earthdailyagro.com).

<p align="right">(<a href="#top">back to top</a>)</p>

## Copyrights

© 2023 Geosys Holdings ULC, an Antarctica Capital portfolio company | All Rights Reserved.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- List of available shields https://shields.io/category/license -->
<!-- List of available shields https://simpleicons.org/ -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=social
[NETcore-shield]: https://img.shields.io/badge/.NET%20Core-6.0-green
[NETcore-url]: https://github.com/dotnet/core
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=plastic&logo=appveyor
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/earthdaily-data-processor/repo.svg?style=plastic&logo=appveyor
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/GEOSYS/earthdaily-data-processor/repo.svg?style=social
[issues-url]: https://github.com/GEOSYS/earthdaily-data-processor/issues
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=social&logo=linkedin
[linkedin-url]: https://www.linkedin.com/company/earthdailyagro/mycompany/
[twitter-shield]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[twitter-url]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[youtube-shield]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[youtube-url]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[language-python-shiedl]: https://img.shields.io/badge/python-3.9-green?logo=python
[language-python-url]: https://pypi.org/ 
[GitStars-shield]: https://img.shields.io/github/stars/GEOSYS?style=social
[GitStars-url]: https://img.shields.io/github/stars/GEOSYS?style=social
[CITest-shield]: https://img.shields.io/github/workflow/status/GEOSYS/earthdaily-data-processor/Continous%20Integration
[CITest-url]: https://img.shields.io/github/workflow/status/GEOSYS/earthdaily-data-processor/Continous%20Integration
