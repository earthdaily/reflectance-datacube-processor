import os
import logging
import time
from typing import List

import geopandas as gpd
import numpy as np
import psutil
import xarray as xr
from earthdaily import earthdatastore
from fastapi import HTTPException
from xarray import Dataset

from utils.file_utils import validate_data
from utils.utils import (
    dataset_to_zarr_format_indep_sensor,
    dataset_to_zarr_format_sensor,
    upload_cube,
)


class reflectance_datacube_processor:
    """
    A class for processing reflectance datacubes.

    Args:
        input_data: The input data for processing.
        cloud_storage: The cloud storage repository.
        create_metacube: Whether to create a metacube.
        bandwidth_display: Whether to display information regarding bandwidth consumption.

    Methods:
        prepare_data: Prepare the data for processing.
        predict: Perform the prediction based on the input data.
        trigger: Trigger the datacube processing.
        generate_datacube_optic: Generate a datacube with indicator values for each pixel and date.
        get_sentinel: Retrieve a Sentinel datacube.
        get_landsat: Retrieve a Landsat datacube.
        get_ed_simulated: Retrieve a cloudless EarthDaily simulated datacube.
        get_venus: Retrieve a Venus datacube.
        create_metacube: Merge different sensors datacubes into one datacube.

    Returns:
        The result of the datacube processing.

    Raises:
        HTTPException: If there is an error while generating the datacube.
    """

    def __init__(
        self,
        input_data,
        cloud_storage,
        create_metacube,
        bucket_name,
        bandwidth_display,
        token: str = None,
    ):
        validate_data(input_data, "input")
        self.input_data = input_data
        self.cloud_storage = cloud_storage
        self.creation_metacube = create_metacube
        self.bucket_name = bucket_name
        self.bandwidth_display = bandwidth_display
        if token:
            self.__client_eds = earthdatastore.Auth((token, os.getenv("EDS_API_URL")))
        else:
            self.__client_eds = earthdatastore.Auth()
        self.sensors = [
            "sentinel-2-l2a",
            "landsat-c2l2",
            "venus-l2a",
            "earthdaily-simulated-cloudless-l2a-cog-edagro",
        ]

    def prepare_data(self):
        print("data_prepared")

    def predict(
        self,
        input_data,
    ):
        print("Output predicted")
        start_time = time.time()
        links = []
        start_date = input_data["parameters"]["startDate"]
        end_date = input_data["parameters"]["endDate"]

        # generate analytics datacube
        datacubes, collections_done = self.generate_datacube_optic(
            polygon=input_data["parameters"]["geometry"],
            start_date=start_date,
            end_date=end_date,
            collections=input_data["parameters"]["collections"],
            assets=input_data["parameters"]["assets"],
            cloud_mask=input_data["parameters"]["cloud_mask"],
            clear_percent=input_data["parameters"]["clear_coverage"],
        )

        # bandwidth use retrieval
        bandwidth_generation = (
            psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        )

        print("bandwidth")
        logging.info(self.bandwidth_display)

        if len(datacubes) <= 0:
            return "No item were found."
        if self.creation_metacube == "Yes":
            cube = self.create_metacube(*datacubes)
            zarr_path = dataset_to_zarr_format_indep_sensor(
                cube,
                input_data["parameters"]["EntityID"],
                input_data["parameters"]["startDate"],
                input_data["parameters"]["endDate"],
            )
            try:
                links.append(
                    upload_cube(
                        zarr_path, self.cloud_storage, bucket_name=self.bucket_name
                    )
                )
            except Exception as exc:
                logging.error(
                    "Error while uploading folder to  %s: %s",
                    str(self.cloud_storage),
                    str(exc),
                )
        else:
            for i, datacube in enumerate(datacubes):
                # convert the generated datacube in zarr file
                zarr_path = dataset_to_zarr_format_sensor(
                    datacube,
                    input_data["parameters"]["EntityID"],
                    input_data["parameters"]["startDate"],
                    input_data["parameters"]["endDate"],
                    collections_done[i],
                )
                try:
                    links.append(
                        upload_cube(
                            zarr_path, self.cloud_storage, bucket_name=self.bucket_name
                        )
                    )
                except Exception as exc:
                    logging.error(
                        "Error while uploading folder to %s: %s",
                        str(self.cloud_storage),
                        str(exc),
                    )
                    raise HTTPException(
                        status_code=500,
                        detail=f"Error while uploading folder to {self.cloud_storage} : {exc}",
                    ) from exc
        # bandwidth use retrieval
        bandwidth_upload = (
            psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        )

        return (
            {
                "Storage_links": links,
                "Execution time": (
                    f"--- {int(np.round((time.time() - start_time)/60))} minutes {int(np.round(np.round((time.time() - start_time))%60))} seconds ---"
                ),
                "Datacube generation network use": (
                    f"--- {np.round((bandwidth_generation)/1024./1024./1024.*8,3)} Gb ---"
                ),
                "Datacube upload network use": (
                    f"--- {np.round((bandwidth_upload-bandwidth_generation)/1024./1024./1024.*8,3)} Gb ---"
                ),
            }
            if self.bandwidth_display == "Yes"
            else {
                "Storage_links": links,
                "Execution time": (
                    f"--- {int(np.round((time.time() - start_time)/60))} minutes {int(np.round(np.round((time.time() - start_time))%60))} seconds ---"
                ),
            }
        )

    def trigger(self):
        print("Processor triggered")
        self.prepare_data()
        result = self.predict(self.input_data)
        # output_data = {
        #     "Metadata": {
        #         "processId": "123",
        #         "processName": "SeasonAnalysis",
        #         "outputFormat": "zarr",
        #     },
        #     "ProcessOutput": {
        #         "status": result,
        #         "outputPath": "http://geosysp3.blob.core.windows.net/example_analytic_datacube.zarr",
        #         "error": "",
        #     },
        # }
        output_data = {"data": result}
        # validate_data(output_data, 'output')
        print("Processor output:", output_data)
        return result

    def generate_datacube_optic(
        self,
        polygon,
        start_date: str,
        end_date: str,
        collections: List[str],
        assets: List[str],
        cloud_mask: str,
        clear_percent: int = 80,
    ):
        """
        Get a xarray.Dataset with indicators values for each pixel and for each date of images found between start and end dates.
        Args:
            - polygon: WKT
            - start_date: beginning of the period
            - end_date: end of the period
            - collections : sensor to use : "sentinel-2-l2a",landsat-c2l2-sr, venus-l2a
            - assets : list of band to get, among : ["red", "green", "blue",  "nir", "swir16", "swir22","lst]
            - cloud_mask : cloud mask to use : "native" or "ag_cloud_mask"
            - clear_percent : clear coverage percentage to select the image takes : int between 0 and 100.
        Returns:
            xarray.Dataset
        """
        # Initiate an empty list for the datasets of each collections selected
        sensors_datasets = []
        sensor_done = []
        # specific assets by collections management
        if "lst" in assets:  # thermal band from Landsat
            lst = True
            assets.remove("lst")
        else:
            lst = False
        if "nir09" in assets:  # band B08A from S2
            nir09 = True
            assets.remove("nir09")
        else:
            nir09 = False
        if "Sentinel-2 L2A" not in collections:
            base_dataset = self.get_sentinel(
                polygon=polygon,
                assets=assets,
                cloud_mask="native",
                dates=[start_date, end_date],
                clear_percent=clear_percent,
            )

        # datacube creation for each collections wanted
        for sens in collections:
            try:
                logging.info(
                    "EarthDailyData:generate_datacube_optic: Get dataset for %s", sens
                )
                if sens == "Sentinel-2 L2A":
                    if nir09:
                        assets.append("nir09")
                    datacube = self.get_sentinel(
                        polygon=polygon,
                        assets=assets,
                        cloud_mask=cloud_mask,
                        dates=[start_date, end_date],
                        clear_percent=clear_percent,
                    )
                    sensors_datasets.append(datacube.copy())
                    base_dataset = datacube.copy()
                    sensor_done.append(self.sensors[0])

                elif sens == "Landsat C2L2":
                    sensors_datasets.append(
                        self.get_landsat(
                            polygon=polygon,
                            assets=assets,
                            cloud_mask=cloud_mask,
                            dates=[start_date, end_date],
                            base_dataset=base_dataset,
                            clear_percent=clear_percent,
                            lst_band=lst,
                        )
                    )
                    sensor_done.append(self.sensors[1])

                elif sens == "Venus L2A":
                    sensors_datasets.append(
                        self.get_venus(
                            polygon=polygon,
                            assets=assets,
                            cloud_mask=cloud_mask,
                            dates=[start_date, end_date],
                            base_dataset=base_dataset,
                            clear_percent=clear_percent,
                        )
                    )
                    sensor_done.append(self.sensors[2])

                elif sens == "EarthDaily Simulated L2A":
                    sensors_datasets.append(
                        self.get_ed_simulated(
                            polygon=polygon,
                            assets=assets,
                            dates=[start_date, end_date],
                            base_dataset=base_dataset,
                        )
                    )
                    sensor_done.append(self.sensors[3])

                else:
                    print(f"Sensor {sens} not supported yet")

            except Exception as exc:
                logging.error(
                    "Error while generating dataset for %s indicator: %s",
                    sens,
                    str(exc),
                )
        return sensors_datasets, sensor_done

    def get_sentinel(
        self,
        polygon: gpd.GeoDataFrame,
        assets: List[str],
        cloud_mask: str,
        dates: List[str],
        clear_percent: int,
    ) -> Dataset:
        """
        Function to retrieve a landsat datacube.
        Parameters:
            - polygon : GeoDataFrame, polygon to extract the data for.
            - assets : [str], assets to extract.
            - cloud_mask : str, cloud mask to use, either 'native' or 'ag_cloud_mask'.
            - dates : [str], dates to extract the data for.
            - clear_percent: int, cloud free percentage wanted.

        Returns:
        xarray.Dataset
        """
        return self.__client_eds.datacube(
            "sentinel-2-l2a",
            intersects=polygon,
            datetime=dates,
            assets=assets,
            rescale=True,
            mask_with=cloud_mask,
            clear_cover=clear_percent,
            prefer_alternate="download",
        )

    def get_landsat(
        self,
        polygon: gpd.GeoDataFrame,
        assets: List[str],
        cloud_mask: str,
        dates: List[str],
        base_dataset: Dataset,
        clear_percent: int,
        lst_band: bool,
    ) -> Dataset:
        """
        Function to retrieve a landsat datacube.
        Parameters:
            - polygon : GeoDataFrame, polygon to extract the data for.
            - assets : [str], assets to extract.
            - cloud_mask : str, cloud mask to use, either 'native' or 'ag_cloud_mask'.
            - dates : [str], dates to extract the data for.
            - base_dataset: xarray.Dataset, first dataset computed to scale the datacube with.
            - clear_percent: int, cloud free percentage wanted.

        Returns:
        xarray.Dataset
        """
        # deal with rededge bands for landsat
        band_adjusted = list(
            filter(
                lambda asset: asset not in ["rededge1", "rededge2", "rededge3"], assets
            )
        )

        # get datacube
        data_cube = self.__client_eds.datacube(
            "landsat-c2l2-sr",
            intersects=polygon,
            datetime=dates,
            assets=band_adjusted,
            mask_with=cloud_mask,
            clear_cover=clear_percent,
            resolution=base_dataset.rio.resolution()[0],
            epsg=base_dataset.rio.crs.to_epsg(),
        )
        if lst_band:
            data_cube_lst = self.__client_eds.datacube(
                "landsat-c2l2-st",
                intersects=polygon,
                datetime=dates,
                assets=["lwir11"],
                mask_with=cloud_mask,
                clear_cover=clear_percent,
                search_kwargs=dict(
                    query={"platform": {"in_": ["LANDSAT_8", "LANDSAT_9"]}}
                ),
                resolution=base_dataset.rio.resolution()[0],
                epsg=base_dataset.rio.crs.to_epsg(),
            )
            return xr.merge([data_cube, data_cube_lst], compat="no_conflicts")
        return data_cube

    def get_ed_simulated(
        self,
        polygon: gpd.GeoDataFrame,
        assets: List[str],
        dates: List[str],
        base_dataset: Dataset,
    ) -> Dataset:
        """
        Function to retrieve a cloudless EarthDaily simulated datacube.
        Parameters:
            - polygon : GeoDataFrame, polygon to extract the data for.
            - assets : [str], assets to extract.
            - dates : [str], dates to extract the data for.
            - base_dataset: xarray.Dataset, first dataset computed to scale the datacube with.

        Returns:
        xarray.Dataset
        """

        if "swir22" in assets:
            assets.remove("swir22")

        simulated_assets = dict(
            blue="blue",
            green="green",
            red="red",
            rededge1="image_file_RE1",
            rededge2="image_file_RE2",
            rededge3="image_file_RE3",
            nir="image_file_NIR",
            swir16="swir16",
        )
        dict_simulated_assets = {simulated_assets[band]: band for band in assets}
        return self.__client_eds.datacube(
            "earthdaily-simulated-cloudless-l2a-cog-edagro",
            intersects=polygon,
            datetime=dates,
            assets=dict_simulated_assets,
            resolution=base_dataset.rio.resolution()[0],
            epsg=base_dataset.rio.crs.to_epsg(),
            prefer_alternate="download",
        )

    def get_venus(
        self,
        polygon: gpd.GeoDataFrame,
        assets: List[str],
        cloud_mask: str,
        dates: List[str],
        base_dataset: Dataset,
        clear_percent: int,
    ) -> Dataset:
        """
        Function to retrieve a Venus datacube.
        Parameters:
            - polygon : GeoDataFrame, polygon to extract the data for.
            - assets : [str], assets to extract.
            - cloud_mask : str, cloud mask to use, either 'native' or 'ag_cloud_mask'.
            - dates : [str], dates to extract the data for.
            - base_dataset: xarray.Dataset, first dataset computed to scale the datacube with.
            - clear_percent: int, cloud free percentage wanted.

        Returns:
        xarray.Dataset
        """
        venus_assets = dict(
            blue="image_file_SRE_B3",
            green="image_file_SRE_B4",
            red="image_file_SRE_B7",
            rededge1="image_file_FRE_B8",
            rededge2="image_file_FRE_B9",
            rededge3="image_file_FRE_B10",
        )

        dict_venus_assets = {venus_assets[band]: band for band in assets}
        return self.__client_eds.datacube(
            "venus-l2a",
            intersects=polygon,
            datetime=dates,
            assets=dict_venus_assets,
            mask_with=cloud_mask,
            clear_cover=clear_percent,
            resolution=base_dataset.rio.resolution()[0],
            epsg=base_dataset.rio.crs.to_epsg(),
            prefer_alternate="download",
        )

    def create_metacube(
        self,
        *list_datacube: Dataset,
    ):
        """
        Function to merge different sensors datacubes into one datacube.
        Parameters:
            - list_datacube : list of xarray.Dataset from all sensors.
        Returns:
        xarray.Dataset
        """
        return earthdatastore.metacube(
            *list_datacube, concat_dim="time", by="time.date", how="mean"
        )
