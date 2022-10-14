# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.parameter import Parameter  # noqa: F401


def test_parameters_get(client: TestClient):
    """Test case for parameters_get

    List all instances of Parameter
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/parameters",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_parameters_id_delete(client: TestClient):
    """Test case for parameters_id_delete

    Delete an existing Parameter
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/parameters/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_parameters_id_get(client: TestClient):
    """Test case for parameters_id_get

    Get a single Parameter by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/parameters/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_parameters_id_put(client: TestClient):
    """Test case for parameters_id_put

    Update an existing Parameter
    """
    parameter = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/parameters/{id}".format(id='id_example'),
        headers=headers,
        json=parameter,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_parameters_post(client: TestClient):
    """Test case for parameters_post

    Create one Parameter
    """
    parameter = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/parameters",
        headers=headers,
        json=parameter,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

