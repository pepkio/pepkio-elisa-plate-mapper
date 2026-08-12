"""Pepkio ELISA Plate Mapper Python client package."""

from __future__ import annotations

from .client import PepkioClient
from .config import DEFAULT_API_BASE_URL, TOOL_ID
from .exceptions import PepkioAPIError
from .models import ElisaPlateMapperInput, RunOptions, RunResult, WellInput

__version__ = "0.1.0"

__all__ = [
    "DEFAULT_API_BASE_URL",
    "ElisaPlateMapperInput",
    "PepkioAPIError",
    "PepkioClient",
    "RunOptions",
    "RunResult",
    "TOOL_ID",
    "WellInput",
    "__version__",
]
