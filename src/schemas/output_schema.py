from typing import Optional
from pydantic import BaseModel, HttpUrl


class Metadata(BaseModel):
    """
    A Pydantic model representing the metadata of the output.

    Attributes:
        processId (str): The ID of the process.
        processName (str): The name of the process.
        outputFormat (str): The format of the output.
    """
    processId: str
    processName: str
    outputFormat: str

class ProcessOutput(BaseModel):
    """
    A Pydantic model representing the process output information.

    Attributes:
        status (str): The status of the process.
        outputPath (Optional[HttpUrl]): The output path, if available.
        error (Optional[str]): The error message, if any.
    """
    status: str
    outputPath: Optional[HttpUrl]
    error: Optional[str]

class OutputModel(BaseModel):
    """
    A Pydantic model representing the output of the process.

    Attributes:
        Metadata (Metadata): The metadata of the output.
        ProcessOutput (ProcessOutput): The process output information.
    """
    Metadata: Metadata
    ProcessOutput: ProcessOutput
