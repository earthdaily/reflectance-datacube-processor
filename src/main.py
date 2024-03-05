"""reflectance_datacube_processor main"""

import argparse
import os

from dotenv import load_dotenv

from api.constants import CloudStorageRepo
from reflectance_datacube_processor.processor import ReflectanceDatacubeProcessor
from utils.file_utils import find_enum, load_input_data


def main(
    input_path=None,
    cloud_storage=None,
    create_metacube=None,
    bucket_name=None,
    metrics=None,
    token=None,
):
    """
    The main function for processing reflectance datacubes.

    Args:
        input_path: The path to the input data.
        cloud_storage: The cloud storage repository.
        create_metacube: Whether to create a metacube.
        bucket_name: The name of the bucket.
        metrics: Whether to display information regarding bandwidth consumption and duration.
        token: EDS token


    Returns:
        The result of the datacube processing.
    """
    load_dotenv()
    environment = os.getenv("APP_ENVIRONMENT", "local")
    if environment == "local":
        input_data = load_input_data(os.getenv("INPUT_JSON_PATH"))

    elif environment in ["integration", "validation", "production"]:
        if not input_path:
            raise ValueError(
                f"No input path provided in the '{environment}' environment."
            )
        input_data = load_input_data(input_path)
    else:
        raise ValueError(f"Unrecognized environment: {environment}")

    cloud_storage_ok = find_enum(cloud_storage, CloudStorageRepo)

    processor = ReflectanceDatacubeProcessor(
        input_data,
        cloud_storage_ok,
        create_metacube,
        bucket_name,
        metrics,
        token,
    )

    result = processor.trigger()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path", type=str, help="Path to the input data", default=None
    )
    parser.add_argument(
        "--cloud_storage",
        type=str,
        help="AWS_S3/AZURE_BLOB_STORAGE",
        default="AZURE_BLOB_STORAGE",
    )
    parser.add_argument(
        "--create_metacube",
        type=str,
        help="Create matecube in the cloud (Yes/No)",
        default="Yes",
    )
    parser.add_argument(
        "--bucket_name",
        type=str,
        help="Name of the AWS bucket",
        default=None,
    )
    parser.add_argument(
        "--metrics",
        type=str,
        help="Display Bandwidth consumption (Yes/No)",
        default="No",
    )
    parser.add_argument(
        "--eds_token",
        type=str,
        help="EDS bearer token",
        default=None,
    )
    args = parser.parse_args()

    main(
        args.input_path,
        args.cloud_storage,
        args.create_metacube,
        args.bucket_name,
        args.metrics,
        args.eds_token,
    )
