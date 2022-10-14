# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.theory_guided_model import TheoryGuidedModel  # noqa: F401


def test_theory_guidedmodels_get(client: TestClient):
    """Test case for theory_guidedmodels_get

    List all instances of Theory-GuidedModel
    """
    params = [("username", 'username_example'),     ("label", 'label_example'),     ("page", 1),     ("per_page", 100)]
    headers = {
    }
    response = client.request(
        "GET",
        "/theory-guidedmodels",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_theory_guidedmodels_id_delete(client: TestClient):
    """Test case for theory_guidedmodels_id_delete

    Delete an existing Theory-GuidedModel
    """
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "DELETE",
        "/theory-guidedmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_theory_guidedmodels_id_get(client: TestClient):
    """Test case for theory_guidedmodels_id_get

    Get a single Theory-GuidedModel by its id
    """
    params = [("username", 'username_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/theory-guidedmodels/{id}".format(id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_theory_guidedmodels_id_put(client: TestClient):
    """Test case for theory_guidedmodels_id_put

    Update an existing Theory-GuidedModel
    """
    theory_guided_model = openapi_server.TheoryGuidedModel()
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "PUT",
        "/theory-guidedmodels/{id}".format(id='id_example'),
        headers=headers,
        json=theory_guided_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_theory_guidedmodels_post(client: TestClient):
    """Test case for theory_guidedmodels_post

    Create one Theory-GuidedModel
    """
    theory_guided_model = openapi_server.TheoryGuidedModel()
    params = [("user", 'user_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/theory-guidedmodels",
        headers=headers,
        json=theory_guided_model,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

