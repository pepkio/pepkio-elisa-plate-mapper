"""Typed API request/response models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .exceptions import PepkioAPIError


class WellInput(BaseModel):
    """Input well model for ELISA Plate Mapper."""

    model_config = ConfigDict(extra="allow")

    well: str = Field(description="Well identifier, e.g. 'A1', 'B2'")
    type: str = Field(description="Well type: 'standard', 'blank', 'control', 'unknown', 'empty'")
    label: str | None = Field(default=None, description="Optional well label")
    concentration: float | None = Field(default=None, description="Optional concentration value")
    od: float | None = Field(default=None, description="Optional optical density (OD) value")
    group_id: str | None = Field(default=None, description="Optional replicate group ID")
    replicate: int | None = Field(default=None, description="Optional replicate index")


class ElisaPlateMapperInput(BaseModel):
    """Tool input model for ELISA Plate Mapper."""

    model_config = ConfigDict(extra="allow")

    wells: list[WellInput] = Field(description="Assigned wells for the plate layout")


class RunOptions(BaseModel):
    """Optional fields for POST .../run."""

    idempotency_key: str | None = None
    label: str | None = None


class RunResult(BaseModel):
    """Tool run response envelope."""

    model_config = ConfigDict(extra="allow")

    run_id: str
    status: str
    result: dict[str, Any] | None = None
    error: dict[str, Any] | None = None
    result_url: str | None = None
    permalink: str | None = None
    duration_ms: int | None = None

    def raise_for_error(self) -> None:
        """Raise PepkioAPIError if the run response includes an error field."""
        if self.error is None:
            return
        err = self.error
        raise PepkioAPIError(
            err.get("message", "Tool run failed"),
            code=err.get("code"),
            details=err.get("details") if isinstance(err.get("details"), dict) else {},
            response_body={"run_id": self.run_id, "status": self.status, "error": self.error},
        )


def parse_run_response(data: dict[str, Any]) -> RunResult:
    """Parse a run API JSON body into RunResult."""
    return RunResult.model_validate(data)
