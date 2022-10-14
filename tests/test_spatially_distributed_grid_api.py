# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid  # noqa: F401


def test_spatiallydistributedgrids_get(client: TestClient):
    """Test case for spatiallydistributedgrids_get

    List all instances of SpatiallyDistributedGrid
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/spatiallydistributedgrids",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatiallydistributedgrids_id_delete(client: TestClient):
    """Test case for spatiallydistributedgrids_id_delete

    Delete an existing SpatiallyDistributedGrid
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/spatiallydistributedgrids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatiallydistributedgrids_id_get(client: TestClient):
    """Test case for spatiallydistributedgrids_id_get

    Get a single SpatiallyDistributedGrid by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/spatiallydistributedgrids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatiallydistributedgrids_id_put(client: TestClient):
    """Test case for spatiallydistributedgrids_id_put

    Update an existing SpatiallyDistributedGrid
    """
    spatially_distributed_grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/spatiallydistributedgrids/{id}".format(id='id_example'),
        headers=headers,
        json=spatially_distributed_grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatiallydistributedgrids_post(client: TestClient):
    """Test case for spatiallydistributedgrids_post

    Create one SpatiallyDistributedGrid
    """
    spatially_distributed_grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/spatiallydistributedgrids",
        headers=headers,
        json=spatially_distributed_grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

