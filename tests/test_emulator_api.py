# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.emulator import Emulator  # noqa: F401


def test_emulators_get(client: TestClient):
    """Test case for emulators_get

    List all instances of Emulator
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/emulators",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_emulators_id_delete(client: TestClient):
    """Test case for emulators_id_delete

    Delete an existing Emulator
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/emulators/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_emulators_id_get(client: TestClient):
    """Test case for emulators_id_get

    Get a single Emulator by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/emulators/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_emulators_id_put(client: TestClient):
    """Test case for emulators_id_put

    Update an existing Emulator
    """
    emulator = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/emulators/{id}".format(id='id_example'),
        headers=headers,
        json=emulator,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_emulators_post(client: TestClient):
    """Test case for emulators_post

    Create one Emulator
    """
    emulator = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/emulators",
        headers=headers,
        json=emulator,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

