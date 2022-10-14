# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.software_configuration import SoftwareConfiguration  # noqa: F401


def test_softwareconfigurations_get(client: TestClient):
    """Test case for softwareconfigurations_get

    List all instances of SoftwareConfiguration
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareconfigurations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareconfigurations_id_delete(client: TestClient):
    """Test case for softwareconfigurations_id_delete

    Delete an existing SoftwareConfiguration
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/softwareconfigurations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareconfigurations_id_get(client: TestClient):
    """Test case for softwareconfigurations_id_get

    Get a single SoftwareConfiguration by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareconfigurations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareconfigurations_id_put(client: TestClient):
    """Test case for softwareconfigurations_id_put

    Update an existing SoftwareConfiguration
    """
    software_configuration = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/softwareconfigurations/{id}".format(id='id_example'),
        headers=headers,
        json=software_configuration,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareconfigurations_post(client: TestClient):
    """Test case for softwareconfigurations_post

    Create one SoftwareConfiguration
    """
    software_configuration = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/softwareconfigurations",
        headers=headers,
        json=software_configuration,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

