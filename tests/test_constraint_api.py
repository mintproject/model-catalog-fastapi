# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.constraint import Constraint  # noqa: F401


def test_constraints_get(client: TestClient):
    """Test case for constraints_get

    List all instances of Constraint
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/constraints",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_constraints_id_delete(client: TestClient):
    """Test case for constraints_id_delete

    Delete an existing Constraint
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/constraints/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_constraints_id_get(client: TestClient):
    """Test case for constraints_id_get

    Get a single Constraint by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/constraints/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_constraints_id_put(client: TestClient):
    """Test case for constraints_id_put

    Update an existing Constraint
    """
    constraint = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/constraints/{id}".format(id='id_example'),
        headers=headers,
        json=constraint,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_constraints_post(client: TestClient):
    """Test case for constraints_post

    Create one Constraint
    """
    constraint = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/constraints",
        headers=headers,
        json=constraint,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

