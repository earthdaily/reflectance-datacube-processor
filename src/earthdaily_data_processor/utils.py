import logging
import xarray
from datetime import datetime
import tempfile
import os
import datetime as dt
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def dataset_to_zarr_format_indep_sensor(dataset: xarray.Dataset,fieldID:str,start_date: dt.date,end_date: dt.date):
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

def dataset_to_zarr_format_sensor(dataset: xarray.Dataset,fieldID:str,start_date: dt.date,end_date: dt.date,sensor: str):
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
