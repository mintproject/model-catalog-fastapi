# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.point_based_grid import PointBasedGrid  # noqa: F401


def test_pointbasedgrids_get(client: TestClient):
    """Test case for pointbasedgrids_get

    List all instances of PointBasedGrid
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/pointbasedgrids",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pointbasedgrids_id_delete(client: TestClient):
    """Test case for pointbasedgrids_id_delete

    Delete an existing PointBasedGrid
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/pointbasedgrids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pointbasedgrids_id_get(client: TestClient):
    """Test case for pointbasedgrids_id_get

    Get a single PointBasedGrid by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/pointbasedgrids/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pointbasedgrids_id_put(client: TestClient):
    """Test case for pointbasedgrids_id_put

    Update an existing PointBasedGrid
    """
    point_based_grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/pointbasedgrids/{id}".format(id='id_example'),
        headers=headers,
        json=point_based_grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pointbasedgrids_post(client: TestClient):
    """Test case for pointbasedgrids_post

    Create one PointBasedGrid
    """
    point_based_grid = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/pointbasedgrids",
        headers=headers,
        json=point_based_grid,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

