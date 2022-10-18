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
from openapi_server.utils.vars import DEFAULT_TYPE_NAME, DEFAULT_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

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
    return query_manager.post_resource(
        
        
        body=user,
        rdf_type_uri=DEFAULT_TYPE_URI,
        rdf_type_name=DEFAULT_TYPE_NAME, 
        kls=default
        )
        
