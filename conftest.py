"""Shared Pytest fixtures."""

import pytest

from clients.api_client import MetMuseumClient


@pytest.fixture(scope="session")
def client() -> MetMuseumClient:
    """Session-scoped HTTP client."""
    with MetMuseumClient() as api_client:
        yield api_client
