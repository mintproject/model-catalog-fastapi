# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.geo_coordinates import GeoCoordinates  # noqa: F401


def test_geocoordinatess_get(client: TestClient):
    """Test case for geocoordinatess_get

    List all instances of GeoCoordinates
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/geocoordinatess",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geocoordinatess_id_delete(client: TestClient):
    """Test case for geocoordinatess_id_delete

    Delete an existing GeoCoordinates
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/geocoordinatess/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geocoordinatess_id_get(client: TestClient):
    """Test case for geocoordinatess_id_get

    Get a single GeoCoordinates by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/geocoordinatess/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geocoordinatess_id_put(client: TestClient):
    """Test case for geocoordinatess_id_put

    Update an existing GeoCoordinates
    """
    geo_coordinates = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/geocoordinatess/{id}".format(id='id_example'),
        headers=headers,
        json=geo_coordinates,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_geocoordinatess_post(client: TestClient):
    """Test case for geocoordinatess_post

    Create one GeoCoordinates
    """
    geo_coordinates = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/geocoordinatess",
        headers=headers,
        json=geo_coordinates,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

