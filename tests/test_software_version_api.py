# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.software_version import SoftwareVersion  # noqa: F401


def test_softwareversions_get(client: TestClient):
    """Test case for softwareversions_get

    List all instances of SoftwareVersion
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareversions",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareversions_id_delete(client: TestClient):
    """Test case for softwareversions_id_delete

    Delete an existing SoftwareVersion
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/softwareversions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareversions_id_get(client: TestClient):
    """Test case for softwareversions_id_get

    Get a single SoftwareVersion by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareversions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareversions_id_put(client: TestClient):
    """Test case for softwareversions_id_put

    Update an existing SoftwareVersion
    """
    software_version = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/softwareversions/{id}".format(id='id_example'),
        headers=headers,
        json=software_version,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareversions_post(client: TestClient):
    """Test case for softwareversions_post

    Create one SoftwareVersion
    """
    software_version = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/softwareversions",
        headers=headers,
        json=software_version,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

