# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.intervention import Intervention  # noqa: F401


def test_interventions_get(client: TestClient):
    """Test case for interventions_get

    List all instances of Intervention
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/interventions",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_interventions_id_delete(client: TestClient):
    """Test case for interventions_id_delete

    Delete an existing Intervention
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/interventions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_interventions_id_get(client: TestClient):
    """Test case for interventions_id_get

    Get a single Intervention by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/interventions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_interventions_id_put(client: TestClient):
    """Test case for interventions_id_put

    Update an existing Intervention
    """
    intervention = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/interventions/{id}".format(id='id_example'),
        headers=headers,
        json=intervention,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_interventions_post(client: TestClient):
    """Test case for interventions_post

    Create one Intervention
    """
    intervention = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/interventions",
        headers=headers,
        json=intervention,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

