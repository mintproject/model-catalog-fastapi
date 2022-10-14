# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.hybrid_model import HybridModel  # noqa: F401


def test_hybridmodels_get(client: TestClient):
    """Test case for hybridmodels_get

    List all instances of HybridModel
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/hybridmodels",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_hybridmodels_id_delete(client: TestClient):
    """Test case for hybridmodels_id_delete

    Delete an existing HybridModel
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/hybridmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_hybridmodels_id_get(client: TestClient):
    """Test case for hybridmodels_id_get

    Get a single HybridModel by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/hybridmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_hybridmodels_id_put(client: TestClient):
    """Test case for hybridmodels_id_put

    Update an existing HybridModel
    """
    hybrid_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/hybridmodels/{id}".format(id='id_example'),
        headers=headers,
        json=hybrid_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_hybridmodels_post(client: TestClient):
    """Test case for hybridmodels_post

    Create one HybridModel
    """
    hybrid_model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/hybridmodels",
        headers=headers,
        json=hybrid_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

