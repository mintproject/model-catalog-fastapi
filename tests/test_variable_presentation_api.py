# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.variable_presentation import VariablePresentation  # noqa: F401


def test_variablepresentations_get(client: TestClient):
    """Test case for variablepresentations_get

    List all instances of VariablePresentation
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/variablepresentations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variablepresentations_id_delete(client: TestClient):
    """Test case for variablepresentations_id_delete

    Delete an existing VariablePresentation
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/variablepresentations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variablepresentations_id_get(client: TestClient):
    """Test case for variablepresentations_id_get

    Get a single VariablePresentation by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/variablepresentations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variablepresentations_id_put(client: TestClient):
    """Test case for variablepresentations_id_put

    Update an existing VariablePresentation
    """
    variable_presentation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/variablepresentations/{id}".format(id='id_example'),
        headers=headers,
        json=variable_presentation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_variablepresentations_post(client: TestClient):
    """Test case for variablepresentations_post

    Create one VariablePresentation
    """
    variable_presentation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/variablepresentations",
        headers=headers,
        json=variable_presentation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

