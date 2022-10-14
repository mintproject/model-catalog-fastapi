# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.process import Process  # noqa: F401


def test_processs_get(client: TestClient):
    """Test case for processs_get

    List all instances of Process
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/processs",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_processs_id_delete(client: TestClient):
    """Test case for processs_id_delete

    Delete an existing Process
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/processs/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_processs_id_get(client: TestClient):
    """Test case for processs_id_get

    Get a single Process by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/processs/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_processs_id_put(client: TestClient):
    """Test case for processs_id_put

    Update an existing Process
    """
    process = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/processs/{id}".format(id='id_example'),
        headers=headers,
        json=process,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_processs_post(client: TestClient):
    """Test case for processs_post

    Create one Process
    """
    process = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/processs",
        headers=headers,
        json=process,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

