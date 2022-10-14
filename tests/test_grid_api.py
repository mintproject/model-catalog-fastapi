# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.grid import Grid  # noqa: F401


def test_grids_get(client: TestClient):
    """Test case for grids_get

    List all instances of Grid
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/grids",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grids_id_delete(client: TestClient):
    """Test case for grids_id_delete

    Delete an existing Grid
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/grids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grids_id_get(client: TestClient):
    """Test case for grids_id_get

    Get a single Grid by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/grids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grids_id_put(client: TestClient):
    """Test case for grids_id_put

    Update an existing Grid
    """
    grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/grids/{id}".format(id='id_example'),
        headers=headers,
        json=grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grids_post(client: TestClient):
    """Test case for grids_post

    Create one Grid
    """
    grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/grids",
        headers=headers,
        json=grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

