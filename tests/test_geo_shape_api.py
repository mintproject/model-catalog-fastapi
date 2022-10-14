# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.geo_shape import GeoShape  # noqa: F401


def test_geoshapes_get(client: TestClient):
    """Test case for geoshapes_get

    List all instances of GeoShape
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/geoshapes",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geoshapes_id_delete(client: TestClient):
    """Test case for geoshapes_id_delete

    Delete an existing GeoShape
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/geoshapes/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geoshapes_id_get(client: TestClient):
    """Test case for geoshapes_id_get

    Get a single GeoShape by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/geoshapes/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geoshapes_id_put(client: TestClient):
    """Test case for geoshapes_id_put

    Update an existing GeoShape
    """
    geo_shape = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/geoshapes/{id}".format(id='id_example'),
        headers=headers,
        json=geo_shape,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geoshapes_post(client: TestClient):
    """Test case for geoshapes_post

    Create one GeoShape
    """
    geo_shape = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/geoshapes",
        headers=headers,
        json=geo_shape,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

