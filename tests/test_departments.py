"""Tests for the /departments endpoint."""

import pytest

from models import DepartmentsResponse


@pytest.mark.smoke
def test_departments_returns_list(client):
    response = client.get_departments()
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    payload = DepartmentsResponse.model_validate(response.json())
    assert payload.departments


@pytest.mark.regression
def test_departments_have_positive_ids(client):
    payload = DepartmentsResponse.model_validate(client.get_departments().json())
    for dept in payload.departments:
        assert dept.departmentId > 0
        assert dept.displayName.strip()


@pytest.mark.regression
def test_departments_ids_are_unique(client):
    payload = DepartmentsResponse.model_validate(client.get_departments().json())
    ids = [d.departmentId for d in payload.departments]
    assert len(ids) == len(set(ids))
