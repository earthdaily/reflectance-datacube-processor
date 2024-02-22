import datetime as dt
from typing import List

from pydantic import BaseModel


class Parameters(BaseModel):
    geometry: str
    startDate: dt.date
    endDate: dt.date
    EntityID: str


class InputModel(BaseModel):
    parameters: Parameters
