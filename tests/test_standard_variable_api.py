# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.standard_variable import StandardVariable  # noqa: F401


def test_standardvariables_get(client: TestClient):
    """Test case for standardvariables_get

    List all instances of StandardVariable
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/standardvariables",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_standardvariables_id_delete(client: TestClient):
    """Test case for standardvariables_id_delete

    Delete an existing StandardVariable
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/standardvariables/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_standardvariables_id_get(client: TestClient):
    """Test case for standardvariables_id_get

    Get a single StandardVariable by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/standardvariables/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_standardvariables_id_put(client: TestClient):
    """Test case for standardvariables_id_put

    Update an existing StandardVariable
    """
    standard_variable = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/standardvariables/{id}".format(id='id_example'),
        headers=headers,
        json=standard_variable,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_standardvariables_post(client: TestClient):
    """Test case for standardvariables_post

    Create one StandardVariable
    """
    standard_variable = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/standardvariables",
        headers=headers,
        json=standard_variable,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

