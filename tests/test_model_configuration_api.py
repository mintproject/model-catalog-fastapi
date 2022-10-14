# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.model_configuration import ModelConfiguration  # noqa: F401


def test_custom_modelconfigurations_id_get(client: TestClient):
    """Test case for custom_modelconfigurations_id_get

    Get a ModelConfiguration
    """
    params = [("username", 'username_example'),     ("custom_query_name", 'custom_modelconfigurations')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/modelconfigurations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurations_get(client: TestClient):
    """Test case for modelconfigurations_get

    List all instances of ModelConfiguration
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelconfigurations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurations_id_delete(client: TestClient):
    """Test case for modelconfigurations_id_delete

    Delete an existing ModelConfiguration
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/modelconfigurations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurations_id_get(client: TestClient):
    """Test case for modelconfigurations_id_get

    Get a single ModelConfiguration by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelconfigurations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurations_id_put(client: TestClient):
    """Test case for modelconfigurations_id_put

    Update an existing ModelConfiguration
    """
    model_configuration = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/modelconfigurations/{id}".format(id='id_example'),
        headers=headers,
        json=model_configuration,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurations_post(client: TestClient):
    """Test case for modelconfigurations_post

    Create one ModelConfiguration
    """
    model_configuration = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/modelconfigurations",
        headers=headers,
        json=model_configuration,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

