# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.time_interval import TimeInterval  # noqa: F401


def test_timeintervals_get(client: TestClient):
    """Test case for timeintervals_get

    List all instances of TimeInterval
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/timeintervals",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_timeintervals_id_delete(client: TestClient):
    """Test case for timeintervals_id_delete

    Delete an existing TimeInterval
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/timeintervals/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_timeintervals_id_get(client: TestClient):
    """Test case for timeintervals_id_get

    Get a single TimeInterval by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/timeintervals/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_timeintervals_id_put(client: TestClient):
    """Test case for timeintervals_id_put

    Update an existing TimeInterval
    """
    time_interval = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/timeintervals/{id}".format(id='id_example'),
        headers=headers,
        json=time_interval,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_timeintervals_post(client: TestClient):
    """Test case for timeintervals_post

    Create one TimeInterval
    """
    time_interval = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/timeintervals",
        headers=headers,
        json=time_interval,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

