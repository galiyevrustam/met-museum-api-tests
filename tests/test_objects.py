"""Tests for the /objects and /objects/{objectID} endpoints."""

import pytest
from pydantic import ValidationError

from config import INVALID_OBJECT_ID, VALID_OBJECT_ID, SMOKE_OBJECT_ID
from models import ArtObject, SearchResult


@pytest.mark.smoke
def test_get_object_by_valid_id_returns_200(client):
    response = client.get_object(VALID_OBJECT_ID)

    assert response.status_code == 200, response.text
    assert response.headers["Content-Type"].startswith("application/json")

    payload = response.json()
    art_object = ArtObject.model_validate(payload)

    assert art_object.objectID == VALID_OBJECT_ID
    assert art_object.title, "Title should not be empty for a known object"
    assert art_object.repository == "Metropolitan Museum of Art, New York, NY"


@pytest.mark.smoke
def test_get_documented_object(client):
    response = client.get_object(SMOKE_OBJECT_ID)
    assert response.status_code == 200

    art = ArtObject.model_validate(response.json())
    assert art.objectID == SMOKE_OBJECT_ID
    assert art.title == "Quail and Millet"
    assert art.artistDisplayName == "Kiyohara Yukinobu"
    assert art.department == "Asian Art"
    assert art.isPublicDomain is True


@pytest.mark.negative
def test_get_object_with_invalid_id_returns_404(client):
    response = client.get_object(INVALID_OBJECT_ID)
    assert response.status_code == 404, response.text


@pytest.mark.regression
def test_objects_endpoint_returns_id_list(client):
    response = client.get_objects()
    assert response.status_code == 200

    result = SearchResult.model_validate(response.json())
    assert result.total and result.total > 0
    assert result.objectIDs
