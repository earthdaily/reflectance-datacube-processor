import argparse
import os
from enum import Enum
from typing import List

from dotenv import load_dotenv

from api.constants import CloudStorageRepo
from reflectance_datacube_processor.processor import reflectance_datacube_processor
from utils.file_utils import find_enum, load_input_data


def main(
    input_path=None, cloud_storage=None, create_metacube=None, bandwidth_display=None
):
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

    print(input_data, cloud_storage_ok, create_metacube, bandwidth_display)

    processor = reflectance_datacube_processor(
        input_data,
        cloud_storage_ok,
        create_metacube,
        bandwidth_display,
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
        "--bandwidth_display",
        type=str,
        help="Display Bandwidth consumption (Yes/No)",
        default="Yes",
    )
    args = parser.parse_args()

    main(
        args.input_path,
        args.cloud_storage,
        args.create_metacube,
        args.bandwidth_display,
    )
