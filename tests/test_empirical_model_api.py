# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.empirical_model import EmpiricalModel  # noqa: F401


def test_empiricalmodels_get(client: TestClient):
    """Test case for empiricalmodels_get

    List all instances of EmpiricalModel
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/empiricalmodels",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_empiricalmodels_id_delete(client: TestClient):
    """Test case for empiricalmodels_id_delete

    Delete an existing EmpiricalModel
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/empiricalmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_empiricalmodels_id_get(client: TestClient):
    """Test case for empiricalmodels_id_get

    Get a single EmpiricalModel by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/empiricalmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_empiricalmodels_id_put(client: TestClient):
    """Test case for empiricalmodels_id_put

    Update an existing EmpiricalModel
    """
    empirical_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/empiricalmodels/{id}".format(id='id_example'),
        headers=headers,
        json=empirical_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_empiricalmodels_post(client: TestClient):
    """Test case for empiricalmodels_post

    Create one EmpiricalModel
    """
    empirical_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/empiricalmodels",
        headers=headers,
        json=empirical_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

