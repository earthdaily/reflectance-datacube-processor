"""outpout schema class"""

from typing import List, Optional

from pydantic import BaseModel


class Metrics(BaseModel):
    """
    Metrics for the output.

    Attributes:
        execution_time (Optional[str]): The execution time.
        data_generation_network_use (Optional[str]): Network use for datacube generation.
        data_upload_network_use (Optional[str]): Network use for datacube upload.
    """

    execution_time: Optional[str] = None
    data_generation_network_use: Optional[str] = None
    data_upload_network_use: Optional[str] = None


class OutputModel(BaseModel):
    """
    Output model containing storage links, and metrics.

    Attributes:
        StorageLinks (List[str]): The link of the output path.
        Metrics (Optional[Metrics]): Metrics for the output.
    """

    storage_links: List[str]
    metrics: Optional[Metrics] = None  # type: ignore
