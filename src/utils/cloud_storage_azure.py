import logging
import os

from azure.storage.blob import BlobServiceClient


def _validate_access_info(account_name, blob_container_name, sas_credential):
    return (
        account_name is not None
        and blob_container_name is not None
        and sas_credential is not None
        and account_name != ""
        and blob_container_name != ""
        and sas_credential != ""
    )


def _get_access_info():
    """
    get access account information
    Returns:
        - account_name: Azure Blob Storage account name.
        - blob_container_name: Name of the blob container.
        - sas_credential: SAS credential for accessing the blob container.
    """
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    blob_container_name = os.getenv("AZURE_BLOB_CONTAINER_NAME")
    sas_credential = os.getenv("AZURE_SAS_CREDENTIAL")

    return account_name, blob_container_name, sas_credential


def write_file_to_azure_blob_storage(local_file_path, blob_name: str = None):
    """
    Upload file to Azure Blob Storage.

    Args:
        - local_file_path: Path of the file to upload.
        - blob_name: Name of the blob to be uploaded.

    Returns:
        True or False depending on the success of the upload.
    """

    account_name, blob_container_name, sas_credential = _get_access_info()

    if _validate_access_info(account_name, blob_container_name, sas_credential):
        try:
            if blob_name is None:
                blob_name = os.path.basename(f"{local_file_path}")  # /sandbox-lwh/
            account_url = f"https://{account_name}.blob.core.windows.net"

            # Upload file
            blob_service_client = BlobServiceClient(
                account_url=account_url, credential=sas_credential
            )
            blob_client = blob_service_client.get_blob_client(
                f"{blob_container_name}", blob_name
            )
            with open(local_file_path, "rb") as local_file:
                blob_client.upload_blob(local_file)

            return True

        except Exception as exc:
            logging.error(
                "Error while uploading file to Azure: %s",str(exc)
                )
            return False

    else:
        logging.error(
            "Please enter valid access information to Azure blob storage in .env file"
        )
        return False


def upload_directory_to_azure_blob_storage(local_directory_path):
    """
    Upload a directory and its contents to Azure Blob Storage.

    Args:
        local_directory_path: The local directory path to upload.
    Returns:
        True or False depending on the success of the upload.
    """

    account_name, blob_container_name, sas_credential = _get_access_info()
    directory_name = os.path.basename(local_directory_path)
    if _validate_access_info(account_name, blob_container_name, sas_credential):
        try:
            # Walk through the directory and its subdirectories
            for root, dirs, files in os.walk(local_directory_path):
                for file in files:
                    local_file_path = os.path.join(root, file)

                    # Remove the local_directory_path prefix to get the relative path
                    relative_path = os.path.relpath(
                        local_file_path, local_directory_path
                    )

                    # Combine with blob container path to get the blob_name
                    blob_name = os.path.join(directory_name, relative_path).replace(
                        os.sep, "/"
                    )

                    # Upload each file to Azure Blob Storage using the write_file_to_azure_blob_storage function
                    write_file_to_azure_blob_storage(local_file_path, blob_name)

            return True
        except Exception as exc:
            logging.error(
                "Error while uploading directory to Azure Blob Storage: %s",str(exc)
            )
            return False

    else:
        logging.error(
            "Please enter valid access information to Azure blob storage in .env file"
        )
        return False


def get_azure_blob_url_path(local_path):
    """
    get the azure blob path of the uploaded element (file or folder)

    Args:
        - local_path: The local path of the uploaded folder/file  on s3

    Returns:
        the azure blob url of the uploaded folder/file
    """
    azure_blob_key = os.path.basename(local_path)
    account_name, blob_container_name, sas_credential = _get_access_info()
    return f"https://{account_name}.blob.core.windows.net/{blob_container_name}/{azure_blob_key}"
