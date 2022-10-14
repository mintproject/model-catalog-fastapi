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
from openapi_server.models.time_interval import TimeInterval
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/timeintervals",
    responses={
        200: {"model": List[TimeInterval], "description": "Successful response - returns an array with the instances of TimeInterval."},
    },
    tags=["TimeInterval"],
    summary="List all instances of TimeInterval",
    response_model_by_alias=True,
)
async def timeintervals_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[TimeInterval]:
    """Gets a list of all instances of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)"""
    ...


@router.delete(
    "/timeintervals/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["TimeInterval"],
    summary="Delete an existing TimeInterval",
    response_model_by_alias=True,
)
async def timeintervals_id_delete(
    id: str = Path(None, description="The ID of the TimeInterval to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)"""
    ...


@router.get(
    "/timeintervals/{id}",
    responses={
        200: {"model": TimeInterval, "description": "Gets the details of a given TimeInterval"},
    },
    tags=["TimeInterval"],
    summary="Get a single TimeInterval by its id",
    response_model_by_alias=True,
)
async def timeintervals_id_get(
    id: str = Path(None, description="The ID of the TimeInterval to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> TimeInterval:
    """Gets the details of a given TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)"""
    ...


@router.put(
    "/timeintervals/{id}",
    responses={
        200: {"model": TimeInterval, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["TimeInterval"],
    summary="Update an existing TimeInterval",
    response_model_by_alias=True,
)
async def timeintervals_id_put(
    id: str = Path(None, description="The ID of the TimeInterval to be retrieved"),
    user: str = Query(None, description="Username"),
    time_interval: TimeInterval = Body(None, description="An old TimeIntervalto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> TimeInterval:
    """Updates an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)"""
    ...


@router.post(
    "/timeintervals",
    responses={
        201: {"model": TimeInterval, "description": "Created"},
    },
    tags=["TimeInterval"],
    summary="Create one TimeInterval",
    response_model_by_alias=True,
)
async def timeintervals_post(
    user: str = Query(None, description="Username"),
    time_interval: TimeInterval = Body(None, description="Information about the TimeIntervalto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> TimeInterval:
    """Create a new instance of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)"""
    ...
