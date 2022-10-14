# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.user import User


router = APIRouter()


@router.post(
    "/user/login",
    responses={
        200: {"model": str, "description": "successful operation"},
        400: {"model": str, "description": "unsuccessful operation"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def user_login_post(
    user: User = Body(None, description="User credentials"),
) -> str:
    """Login the user"""
    ...
        
