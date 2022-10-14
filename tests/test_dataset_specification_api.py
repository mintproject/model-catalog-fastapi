# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.dataset_specification import DatasetSpecification  # noqa: F401


def test_custom_configuration_id_inputs_get(client: TestClient):
    """Test case for custom_configuration_id_inputs_get

    Gets all inputs of a configuration
    """
    params = [("username", 'username_example'),     ("custom_query_name", 'search_datasetspecification_by_configurationid')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/configuration/{id}/inputs".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_datasetspecifications_get(client: TestClient):
    """Test case for custom_datasetspecifications_get

    Gets all inputs of a configuration
    """
    params = [("username", 'username_example'),     ("configurationid", 'configurationid_example'),     ("custom_query_name", 'custom_allinputs')]
    headers = {
    }
    response = client.request(
        "GET",
        "/custom/datasetspecifications",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datasetspecifications_get(client: TestClient):
    """Test case for datasetspecifications_get

    List all instances of DatasetSpecification
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/datasetspecifications",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datasetspecifications_id_delete(client: TestClient):
    """Test case for datasetspecifications_id_delete

    Delete an existing DatasetSpecification
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/datasetspecifications/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datasetspecifications_id_get(client: TestClient):
    """Test case for datasetspecifications_id_get

    Get a single DatasetSpecification by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/datasetspecifications/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datasetspecifications_id_put(client: TestClient):
    """Test case for datasetspecifications_id_put

    Update an existing DatasetSpecification
    """
    dataset_specification = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/datasetspecifications/{id}".format(id='id_example'),
        headers=headers,
        json=dataset_specification,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_datasetspecifications_post(client: TestClient):
    """Test case for datasetspecifications_post

    Create one DatasetSpecification
    """
    dataset_specification = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/datasetspecifications",
        headers=headers,
        json=dataset_specification,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

