# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.person import Person  # noqa: F401


def test_persons_get(client: TestClient):
    """Test case for persons_get

    List all instances of Person
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/persons",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_persons_id_delete(client: TestClient):
    """Test case for persons_id_delete

    Delete an existing Person
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/persons/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_persons_id_get(client: TestClient):
    """Test case for persons_id_get

    Get a single Person by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/persons/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_persons_id_put(client: TestClient):
    """Test case for persons_id_put

    Update an existing Person
    """
    person = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/persons/{id}".format(id='id_example'),
        headers=headers,
        json=person,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_persons_post(client: TestClient):
    """Test case for persons_post

    Create one Person
    """
    person = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/persons",
        headers=headers,
        json=person,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

