# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.visualization import Visualization  # noqa: F401


def test_visualizations_get(client: TestClient):
    """Test case for visualizations_get

    List all instances of Visualization
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/visualizations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_visualizations_id_delete(client: TestClient):
    """Test case for visualizations_id_delete

    Delete an existing Visualization
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/visualizations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_visualizations_id_get(client: TestClient):
    """Test case for visualizations_id_get

    Get a single Visualization by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/visualizations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_visualizations_id_put(client: TestClient):
    """Test case for visualizations_id_put

    Update an existing Visualization
    """
    visualization = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/visualizations/{id}".format(id='id_example'),
        headers=headers,
        json=visualization,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_visualizations_post(client: TestClient):
    """Test case for visualizations_post

    Create one Visualization
    """
    visualization = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/visualizations",
        headers=headers,
        json=visualization,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

