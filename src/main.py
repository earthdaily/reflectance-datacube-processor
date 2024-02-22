import argparse
import os
from typing import List

from api.constants import Bands, CloudMask, CloudStorageRepo, Collections
from dotenv import load_dotenv
from reflectance_datacube_processor.processor import reflectance_datacube_processor
from utils.file_utils import load_input_data


def main(input_path=None):
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

    CLOUD_STORAGE = CloudStorageRepo.AZURE
    COLLECTIONS = [Collections.Landsat.value]
    ASSETS = [
        Bands.BLUE.value,
        Bands.GREEN.value,
        Bands.RED.value,
        Bands.NIR.value,
    ]
    CLOUD_MASK = CloudMask.native.value
    CREATE_METACUBE = "No"
    BANDWIDTH_DISPLAY = "Yes"
    CLEAR_COVERAGE = 0

    processor = reflectance_datacube_processor(
        input_data,
        CLOUD_STORAGE,
        COLLECTIONS,
        ASSETS,
        CLOUD_MASK,
        CREATE_METACUBE,
        BANDWIDTH_DISPLAY,
        CLEAR_COVERAGE,
    )

    result = processor.trigger()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path", type=str, help="Path to the input data", default=None
    )
    args = parser.parse_args()

    main(args.input_path)
