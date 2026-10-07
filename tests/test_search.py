"""Tests for /search and /v1.1/search endpoints."""

import pytest

from config import DEFAULT_PAGE_LIMIT, MAX_PAGE_LIMIT, MAX_REACHABLE_RESULTS
from models import ArtObject, SearchResult


@pytest.mark.smoke
def test_search_v1_1_by_keyword(client):
    response = client.search_v1_1(q="sunflowers")
    assert response.status_code == 200, response.text

    result = SearchResult.model_validate(response.json())
    assert result.total > 0
    assert result.objectIDs
    assert len(result.objectIDs) <= DEFAULT_PAGE_LIMIT


@pytest.mark.regression
def test_search_v1_1_default_page_size(client):
    response = client.search_v1_1(q="flowers")
    assert response.status_code == 200
    result = SearchResult.model_validate(response.json())
    assert len(result.objectIDs) <= DEFAULT_PAGE_LIMIT


@pytest.mark.regression
def test_search_v1_1_limit_capped_at_500(client):
    response = client.search_v1_1(q="flowers", limit=9999)
    assert response.status_code == 200
    result = SearchResult.model_validate(response.json())
    assert len(result.objectIDs) <= MAX_PAGE_LIMIT


@pytest.mark.regression
def test_search_v1_1_offset_paging_is_consistent(client):
    page1 = client.search_v1_1(q="flowers", offset=0, limit=10)
    page2 = client.search_v1_1(q="flowers", offset=10, limit=10)
    assert page1.status_code == page2.status_code == 200

    ids1 = SearchResult.model_validate(page1.json()).objectIDs or []
    ids2 = SearchResult.model_validate(page2.json()).objectIDs or []
    assert set(ids1).isdisjoint(set(ids2))


@pytest.mark.regression
def test_search_v1_1_offset_limit_boundary(client):
    response = client.search_v1_1(
        q="flowers", offset=MAX_REACHABLE_RESULTS, limit=10
    )
    assert response.status_code >= 400, response.text


@pytest.mark.regression
def test_search_filter_has_images(client):
    response = client.search_v1_1(q="cat", hasImages="true", limit=10)
    assert response.status_code == 200

    result = SearchResult.model_validate(response.json())
    assert result.objectIDs

    for object_id in result.objectIDs[:3]:
        art = ArtObject.model_validate(client.get_object(object_id).json())
        assert art.primaryImage


@pytest.mark.regression
def test_search_filter_only_no_q(client):
    response = client.search_v1_1(hasImages="true", departmentId=11, limit=5)
    assert response.status_code == 200
    result = SearchResult.model_validate(response.json())
    assert result.objectIDs


@pytest.mark.negative
def test_search_v1_1_nonsense_query(client):
    response = client.search_v1_1(q="zzxxqq__no_such_thing__12345")
    assert response.status_code == 200
    result = SearchResult.model_validate(response.json())
    assert result.total == 0 or not result.objectIDs
