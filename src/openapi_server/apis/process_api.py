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
from openapi_server.models.process import Process
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/processs",
    responses={
        200: {"model": List[Process], "description": "Successful response - returns an array with the instances of Process."},
    },
    tags=["Process"],
    summary="List all instances of Process",
    response_model_by_alias=True,
)
async def processs_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Process]:
    """Gets a list of all instances of Process (more information in https://w3id.org/okn/o/sdm#Process)"""
    ...


@router.delete(
    "/processs/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Process"],
    summary="Delete an existing Process",
    response_model_by_alias=True,
)
async def processs_id_delete(
    id: str = Path(None, description="The ID of the Process to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Process (more information in https://w3id.org/okn/o/sdm#Process)"""
    ...


@router.get(
    "/processs/{id}",
    responses={
        200: {"model": Process, "description": "Gets the details of a given Process"},
    },
    tags=["Process"],
    summary="Get a single Process by its id",
    response_model_by_alias=True,
)
async def processs_id_get(
    id: str = Path(None, description="The ID of the Process to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Process:
    """Gets the details of a given Process (more information in https://w3id.org/okn/o/sdm#Process)"""
    ...


@router.put(
    "/processs/{id}",
    responses={
        200: {"model": Process, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Process"],
    summary="Update an existing Process",
    response_model_by_alias=True,
)
async def processs_id_put(
    id: str = Path(None, description="The ID of the Process to be retrieved"),
    user: str = Query(None, description="Username"),
    process: Process = Body(None, description="An old Processto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Process:
    """Updates an existing Process (more information in https://w3id.org/okn/o/sdm#Process)"""
    ...


@router.post(
    "/processs",
    responses={
        201: {"model": Process, "description": "Created"},
    },
    tags=["Process"],
    summary="Create one Process",
    response_model_by_alias=True,
)
async def processs_post(
    user: str = Query(None, description="Username"),
    process: Process = Body(None, description="Information about the Processto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Process:
    """Create a new instance of Process (more information in https://w3id.org/okn/o/sdm#Process)"""
    ...
