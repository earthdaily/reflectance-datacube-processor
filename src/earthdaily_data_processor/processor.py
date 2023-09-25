# -*- coding: utf-8 -*-
"""
Created on Sep 12

@author: lwh
"""
#%%
import logging
import os
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from geosyspy import Geosys
from geosyspy.utils.constants import *

import requests
import geopandas as gpd

import xarray as xr
from xarray import DataArray, Dataset
from earthdaily import earthdatastore
import shapely
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#%%
class EarthDailyData:

    def __init__(self):
        
        load_dotenv()
        self.__client_eds = earthdatastore.Auth()
        
    def generate_datacube_optic(self,
                                polygon,
                                start_date: str,
                                end_date: str,
                                collections: [str],
                                assets: [str],
                                cloud_mask: str):
        """
            Get a xarray.Dataset with indicators values for each pixel and for each date of images found between start and end dates.

            Args:
                - polygon: WKT
                - start_date: beginning of the period
                - end_date: end of the period
                - collections : sensor to use : "sentinel-2-l2a",landsat-c2l2-sr
                - assets : list of band to get, among : ["red", "green", "blue",  "nir08", "swir16", "swir22"]
                - cloud_mask : cloud mask to use : "scl" or 
            Returns:
                xarray.Dataset
        """
        # Build a list with datasets of each indicator
        sensors_datasets = []
        pol = shapely.wkt.loads(polygon)
        dataframe_pol = gpd.GeoDataFrame([[1,pol]],columns=['id','geometry'])
        dataframe_pol.set_geometry('geometry',inplace=True)
        dataframe_pol.set_crs('epsg:4326',inplace=True)
        sensor_done = []
        if 'lst' in assets and "landsat-c2l2-sr" in collections:
            lst=True
            assets.remove('lst')
        else:
            lst=False
            
        for sens in collections:
            try:
                logging.info(f"EarthDailyData:generate_datacube_optic: Get dataset for {sens}")
                if sens =="sentinel-2-l2a":
                    data_cube = self.__client_eds.datacube(
                        sens,
                        intersects=dataframe_pol,
                        datetime=[start_date, end_date],
                        assets=assets,
                        rescale=True,
                        mask_with=cloud_mask,  
                        mask_statistics=True
                    ) 
                    if cloud_mask == 'native':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_scl > 80])
                    elif cloud_mask =='ag_cloud_mask':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_ag_cloud_mask > 80])
                    sensors_datasets.append(data_cube) 
                             
                elif  sens =="landsat-c2l2-sr":
                    #deal with rededge bands for landsat
                    band_adjusted = assets.copy()
                    if 'rededge1' in assets:
                        band_adjusted.remove('rededge1')
                    if 'rededge2' in assets:
                        band_adjusted.remove('rededge2')
                    if 'rededge3' in assets:
                        band_adjusted.remove('rededge3')
                        
                    #get datacube
                    data_cube = self.__client_eds.datacube(
                        sens,
                        intersects=dataframe_pol,
                        datetime=[start_date, end_date],
                        assets=band_adjusted,
                        mask_with=cloud_mask,  
                        mask_statistics=True,
                        resolution=sensors_datasets[0].rio.resolution()[0],
                        epsg=sensors_datasets[0].rio.crs.to_epsg()
                    ) 
                    if cloud_mask == 'native':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_qa_pixel > 80])
                    elif cloud_mask =='ag_cloud_mask':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_ag_cloud_mask > 80])
                    sensors_datasets.append(data_cube) 
                    sensors_datasets.append(data_cube)
                    
                elif sens=='venus-l2a':
                    lst_venus_assets = self.get_venus_asset(assets)
                    data_cube = self.__client_eds.datacube(
                        sens,
                        intersects=dataframe_pol,
                        datetime=[start_date, end_date],
                        assets=lst_venus_assets,
                        mask_with=cloud_mask,  
                        mask_statistics=True,
                        resolution=sensors_datasets[0].rio.resolution()[0],
                        epsg=sensors_datasets[0].rio.crs.to_epsg()
                    ) 
                    if cloud_mask == 'native':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_detailed_cloud_mask > 80])
                    elif cloud_mask =='ag_cloud_mask':
                        data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_ag_cloud_mask > 80])
                    sensors_datasets.append(data_cube)
                else:
                    print(f'Sensor {sens} not supported yet')    
                sensor_done.append(sens)                                                       
            except Exception as exc:
                logging.error(f"Error while generating dataset for {sens} indicator: {str(exc)}")
        if lst :
            #not ok for now : band lwir11 not accessible 
            try:
                data_cube = self.__client_eds.datacube(
                    'landsat-c2l2-st',
                    intersects=dataframe_pol,
                    datetime=[start_date, end_date],
                    assets=['lwir11'],
                    mask_with=cloud_mask,  
                    mask_statistics=True,
                    search_kwargs=dict(query={"platform": {"in_": ["LANDSAT_8", "LANDSAT_9"]}}),
                    resolution=sensors_datasets[0].rio.resolution()[0],
                    epsg=sensors_datasets[0].rio.crs.to_epsg()
                ) 
                if cloud_mask == 'native':
                    data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_qa_pixel > 80])
                elif cloud_mask =='ag_cloud_mask':
                    data_cube = data_cube.sel(time=data_cube.time[data_cube.clear_percent_ag_cloud_mask > 80])
                data_cube_landsat_st = sensors_datasets[1]
                data_cube_landsat_all = xr.concat([data_cube_landsat_st,data_cube], dim="band")
                sensors_datasets.remove(data_cube_landsat_st)
                sensors_datasets.insert(1,data_cube_landsat_all)
            except Exception as exc:
                logging.error(f"Error while generating dataset for LST indicator: {str(exc)}")
        
        return sensors_datasets, sensor_done

    def get_venus_asset(self, bands):
        venus_assets = dict(
            blue='image_file_SRE_B3',
            green="image_file_SRE_B4",
            red="image_file_SRE_B7",
            rededge1='image_file_FRE_B8',
            rededge2='image_file_FRE_B9',
            rededge3='image_file_FRE_B10'
        )
        venus_assets_reversed = dict(
            image_file_SRE_B3="blue",
            image_file_SRE_B4="green",
            image_file_SRE_B7="red",
            image_file_SRE_B8="rededge1",
            image_file_FRE_B9='rededge2',
            image_file_FRE_B10='rededge3',
            )
        
        
        lst_venus_assets = []
        for band in bands:
            try:
                lst_venus_assets.append(venus_assets[f'{band}'])
            except:
                pass
        dict_venus_assets = {i:venus_assets_reversed[f'{i}'] for i in lst_venus_assets}
        return(dict_venus_assets)
    
    def get_assets(self):
        cols_optic = [ 'sentinel-2-l2a','landsat-c2l2-sr','venus-l2a','earthdaily-simulated-cloudless-l2a-cog-edagro']
        collections  = [i.id for i in list(self.__client_skyfox.client.get_all_collections())]
        for collection in collections:
            if collection in cols_optic:
                try:      
                    assets = self.__client_skyfox.explore(collection).assets()
                    assets_common_name = []
                    for asset in assets:
                        common_name = self.__client_skyfox.explore(collection).assets(asset).get('eo:bands',[{}])[0].get('common_name','')
                        assets_common_name.append(common_name)
                    return(dict(zip(assets,assets_common_name)))
                except:
                    pass
    def cross_calibration_collections(self,
                       *list_datacube: Dataset,
                       ):
        
        final_cube = stackfox.metacube(*list_datacube, concat_dim="time", by="time.date", how="mean")
        return(final_cube)
                  
# #%%
# initalize = StackfoxDatacube(Env.PROD)
# polygon = "POLYGON ((1.26 43.427, 1.263 43.428, 1.263 43.426, 1.26 43.426, 1.26 43.427))"
# data,sensors = initalize.generate_datacube_optic(
#                                     polygon,
#                                     start_date = "2019-05-01",
#                                     end_date = "2019-05-31",
#                                     sensor = ["sentinel-2-l2a","landsat-c2l2-sr",'venus-l2a'],
#                                     bands= ["red", "green"],
#                                     cloud_mask= "native")
# #%%
# print(len(data))

# # %%
# cube = initalize.merge_datacube(data)


# # %%
# print(cube)
# # %%
