# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.coupled_model import CoupledModel  # noqa: F401


def test_coupledmodels_get(client: TestClient):
    """Test case for coupledmodels_get

    List all instances of CoupledModel
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/coupledmodels",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_coupledmodels_id_delete(client: TestClient):
    """Test case for coupledmodels_id_delete

    Delete an existing CoupledModel
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/coupledmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_coupledmodels_id_get(client: TestClient):
    """Test case for coupledmodels_id_get

    Get a single CoupledModel by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/coupledmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_coupledmodels_id_put(client: TestClient):
    """Test case for coupledmodels_id_put

    Update an existing CoupledModel
    """
    coupled_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/coupledmodels/{id}".format(id='id_example'),
        headers=headers,
        json=coupled_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_coupledmodels_post(client: TestClient):
    """Test case for coupledmodels_post

    Create one CoupledModel
    """
    coupled_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/coupledmodels",
        headers=headers,
        json=coupled_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

