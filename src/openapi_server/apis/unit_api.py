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
from openapi_server.models.unit import Unit
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/units",
    responses={
        200: {"model": List[Unit], "description": "Successful response - returns an array with the instances of Unit."},
    },
    tags=["Unit"],
    summary="List all instances of Unit",
    response_model_by_alias=True,
)
async def units_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Unit]:
    """Gets a list of all instances of Unit (more information in https://w3id.org/okn/o/sd#Unit)"""
    ...


@router.delete(
    "/units/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Unit"],
    summary="Delete an existing Unit",
    response_model_by_alias=True,
)
async def units_id_delete(
    id: str = Path(None, description="The ID of the Unit to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Unit (more information in https://w3id.org/okn/o/sd#Unit)"""
    ...


@router.get(
    "/units/{id}",
    responses={
        200: {"model": Unit, "description": "Gets the details of a given Unit"},
    },
    tags=["Unit"],
    summary="Get a single Unit by its id",
    response_model_by_alias=True,
)
async def units_id_get(
    id: str = Path(None, description="The ID of the Unit to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Unit:
    """Gets the details of a given Unit (more information in https://w3id.org/okn/o/sd#Unit)"""
    ...


@router.put(
    "/units/{id}",
    responses={
        200: {"model": Unit, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Unit"],
    summary="Update an existing Unit",
    response_model_by_alias=True,
)
async def units_id_put(
    id: str = Path(None, description="The ID of the Unit to be retrieved"),
    user: str = Query(None, description="Username"),
    unit: Unit = Body(None, description="An old Unitto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Unit:
    """Updates an existing Unit (more information in https://w3id.org/okn/o/sd#Unit)"""
    ...


@router.post(
    "/units",
    responses={
        201: {"model": Unit, "description": "Created"},
    },
    tags=["Unit"],
    summary="Create one Unit",
    response_model_by_alias=True,
)
async def units_post(
    user: str = Query(None, description="Username"),
    unit: Unit = Body(None, description="Information about the Unitto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Unit:
    """Create a new instance of Unit (more information in https://w3id.org/okn/o/sd#Unit)"""
    ...
