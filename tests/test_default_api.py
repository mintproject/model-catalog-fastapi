# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.user import User  # noqa: F401


def test_user_login_post(client: TestClient):
    """Test case for user_login_post

    
    """
    user = {"password":"password","username":"username"}

    headers = {
    }
    response = client.request(
        "POST",
        "/user/login",
        headers=headers,
        json=user,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

