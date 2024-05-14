import datetime as dt
import logging
import os
import shutil
import tempfile

import boto3
import cloudpathlib
import fsspec
import xarray
import zarr
from azure.storage.blob import ContainerClient
from byoa.cloud_storage import aws_s3, azure_blob_storage

from api.constants import CloudStorageRepo

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def dataset_to_zarr_format_indep_sensor(
    dataset: xarray.Dataset,
    fieldid: str,
    start_date: dt.datetime,
    end_date: dt.datetime,
):
    """
    Save a xarray.Dataset as zarr format in a temporary folder.
    Output zarr path : "{start_date}_{end_date}_{fieldid}_datacube.zarr"

    Args:
        - dataset: the Dataset to save

    Returns:
        The complete zarr path
    """
    start_date_str = str(start_date)[:10]
    end_date_str = str(end_date)[:10]
    # Make a valid path whatever the OS
    zarr_path = os.path.join(
        tempfile.gettempdir(),
        f"{start_date_str}_{end_date_str}_{fieldid}_datacube.zarr",
    )
    logging.info("AnalyticsDatacube:save_dataset_to_temporary_zarr: path is %s", zarr_path)

    if os.path.exists(zarr_path):
        # Use shutil.rmtree to recursively delete the directory
        shutil.rmtree(zarr_path)
        print(f"The directory '{zarr_path}' existed so it has been deleted.")
    else:
        print(f"The directory '{zarr_path}' does not exist.")

    # save dataset and return complete zarr path
    dataset.to_zarr(zarr_path)
    return zarr_path


def dataset_to_zarr_format_sensor(
    dataset: xarray.Dataset,
    fieldid: str,
    start_date: dt.date,
    end_date: dt.date,
    sensor: str,
):
    """
    Save a xarray.Dataset as zarr format in a temporary folder.
    Output zarr path : "{start_date}_{end_date}_{fieldid}_{sensor}_datacube.zarr"

    Args:
        - dataset: the Dataset to save

    Returns:
        The complete zarr path
    """
    start_date_str = str(start_date)[:10]
    end_date_str = str(end_date)[:10]
    # Make a valid path whatever the OS
    zarr_path = os.path.join(
        tempfile.gettempdir(),
        f"{start_date_str}_{end_date_str}_{fieldid}_{sensor}_datacube.zarr",
    )
    logging.info("AnalyticsDatacube:save_dataset_to_temporary_zarr: path is %s", zarr_path)

    # save dataset and return complete zarr path
    dataset.to_zarr(zarr_path)
    return zarr_path


def upload_cube(zarr_path: str, cloud_storage: str, bucket_name: str = None):
    """
    Upload a zarr to a cloud storage.

    Args:
        - zarr_path: complete zarr path
        - cloud_storage : Name of the cloud storage selected

    Returns:
        The complete path to the zarr folder in the storage account.
    """
    # upload result on chosen CloudStorage provider (AWS or Azure)
    if cloud_storage == CloudStorageRepo.AWS:
        if bucket_name is None:
            bucket_name = os.getenv("AWS_BUCKET_NAME")

        aws_s3.write_folder_to_aws_s3(zarr_path, bucket_name=bucket_name)
        logger.info("EarthDaily DataCube uploaded to AWS S3")
        __delete_local_directory(zarr_path)
        link = aws_s3.get_s3_uri_path(zarr_path, bucket_name=bucket_name)
    elif (
        cloud_storage == CloudStorageRepo.AZURE
        and azure_blob_storage.upload_directory_to_azure_blob_storage(zarr_path)
    ):
        logger.info("EarthDaily DataCube uploaded to Azure Blob Storage")
        __delete_local_directory(zarr_path)
        link = azure_blob_storage.get_azure_blob_url_path(zarr_path)
    return link


def open_cube_azure(image: str):
    """
    Open Datacube from azure cloud storage.

    Args:
        - image: name of the image generated on the API

    Returns:
        The xarray.Dataset generated on the API.
    """

    # retrieve credentials
    account_storage = os.getenv("AZURE_ACCOUNT_NAME")
    account_url = f"https://{account_storage}.blob.core.windows.net"
    container_name = os.getenv("AZURE_BLOB_CONTAINER_NAME")
    credential = os.getenv("AZURE_SAS_CREDENTIAL")

    # Load container client
    container_client = ContainerClient(
        account_url=account_url, container_name=container_name, credential=credential
    )

    # Load zarr cube
    store = zarr.ABSStore(client=container_client, prefix=image)

    # Open and return cube as xarray Dataset
    return xarray.open_zarr(store=store, consolidated=True)


def open_datacube(
    path: cloudpathlib.S3Path | cloudpathlib.AzureBlobPath,
    order_id=None,
    refresh_interval=10,
    **kwargs,
):
    if order_id is not None:
        success, status = _wait_success(order_id, refresh_interval)
        if not success:
            raise Exception(f"Order {order_id} failed : {status}")
    if isinstance(path, cloudpathlib.S3Path):
        import s3fs

        credentials = path.client.sess.get_credentials()
        aws_access_key = credentials.access_key
        aws_secret_key = credentials.secret_key
        token = credentials.token

        s3 = s3fs.S3FileSystem(key=aws_access_key, secret=aws_secret_key, token=token)
        store = s3fs.S3Map(root=path.as_uri(), s3=s3, check=False)
    elif isinstance(path, cloudpathlib.AzureBlobPath):
        from dotenv import load_dotenv

        load_dotenv()
        import adlfs

        fs = adlfs.AzureBlobFileSystem(
            account_name=path.client.service_client.account_name,
            connection_string=None,
            account_key=None,
            # sas_token=path.client.service_client.url.split('?')[1])
            sas_token=os.getenv("AZURE_SAS_CREDENTIAL"),
        )
        store = fs.get_mapper(path.as_uri())
    else:
        raise NotImplementedError("Cloud provider not supported.")

    if "chunks" not in kwargs.keys():
        kwargs["chunks"] = "auto"
    if "consolidated" not in kwargs.keys():
        kwargs["consolidated"] = True
    dc = xarray.open_zarr(store, **kwargs)

    return dc


def __delete_local_directory(path: str):
    """
    Delete a local directory if it exists.

    Args:
        path (str): The path of the directory to delete.
    """
    # Remove local csv file
    if os.path.exists(path):
        logging.info("Delete local directory after upload")
        shutil.rmtree(path)
    else:
        logging.info("File not present.")
