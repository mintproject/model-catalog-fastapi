# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.catalog_identifier import CatalogIdentifier  # noqa: F401


def test_catalogidentifiers_get(client: TestClient):
    """Test case for catalogidentifiers_get

    List all instances of CatalogIdentifier
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/catalogidentifiers",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_catalogidentifiers_id_delete(client: TestClient):
    """Test case for catalogidentifiers_id_delete

    Delete an existing CatalogIdentifier
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/catalogidentifiers/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_catalogidentifiers_id_get(client: TestClient):
    """Test case for catalogidentifiers_id_get

    Get a single CatalogIdentifier by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/catalogidentifiers/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_catalogidentifiers_id_put(client: TestClient):
    """Test case for catalogidentifiers_id_put

    Update an existing CatalogIdentifier
    """
    catalog_identifier = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/catalogidentifiers/{id}".format(id='id_example'),
        headers=headers,
        json=catalog_identifier,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_catalogidentifiers_post(client: TestClient):
    """Test case for catalogidentifiers_post

    Create one CatalogIdentifier
    """
    catalog_identifier = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/catalogidentifiers",
        headers=headers,
        json=catalog_identifier,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

