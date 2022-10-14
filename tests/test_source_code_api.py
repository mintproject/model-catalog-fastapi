# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.source_code import SourceCode  # noqa: F401


def test_sourcecodes_get(client: TestClient):
    """Test case for sourcecodes_get

    List all instances of SourceCode
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/sourcecodes",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sourcecodes_id_delete(client: TestClient):
    """Test case for sourcecodes_id_delete

    Delete an existing SourceCode
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/sourcecodes/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sourcecodes_id_get(client: TestClient):
    """Test case for sourcecodes_id_get

    Get a single SourceCode by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/sourcecodes/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sourcecodes_id_put(client: TestClient):
    """Test case for sourcecodes_id_put

    Update an existing SourceCode
    """
    source_code = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/sourcecodes/{id}".format(id='id_example'),
        headers=headers,
        json=source_code,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_sourcecodes_post(client: TestClient):
    """Test case for sourcecodes_post

    Create one SourceCode
    """
    source_code = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/sourcecodes",
        headers=headers,
        json=source_code,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

