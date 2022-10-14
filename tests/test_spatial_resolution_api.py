# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.spatial_resolution import SpatialResolution  # noqa: F401


def test_spatialresolutions_get(client: TestClient):
    """Test case for spatialresolutions_get

    List all instances of SpatialResolution
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/spatialresolutions",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatialresolutions_id_delete(client: TestClient):
    """Test case for spatialresolutions_id_delete

    Delete an existing SpatialResolution
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/spatialresolutions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatialresolutions_id_get(client: TestClient):
    """Test case for spatialresolutions_id_get

    Get a single SpatialResolution by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/spatialresolutions/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatialresolutions_id_put(client: TestClient):
    """Test case for spatialresolutions_id_put

    Update an existing SpatialResolution
    """
    spatial_resolution = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/spatialresolutions/{id}".format(id='id_example'),
        headers=headers,
        json=spatial_resolution,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_spatialresolutions_post(client: TestClient):
    """Test case for spatialresolutions_post

    Create one SpatialResolution
    """
    spatial_resolution = {"value":{"id":"some_id"}}
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/spatialresolutions",
        headers=headers,
        json=spatial_resolution,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

