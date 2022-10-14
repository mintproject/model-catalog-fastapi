# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.sample_collection import SampleCollection  # noqa: F401


def test_samplecollections_get(client: TestClient):
    """Test case for samplecollections_get

    List all instances of SampleCollection
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/samplecollections",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_samplecollections_id_delete(client: TestClient):
    """Test case for samplecollections_id_delete

    Delete an existing SampleCollection
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/samplecollections/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_samplecollections_id_get(client: TestClient):
    """Test case for samplecollections_id_get

    Get a single SampleCollection by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/samplecollections/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_samplecollections_id_put(client: TestClient):
    """Test case for samplecollections_id_put

    Update an existing SampleCollection
    """
    sample_collection = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/samplecollections/{id}".format(id='id_example'),
        headers=headers,
        json=sample_collection,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_samplecollections_post(client: TestClient):
    """Test case for samplecollections_post

    Create one SampleCollection
    """
    sample_collection = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/samplecollections",
        headers=headers,
        json=sample_collection,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

