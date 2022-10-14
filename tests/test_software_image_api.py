# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.software_image import SoftwareImage  # noqa: F401


def test_softwareimages_get(client: TestClient):
    """Test case for softwareimages_get

    List all instances of SoftwareImage
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareimages",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareimages_id_delete(client: TestClient):
    """Test case for softwareimages_id_delete

    Delete an existing SoftwareImage
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/softwareimages/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareimages_id_get(client: TestClient):
    """Test case for softwareimages_id_get

    Get a single SoftwareImage by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwareimages/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareimages_id_put(client: TestClient):
    """Test case for softwareimages_id_put

    Update an existing SoftwareImage
    """
    software_image = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/softwareimages/{id}".format(id='id_example'),
        headers=headers,
        json=software_image,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwareimages_post(client: TestClient):
    """Test case for softwareimages_post

    Create one SoftwareImage
    """
    software_image = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/softwareimages",
        headers=headers,
        json=software_image,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

