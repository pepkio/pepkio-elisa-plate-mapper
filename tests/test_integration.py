"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_elisa_plate_mapper.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY") or os.getenv("PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, default_base_url = request.param
    base_url = os.getenv("PEPKIO_API_BASE_URL") or default_base_url
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "elisa-plate-mapper"
    names = live_client.list_examples()
    assert "example_sandwich_elisa" in names


def test_run_example_sandwich_elisa(live_client: PepkioClient):
    inp = live_client.get_example_input("example_sandwich_elisa")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert "blank_count" in result.result
    assert result.result.get("blank_count") == 1
    assert "standard_point_count" in result.result


def test_run_missing_blank_warns(live_client: PepkioClient):
    inp = live_client.get_example_input("missing_blank_warns")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("blank_count") == 0


def test_run_high_cv_od(live_client: PepkioClient):
    inp = live_client.get_example_input("high_cv_od")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert "blank_count" in result.result


def test_get_run_integration(live_client: PepkioClient):
    inp = live_client.get_example_input("example_sandwich_elisa")
    run_res = live_client.run(inp)
    fetched = live_client.get_run(run_res.run_id)
    assert fetched.run_id == run_res.run_id
    assert fetched.status == "completed"
    assert fetched.result == run_res.result
