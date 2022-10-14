# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.numerical_index import NumericalIndex  # noqa: F401


def test_numericalindexs_get(client: TestClient):
    """Test case for numericalindexs_get

    List all instances of NumericalIndex
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/numericalindexs",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_numericalindexs_id_delete(client: TestClient):
    """Test case for numericalindexs_id_delete

    Delete an existing NumericalIndex
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/numericalindexs/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_numericalindexs_id_get(client: TestClient):
    """Test case for numericalindexs_id_get

    Get a single NumericalIndex by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/numericalindexs/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_numericalindexs_id_put(client: TestClient):
    """Test case for numericalindexs_id_put

    Update an existing NumericalIndex
    """
    numerical_index = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/numericalindexs/{id}".format(id='id_example'),
        headers=headers,
        json=numerical_index,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_numericalindexs_post(client: TestClient):
    """Test case for numericalindexs_post

    Create one NumericalIndex
    """
    numerical_index = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/numericalindexs",
        headers=headers,
        json=numerical_index,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

