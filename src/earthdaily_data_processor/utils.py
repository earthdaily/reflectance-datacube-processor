import logging
import xarray
from datetime import datetime
import tempfile
import os
import datetime as dt
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from cloud_storage import cloud_storage_aws, cloud_storage_azure
from api.constants import CloudStorageRepo

def dataset_to_zarr_format_indep_sensor(dataset: xarray.Dataset,
                                        fieldID:str,
                                        start_date: dt.date,
                                        end_date: dt.date):
    """
        Save a xarray.Dataset as zarr format in a temporary folder.
        Output zarr path : "\{start_date}_{end_date}_{fieldID}_datacube.zarr"

        Args:
            - dataset: the Dataset to save

        Returns:
            The complete zarr path
    """
    # Make a valid path whatever the OS
    zarr_path = os.path.join(tempfile.gettempdir(),
                             f"{start_date}_{end_date}_{fieldID}_datacube.zarr")
    logging.info("AnalyticsDatacube:save_dataset_to_temporary_zarr: path is " + zarr_path)

    # save dataset and return complete zarr path
    dataset.to_zarr(zarr_path)
    return zarr_path

def dataset_to_zarr_format_sensor(dataset: xarray.Dataset,
                                  fieldID:str,
                                  start_date: dt.date,
                                  end_date: dt.date,sensor: str):
    """
        Save a xarray.Dataset as zarr format in a temporary folder.
        Output zarr path : "\{start_date}_{end_date}_{fieldID}_{sensor}_datacube.zarr"

        Args:
            - dataset: the Dataset to save

        Returns:
            The complete zarr path
    """
    # Make a valid path whatever the OS
    zarr_path = os.path.join(tempfile.gettempdir(),
                             f"{start_date}_{end_date}_{fieldID}_{sensor}_datacube.zarr")
    logging.info("AnalyticsDatacube:save_dataset_to_temporary_zarr: path is " + zarr_path)

    # save dataset and return complete zarr path
    dataset.to_zarr(zarr_path)
    return zarr_path

def upload_cube(zarr_path: str, 
                cloud_storage: str):
    """
        Upload a zarr to a cloud storage.

        Args:
            - zarr_path: complete zarr path
            - cloud_storage : Name of the cloud storage selected

        Returns:
            The complete path to the zarr folder in the storage account.
    """
    # upload result on chosen CloudStorage provider (AWS or Azure)
    if cloud_storage == CloudStorageRepo.AWS and cloud_storage_aws.upload_folder_to_aws_s3(zarr_path):
        logger.info("EarthDaily DataCube uploaded to AWS S3")
        link = cloud_storage_aws.get_s3_uri_path(zarr_path)
    elif cloud_storage == CloudStorageRepo.AZURE and cloud_storage_azure.upload_directory_to_azure_blob_storage(
            zarr_path):
        logger.info("EarthDaily DataCube uploaded to Azure Blob Storage")
        link = cloud_storage_azure.get_azure_blob_url_path(zarr_path)
    return(link)
