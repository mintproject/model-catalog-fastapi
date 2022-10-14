# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.configuration_setup import ConfigurationSetup  # noqa: F401
from openapi_server.models.model_configuration_setup import ModelConfigurationSetup  # noqa: F401


def test_configurationsetups_get(client: TestClient):
    """Test case for configurationsetups_get

    List all instances of ConfigurationSetup
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/configurationsetups",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_configurationsetups_id_delete(client: TestClient):
    """Test case for configurationsetups_id_delete

    Delete an existing ConfigurationSetup
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/configurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_configurationsetups_id_get(client: TestClient):
    """Test case for configurationsetups_id_get

    Get a single ConfigurationSetup by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/configurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_configurationsetups_id_put(client: TestClient):
    """Test case for configurationsetups_id_put

    Update an existing ConfigurationSetup
    """
    configuration_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/configurationsetups/{id}".format(id='id_example'),
        headers=headers,
        json=configuration_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_configurationsetups_post(client: TestClient):
    """Test case for configurationsetups_post

    Create one ConfigurationSetup
    """
    configuration_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/configurationsetups",
        headers=headers,
        json=configuration_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_configurationsetups_id_get(client: TestClient):
    """Test case for custom_configurationsetups_id_get

    Get a ModelConfigurationSetup
    """
    params = [("username", 'username_example'),     ("custom_query_name", 'custom_configurationsetups')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/configurationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

