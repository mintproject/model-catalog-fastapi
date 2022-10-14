# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.image import Image  # noqa: F401


def test_images_get(client: TestClient):
    """Test case for images_get

    List all instances of Image
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/images",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_images_id_delete(client: TestClient):
    """Test case for images_id_delete

    Delete an existing Image
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/images/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_images_id_get(client: TestClient):
    """Test case for images_id_get

    Get a single Image by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/images/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_images_id_put(client: TestClient):
    """Test case for images_id_put

    Update an existing Image
    """
    image = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/images/{id}".format(id='id_example'),
        headers=headers,
        json=image,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_images_post(client: TestClient):
    """Test case for images_post

    Create one Image
    """
    image = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/images",
        headers=headers,
        json=image,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

