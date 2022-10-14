# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.variable import Variable  # noqa: F401


def test_variables_get(client: TestClient):
    """Test case for variables_get

    List all instances of Variable
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/variables",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variables_id_delete(client: TestClient):
    """Test case for variables_id_delete

    Delete an existing Variable
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/variables/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variables_id_get(client: TestClient):
    """Test case for variables_id_get

    Get a single Variable by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/variables/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variables_id_put(client: TestClient):
    """Test case for variables_id_put

    Update an existing Variable
    """
    variable = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/variables/{id}".format(id='id_example'),
        headers=headers,
        json=variable,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variables_post(client: TestClient):
    """Test case for variables_post

    Create one Variable
    """
    variable = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/variables",
        headers=headers,
        json=variable,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

