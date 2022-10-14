# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.model_category import ModelCategory  # noqa: F401


def test_modelcategorys_get(client: TestClient):
    """Test case for modelcategorys_get

    List all instances of ModelCategory
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelcategorys",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelcategorys_id_delete(client: TestClient):
    """Test case for modelcategorys_id_delete

    Delete an existing ModelCategory
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/modelcategorys/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelcategorys_id_get(client: TestClient):
    """Test case for modelcategorys_id_get

    Get a single ModelCategory by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/modelcategorys/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelcategorys_id_put(client: TestClient):
    """Test case for modelcategorys_id_put

    Update an existing ModelCategory
    """
    model_category = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/modelcategorys/{id}".format(id='id_example'),
        headers=headers,
        json=model_category,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_modelcategorys_post(client: TestClient):
    """Test case for modelcategorys_post

    Create one ModelCategory
    """
    model_category = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/modelcategorys",
        headers=headers,
        json=model_category,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

