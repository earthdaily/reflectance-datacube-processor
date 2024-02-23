import logging
import os

import boto3


def _get_s3_client():
    access_key: str = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    if (
        access_key is not None
        and secret_key is not None
        and access_key
        and secret_key
    ):
        return boto3.client(
            "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key
        )
    logging.error("Please enter valid access information to AWS S3 in .env file")
    return None


def write_file_to_aws_s3(local_file_path, bucket_name=None):
    """
    Upload a file to AWS S3 Bucket.

    Args:
        - local_file_path: The local file path to upload.
        - bucket_name: The name of the AWS S3 bucket.


    Returns:
        True or False depending on the success of the upload.
    """

    # get bucket name
    if bucket_name is None:
        bucket_name = os.getenv("AWS_BUCKET_NAME")

    s3_client = _get_s3_client()
    if s3_client and bucket_name is not None:
        try:
            file_name = os.path.basename(local_file_path)
            s3_client.upload_file(local_file_path, bucket_name, file_name)
            return True
        except Exception as exc:
            logging.error(
                "Error while uploading file to AWS S3: %s", str(exc)
                )
            return False
    else:
        return False


def upload_folder_to_aws_s3(local_folder_path, bucket_name=None):
    """
    Upload a folder to AWS S3 Bucket.

    Args:
        - local_folder_path: The local folder path to upload.
        - bucket_name: The name of the AWS S3 bucket.

    Returns:
        True or False depending on the success of the upload.
    """

    # get bucket name
    if bucket_name is None:
        bucket_name = os.getenv("AWS_BUCKET_NAME")

    if not (s3_client := _get_s3_client()):
        return False
    try:
        for root, dirs, files in os.walk(local_folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_folder_path)
                s3_key = os.path.join(
                    os.path.basename(local_folder_path), relative_path
                ).replace(os.sep, "/")
                s3_client.upload_file(local_file_path, bucket_name, s3_key)
        return True
    except Exception as exc:
        logging.error(
            "Error while uploading folder to AWS S3: %s", str(exc)
            )
        return False


def get_s3_uri_path(local_path):
    """
    get the s3 path of the uploaded element (file or folder)

    Args:
        - local_path: The local path of the uploaded folder/file  on s3

    Returns:
        the s3 uri of the uploaded folder/file
    """
    s3_key = os.path.basename(local_path)
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    
    return f"s3://{bucket_name}/{s3_key}"
