# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: F401


def test_custom_modelconfigurationsetups_id_get(client: TestClient):
    """Test case for custom_modelconfigurationsetups_id_get

    Get a ModelConfigurationSetup
    """
    params = [("username", 'username_example'),     ("custom_query_name", 'custom_modelconfigurationsetups')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/modelconfigurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_modelconfigurationsetups_variable_get(client: TestClient):
    """Test case for custom_modelconfigurationsetups_variable_get

    Get a list  Model
    """
    params = [("custom_query_name", 'custom_modelconfigurationsetups_variable'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/modelconfigurationsetups/variable",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurationsetups_get(client: TestClient):
    """Test case for modelconfigurationsetups_get

    List all instances of ModelConfigurationSetup
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelconfigurationsetups",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurationsetups_id_delete(client: TestClient):
    """Test case for modelconfigurationsetups_id_delete

    Delete an existing ModelConfigurationSetup
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/modelconfigurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurationsetups_id_get(client: TestClient):
    """Test case for modelconfigurationsetups_id_get

    Get a single ModelConfigurationSetup by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelconfigurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurationsetups_id_put(client: TestClient):
    """Test case for modelconfigurationsetups_id_put

    Update an existing ModelConfigurationSetup
    """
    model_configuration_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/modelconfigurationsetups/{id}".format(id='id_example'),
        headers=headers,
        json=model_configuration_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelconfigurationsetups_post(client: TestClient):
    """Test case for modelconfigurationsetups_post

    Create one ModelConfigurationSetup
    """
    model_configuration_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/modelconfigurationsetups",
        headers=headers,
        json=model_configuration_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

