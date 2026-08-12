"""Shared test fixtures for pepkio-elisa-plate-mapper."""

from __future__ import annotations

import pytest


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "schema_version": "1.0",
        "tool_id": "elisa-plate-mapper",
        "title": "ELISA Plate Mapper",
        "description": "Visual 96-well ELISA plate layout planner",
        "execution_mode": "sync",
        "input": {
            "type": "object",
            "required": ["wells"],
            "properties": {
                "wells": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["well", "type"],
                        "properties": {
                            "well": {"type": "string"},
                            "type": {"type": "string"},
                        },
                    },
                }
            },
        },
        "examples": [
            {
                "name": "example_sandwich_elisa",
                "input": {
                    "wells": [
                        {"well": "A1", "type": "blank", "label": "Blank", "group_id": "Blank"},
                        {
                            "well": "A2",
                            "type": "standard",
                            "label": "Std-1-1",
                            "concentration": 1000,
                            "group_id": "Std-1",
                            "replicate": 1,
                        },
                        {
                            "well": "A3",
                            "type": "standard",
                            "label": "Std-1-2",
                            "concentration": 1000,
                            "group_id": "Std-1",
                            "replicate": 2,
                        },
                    ]
                },
                "output": {"blank_count": 1, "standard_point_count": 1},
            },
            {
                "name": "missing_blank_warns",
                "input": {
                    "wells": [
                        {
                            "well": "A2",
                            "type": "standard",
                            "label": "Std-1",
                            "concentration": 1000,
                            "group_id": "Std-1",
                        },
                        {
                            "well": "A3",
                            "type": "standard",
                            "label": "Std-2",
                            "concentration": 500,
                            "group_id": "Std-2",
                        },
                    ]
                },
                "output": {"blank_count": 0, "standard_point_count": 2},
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_test123",
        "status": "completed",
        "result": {
            "warnings": [],
            "cv_groups": [],
            "standard_point_count": 1,
            "blank_count": 1,
            "perimeter_standard_fraction": 1.0,
        },
        "error": None,
        "result_url": "https://tools.example.com/api/tools/v1/runs/run_test123",
        "permalink": "https://tools.example.com/r/run_test123",
        "duration_ms": 5,
    }
