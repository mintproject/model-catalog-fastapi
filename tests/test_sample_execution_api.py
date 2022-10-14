# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.sample_execution import SampleExecution  # noqa: F401


def test_sampleexecutions_get(client: TestClient):
    """Test case for sampleexecutions_get

    List all instances of SampleExecution
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/sampleexecutions",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleexecutions_id_delete(client: TestClient):
    """Test case for sampleexecutions_id_delete

    Delete an existing SampleExecution
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/sampleexecutions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleexecutions_id_get(client: TestClient):
    """Test case for sampleexecutions_id_get

    Get a single SampleExecution by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/sampleexecutions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleexecutions_id_put(client: TestClient):
    """Test case for sampleexecutions_id_put

    Update an existing SampleExecution
    """
    sample_execution = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/sampleexecutions/{id}".format(id='id_example'),
        headers=headers,
        json=sample_execution,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sampleexecutions_post(client: TestClient):
    """Test case for sampleexecutions_post

    Create one SampleExecution
    """
    sample_execution = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/sampleexecutions",
        headers=headers,
        json=sample_execution,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

