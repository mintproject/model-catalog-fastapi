# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.sample_resource import SampleResource  # noqa: F401


def test_sampleresources_get(client: TestClient):
    """Test case for sampleresources_get

    List all instances of SampleResource
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/sampleresources",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleresources_id_delete(client: TestClient):
    """Test case for sampleresources_id_delete

    Delete an existing SampleResource
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/sampleresources/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleresources_id_get(client: TestClient):
    """Test case for sampleresources_id_get

    Get a single SampleResource by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/sampleresources/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleresources_id_put(client: TestClient):
    """Test case for sampleresources_id_put

    Update an existing SampleResource
    """
    sample_resource = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/sampleresources/{id}".format(id='id_example'),
        headers=headers,
        json=sample_resource,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleresources_post(client: TestClient):
    """Test case for sampleresources_post

    Create one SampleResource
    """
    sample_resource = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/sampleresources",
        headers=headers,
        json=sample_resource,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

