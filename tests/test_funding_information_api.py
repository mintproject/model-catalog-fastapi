# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.funding_information import FundingInformation  # noqa: F401


def test_fundinginformations_get(client: TestClient):
    """Test case for fundinginformations_get

    List all instances of FundingInformation
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/fundinginformations",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fundinginformations_id_delete(client: TestClient):
    """Test case for fundinginformations_id_delete

    Delete an existing FundingInformation
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/fundinginformations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fundinginformations_id_get(client: TestClient):
    """Test case for fundinginformations_id_get

    Get a single FundingInformation by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/fundinginformations/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fundinginformations_id_put(client: TestClient):
    """Test case for fundinginformations_id_put

    Update an existing FundingInformation
    """
    funding_information = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/fundinginformations/{id}".format(id='id_example'),
        headers=headers,
        json=funding_information,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fundinginformations_post(client: TestClient):
    """Test case for fundinginformations_post

    Create one FundingInformation
    """
    funding_information = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/fundinginformations",
        headers=headers,
        json=funding_information,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

