import os
from geosyspy import Geosys
from geosyspy.utils.constants import *
from dotenv import load_dotenv
from datetime import datetime
from analytics_datacube.processor import AnalyticsDatacube
import logging
import matplotlib.pyplot as plt
from cloud_storage import cloud_storage_aws,cloud_storage_azure

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# read .env file
load_dotenv()

API_CLIENT_ID = os.getenv('API_CLIENT_ID')
API_CLIENT_SECRET = os.getenv('API_CLIENT_SECRET')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')

client = AnalyticsDatacube(API_CLIENT_ID, API_CLIENT_SECRET, API_USERNAME, API_PASSWORD, Env.PROD, Region.NA)

print(client.test())

polygon = "POLYGON((-90.41 41.6663, -90.41 41.6545, -90.3775 41.6541, -90.3778 41.6660, -90.41 41.6663))"
startDate = datetime.strptime("2023-06-01", "%Y-%m-%d")
endDate = datetime.strptime("2023-07-01", "%Y-%m-%d")

# Get analytics datacube
indicators = ["NDVI", "NDWI", "EVI"]
analytics_datacube = client.get_analytics_datacube(polygon, startDate, endDate, indicators)

# Save to csv as dataframe
#df = analytics_datacube.to_dataframe()
#df.to_csv('analytics_datacube.csv')

# Save as zarr
zarr_path = client.dataset_to_zarr_format(analytics_datacube)
print(zarr_path)

# Upload to AWS and Azure
# if cloud_storage_aws.write_folder_to_aws_s3(zarr_path):
#     print("Zarr uploaded to AWS")
if cloud_storage_azure.write_folder_to_azure_blob_storage(zarr_path):
   print("Zarr uploaded to Azure")

