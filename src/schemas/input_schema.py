import datetime as dt
from typing import List

from pydantic import BaseModel


class Parameters(BaseModel):
    """
    A Pydantic model representing the parameters for the input.

    Attributes:
        geometry (str): The geometry.
        startDate (dt.datetime): The start date.
        endDate (dt.datetime): The end date.
        EntityID (str): The entity ID.
        collections (List[str]): The list of collections.
        assets (List[str]): The list of assets.
        cloud_mask (str): The cloud mask.
        clear_coverage (int): The clear coverage.
    """
    geometry: str
    startDate: dt.datetime
    endDate: dt.datetime
    EntityID: str
    collections: List[str]
    assets: List[str]
    cloud_mask: str
    clear_coverage: int


class InputModel(BaseModel):
    """
    A Pydantic model representing the input for the process.

    Attributes:
        parameters (Parameters): The parameters for the process.
    """
    parameters: Parameters
