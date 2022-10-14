# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.region import Region  # noqa: F401


def test_regions_get(client: TestClient):
    """Test case for regions_get

    List all instances of Region
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/regions",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_regions_id_delete(client: TestClient):
    """Test case for regions_id_delete

    Delete an existing Region
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/regions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_regions_id_get(client: TestClient):
    """Test case for regions_id_get

    Get a single Region by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/regions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_regions_id_put(client: TestClient):
    """Test case for regions_id_put

    Update an existing Region
    """
    region = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/regions/{id}".format(id='id_example'),
        headers=headers,
        json=region,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_regions_post(client: TestClient):
    """Test case for regions_post

    Create one Region
    """
    region = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/regions",
        headers=headers,
        json=region,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

