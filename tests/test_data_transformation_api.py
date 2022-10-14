# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.data_transformation import DataTransformation  # noqa: F401


def test_custom_datasetspecifications_id_datatransformations_get(client: TestClient):
    """Test case for custom_datasetspecifications_id_datatransformations_get

    Gets a list of data transformations related a dataset
    """
    params = [("custom_query_name", 'custom_datatransformations'),     ("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/datasetspecifications/{id}/datatransformations".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformations_get(client: TestClient):
    """Test case for datatransformations_get

    List all instances of DataTransformation
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/datatransformations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformations_id_delete(client: TestClient):
    """Test case for datatransformations_id_delete

    Delete an existing DataTransformation
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/datatransformations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformations_id_get(client: TestClient):
    """Test case for datatransformations_id_get

    Get a single DataTransformation by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/datatransformations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformations_id_put(client: TestClient):
    """Test case for datatransformations_id_put

    Update an existing DataTransformation
    """
    data_transformation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/datatransformations/{id}".format(id='id_example'),
        headers=headers,
        json=data_transformation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformations_post(client: TestClient):
    """Test case for datatransformations_post

    Create one DataTransformation
    """
    data_transformation = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/datatransformations",
        headers=headers,
        json=data_transformation,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

