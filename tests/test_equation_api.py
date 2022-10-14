# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.equation import Equation  # noqa: F401


def test_equations_get(client: TestClient):
    """Test case for equations_get

    List all instances of Equation
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/equations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_equations_id_delete(client: TestClient):
    """Test case for equations_id_delete

    Delete an existing Equation
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/equations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_equations_id_get(client: TestClient):
    """Test case for equations_id_get

    Get a single Equation by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/equations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_equations_id_put(client: TestClient):
    """Test case for equations_id_put

    Update an existing Equation
    """
    equation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/equations/{id}".format(id='id_example'),
        headers=headers,
        json=equation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_equations_post(client: TestClient):
    """Test case for equations_post

    Create one Equation
    """
    equation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/equations",
        headers=headers,
        json=equation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

