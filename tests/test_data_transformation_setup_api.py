# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.data_transformation_setup import DataTransformationSetup  # noqa: F401


def test_datatransformationsetups_get(client: TestClient):
    """Test case for datatransformationsetups_get

    List all instances of DataTransformationSetup
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/datatransformationsetups",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformationsetups_id_delete(client: TestClient):
    """Test case for datatransformationsetups_id_delete

    Delete an existing DataTransformationSetup
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/datatransformationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformationsetups_id_get(client: TestClient):
    """Test case for datatransformationsetups_id_get

    Get a single DataTransformationSetup by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/datatransformationsetups/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformationsetups_id_put(client: TestClient):
    """Test case for datatransformationsetups_id_put

    Update an existing DataTransformationSetup
    """
    data_transformation_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/datatransformationsetups/{id}".format(id='id_example'),
        headers=headers,
        json=data_transformation_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datatransformationsetups_post(client: TestClient):
    """Test case for datatransformationsetups_post

    Create one DataTransformationSetup
    """
    data_transformation_setup = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/datatransformationsetups",
        headers=headers,
        json=data_transformation_setup,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

