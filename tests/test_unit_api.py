# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.unit import Unit  # noqa: F401


def test_units_get(client: TestClient):
    """Test case for units_get

    List all instances of Unit
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/units",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_units_id_delete(client: TestClient):
    """Test case for units_id_delete

    Delete an existing Unit
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/units/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_units_id_get(client: TestClient):
    """Test case for units_id_get

    Get a single Unit by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/units/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_units_id_put(client: TestClient):
    """Test case for units_id_put

    Update an existing Unit
    """
    unit = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/units/{id}".format(id='id_example'),
        headers=headers,
        json=unit,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_units_post(client: TestClient):
    """Test case for units_post

    Create one Unit
    """
    unit = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/units",
        headers=headers,
        json=unit,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

