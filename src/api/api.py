"""Fast api to trigger the reflectance datacube processor.
Result can be stored on AWS S3 or Azure Blob storage 
"""

import datetime as dt
import os
from typing import List

import requests
from byoa.telemetry.log_manager import log_manager
from dotenv import load_dotenv
from fastapi import FastAPI, Form, HTTPException, Query
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from pydantic import BaseModel, Field, SecretStr

from api.constants import Bands, CloudMask, CloudStorageRepo, Collections, Question
from reflectance_datacube_processor.processor import ReflectanceDatacubeProcessor
from schemas.input_schema import InputModel, Parameters

# pylint: disable=missing-docstring

logger_manager = log_manager.LogManager.get_instance()

app = FastAPI(docs_url=None, title="reflectance-datacube-processor" + " API", description="")
handler = Mangum(app)


load_dotenv()

# identity server configuration
tokenUrl = os.getenv("EDS_AUTH_URL")
app.mount("/static", StaticFiles(directory="./api/files"), name="static")


@app.get("/")
async def hello():
    return {"message": "test API reflectance"}


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="reflectance-datacube-processor" + " API",
        swagger_favicon_url="/static/favicon.svg",
    )


def authenticate_client(client_id: str, client_secret: str):
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    response = requests.post(tokenUrl, data=data, timeout=60)
    if response.status_code == 200:
        return response.json()["access_token"]
    raise HTTPException(
        status_code=response.status_code,
        detail="Failed to authenticate client",
        headers=response.headers,
    )


def generate_access_token(client_id: str, client_secret: str):
    return authenticate_client(client_id, client_secret)


def login_for_access_token(client_id: str = Form(...), client_secret: SecretStr = Form(...)):

    return generate_access_token(client_id, client_secret.get_secret_value())


class Item(BaseModel):
    geometry: str = Field(
        ...,
        examples=["POLYGON ((1.26 43.427, 1.263 43.428, 1.263 43.426, 1.26 43.426, 1.26 43.427))"],
    )
    startDate: dt.date = Field(..., examples=["2019-05-01"])
    endDate: dt.date = Field(..., examples=["2019-05-31"])
    EntityID: str = Field(..., examples=["entity_1"])


@app.post("/reflectance-datacube-processor", tags=["Datacube Computation"])
async def create_analytics_datacube(
    item: Item,
    eds_client_id: str = Query(...),
    eds_client_secret: SecretStr = Query(...),
    cloud_storage: CloudStorageRepo = Query(alias="Cloud Storage"),
    aws_s3_bucket: str = Query(
        default=None,
        alias="AWS S3 bucket name",
    ),
    collections: List[Collections] = Query(alias="Collections"),
    assets: List[Bands] = Query(alias="Assets"),
    cloud_mask: CloudMask = Query(alias="Cloud Mask"),
    create_metacube: Question = Query(alias="Create Metacube"),
    metrics: Question = Query(
        alias="Display metrics information (bandwidth consumption, duration)"
    ),
    clear_coverage: int = Query(
        default=0,
        alias="Clear Coverage (%)",
        allow_inf_nan=False,
        examples=[0, 10, 50, 80, 90, 100],
    ),
):
    token = login_for_access_token(eds_client_id, eds_client_secret)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid access token")

    start_date = dt.datetime(item.startDate.year, item.startDate.month, item.startDate.day)

    end_date = dt.datetime(item.endDate.year, item.endDate.month, item.endDate.day)
    parameters = Parameters(
        geometry=item.geometry,
        startDate=start_date,
        endDate=end_date,
        EntityID=item.EntityID,
        collections=collections,
        assets=assets,
        cloud_mask=cloud_mask,
        clear_coverage=clear_coverage,
    )
    input_data = InputModel(parameters=parameters)

    display_metrics = False
    if metrics == Question.YES:
        display_metrics = True

    client = ReflectanceDatacubeProcessor(
        input_data=input_data.model_dump(),
        cloud_storage=cloud_storage,
        create_metacube=create_metacube.value,
        bucket_name=aws_s3_bucket,
        metrics=display_metrics,
        token=token,
    )

    # generate analytics datacube
    analytics_datacube = client.trigger()

    if not analytics_datacube:
        logger_manager.error("Error while generating datacube")
        raise HTTPException(status_code=500)

    return analytics_datacube
