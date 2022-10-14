# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.organization import Organization  # noqa: F401


def test_organizations_get(client: TestClient):
    """Test case for organizations_get

    List all instances of Organization
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/organizations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_organizations_id_delete(client: TestClient):
    """Test case for organizations_id_delete

    Delete an existing Organization
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/organizations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_organizations_id_get(client: TestClient):
    """Test case for organizations_id_get

    Get a single Organization by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/organizations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_organizations_id_put(client: TestClient):
    """Test case for organizations_id_put

    Update an existing Organization
    """
    organization = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/organizations/{id}".format(id='id_example'),
        headers=headers,
        json=organization,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_organizations_post(client: TestClient):
    """Test case for organizations_post

    Create one Organization
    """
    organization = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/organizations",
        headers=headers,
        json=organization,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

