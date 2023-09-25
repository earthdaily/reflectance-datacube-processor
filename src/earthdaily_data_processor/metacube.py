# -*- coding: utf-8 -*-
import logging
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import box
from rasterio.enums import Resampling
from rasterio.features import geometry_mask
import xarray as xr
import rioxarray as rxr
from pystac import ItemCollection
import json

def _propagade_rio(src, ds):
    coords = ["epsg", "spatial_ref"]
    for coord in coords:
        if coord in src:
            ds = ds.assign_coords(coord=src[coord])
    return ds


def _drop_unfrozen_coords(ds):
    unfrozen_coords = [i for i in list(ds.coords) if i not in ds.dims]
    ds = ds.drop(unfrozen_coords)
    return ds


def _common_data_vars(cubes):
    data_vars = list(set([k for cube in cubes for k in list(cube.data_vars.keys())]))
    return data_vars


def _groupby(ds, by="time.date", how="mean"):
    condition = getattr(ds, by).size != np.unique(getattr(ds, by)).size
    if condition:
        ds = ds.groupby(by)
        ds = getattr(ds, how)()
        if by == "time.date":
            ds = ds.rename(dict(date="time"))
            ds["time"] = ds.time.astype("<M8[ns]")
    return ds


def _have_same_xy(cubes):
    print(type(cubes))
    print(cubes)
    print(cubes[0])
    x_size = list(set(np.array([cube.coords["x"].data.tolist() for cube in cubes]).flatten().tolist()))
    y_size = list(set(np.array([cube.coords["y"].data.tolist() for cube in cubes]).flatten().tolist()))
    return len(x_size) == 1 and len(y_size) == 1


def supercube(cubes, concat_dim="time", by="time.date", how="mean"):
    """
    Given n cubes, will build a new cube in an optimal way.
    metacube will manage different size of data variables (i.e. bands).

    Parameters
    ----------
    *cubes : list of datasets.
        xarray datasets with same x/y dimensions.
    concat_dim : str, optional
        The dim to concat arrays. The default is "time".
    by : str, optional
        . The default is "time.date".
    how : str, optional
        Any aggregation method available from xarray. See https://docs.xarray.dev/en/stable/generated/xarray.core.groupby.DataArrayGroupBy.html#xarray.core.groupby.DataArrayGroupBy`
        The default is "mean".


    Returns
    -------
    xr.dataset
        The cube from cubes.

    """
    lst_datacube_array = [cube.to_array()[0] for cube in cubes] 
    cube = xr.concat([_drop_unfrozen_coords(cube) for cube in lst_datacube_array], dim=concat_dim)
    cube = _groupby(cube, by=by, how=how)
    return _propagade_rio(cubes[0], cube)