import datetime as dt
import json
import os
from typing import List

from byoa.telemetry.log_manager import log_manager
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from api.constants import Bands, CloudMask, CloudStorageRepo, Collections, Question
from reflectance_datacube_processor.processor import reflectance_datacube_processor
from schemas.input_schema import InputModel, Parameters

logger_manager = log_manager.LogManager.get_instance()

app = FastAPI(
    docs_url=None, title="reflectance-datacube-processor" + " API", description=""
)

load_dotenv()

app.mount("/static", StaticFiles(directory="./api/files"), name="static")


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="reflectance-datacube-processor" + " API",
        swagger_favicon_url="/static/favicon.svg",
    )


@app.post("/reflectance-datacube-processor", tags=["Datacube Computation"])
async def create_analytics_datacube(
    parameters: Parameters,
    cloud_storage: CloudStorageRepo = Query(alias="Cloud Storage"),
    # collections: List[Collections] = Query(alias="Collections"),
    # assets: List[Bands] = Query(alias="Assets"),
    # cloud_mask: CloudMask = Query(alias="Cloud Mask"),
    create_metacube: Question = Query(alias="Create Metacube"),
    # aws_azure_id: str = Query(alias="AWS Access Key ID/Azure Account Name"),
    # aws_azure_secret: str = Query(alias="AWS Secret Access Key/Azure SAS Credential"),
    # aws_bucket_azure_blob: str = Query(
    #     alias="AWS Bucket Name/Azure Blob Container Name"
    # ),
    bandwidth_display: Question = Query(
        alias="Display information regarding bandwith consumption"
    ),
    # clear_coverage: int = Query(
    #     default=0,
    #     alias="Clear Coverage (%)",
    #     allow_inf_nan=False,
    #     examples=[0, 10, 50, 80, 90, 100],
    # ),
):

    input_data = InputModel(parameters=parameters)

    client = reflectance_datacube_processor(
        input_data.model_dump(),
        cloud_storage,
        create_metacube,
        bandwidth_display,
    )

    # generate analytics datacube
    analytics_datacube = client.trigger()

    if not analytics_datacube:
        logger_manager.error(f"Error while generating datacube")
        raise HTTPException(status_code=500)
