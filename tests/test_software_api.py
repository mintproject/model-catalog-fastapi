# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.software import Software  # noqa: F401


def test_softwares_get(client: TestClient):
    """Test case for softwares_get

    List all instances of Software
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwares",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwares_id_delete(client: TestClient):
    """Test case for softwares_id_delete

    Delete an existing Software
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/softwares/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwares_id_get(client: TestClient):
    """Test case for softwares_id_get

    Get a single Software by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/softwares/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwares_id_put(client: TestClient):
    """Test case for softwares_id_put

    Update an existing Software
    """
    software = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/softwares/{id}".format(id='id_example'),
        headers=headers,
        json=software,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_softwares_post(client: TestClient):
    """Test case for softwares_post

    Create one Software
    """
    software = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/softwares",
        headers=headers,
        json=software,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

