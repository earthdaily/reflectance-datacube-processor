import datetime as dt
from typing import List

from pydantic import BaseModel


class Parameters(BaseModel):
    geometry: str
    startDate: dt.date
    endDate: dt.date
    EntityID: str
    collections: List[str]
    assets: List[str]
    cloud_mask: str
    clear_coverage: int


class InputModel(BaseModel):
    parameters: Parameters
