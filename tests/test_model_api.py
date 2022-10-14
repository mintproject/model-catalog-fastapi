# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.model import Model  # noqa: F401


def test_custom_model_index_get(client: TestClient):
    """Test case for custom_model_index_get

    Get a Model
    """
    params = [("custom_query_name", 'custom_model_index'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/model/index",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_model_intervention_get(client: TestClient):
    """Test case for custom_model_intervention_get

    Get a Model
    """
    params = [("custom_query_name", 'custom_model_intervetion'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/model/intervention",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_model_region_get(client: TestClient):
    """Test case for custom_model_region_get

    Get a Model
    """
    params = [("custom_query_name", 'custom_model_region'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/model/region",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_models_standard_variable_get(client: TestClient):
    """Test case for custom_models_standard_variable_get

    Get a list of models
    """
    params = [("custom_query_name", 'custom_model_standard_variable'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/models/standard_variable",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_models_variable_get(client: TestClient):
    """Test case for custom_models_variable_get

    Get a list of Model
    """
    params = [("custom_query_name", 'custom_models_variable'),     ("username", 'username_example'),     ("label", 'label_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/models/variable",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_models_get(client: TestClient):
    """Test case for models_get

    List all instances of Model
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/models",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_models_id_delete(client: TestClient):
    """Test case for models_id_delete

    Delete an existing Model
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/models/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_models_id_get(client: TestClient):
    """Test case for models_id_get

    Get a single Model by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/models/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_models_id_put(client: TestClient):
    """Test case for models_id_put

    Update an existing Model
    """
    model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/models/{id}".format(id='id_example'),
        headers=headers,
        json=model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_models_post(client: TestClient):
    """Test case for models_post

    Create one Model
    """
    model = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/models",
        headers=headers,
        json=model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

