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
from openapi_server.models.standard_variable import StandardVariable
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/standardvariables",
    responses={
        200: {"model": List[StandardVariable], "description": "Successful response - returns an array with the instances of StandardVariable."},
    },
    tags=["StandardVariable"],
    summary="List all instances of StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[StandardVariable]:
    """Gets a list of all instances of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""
    ...


@router.delete(
    "/standardvariables/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["StandardVariable"],
    summary="Delete an existing StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_id_delete(
    id: str = Path(None, description="The ID of the StandardVariable to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""
    ...


@router.get(
    "/standardvariables/{id}",
    responses={
        200: {"model": StandardVariable, "description": "Gets the details of a given StandardVariable"},
    },
    tags=["StandardVariable"],
    summary="Get a single StandardVariable by its id",
    response_model_by_alias=True,
)
async def standardvariables_id_get(
    id: str = Path(None, description="The ID of the StandardVariable to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> StandardVariable:
    """Gets the details of a given StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""
    ...


@router.put(
    "/standardvariables/{id}",
    responses={
        200: {"model": StandardVariable, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["StandardVariable"],
    summary="Update an existing StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_id_put(
    id: str = Path(None, description="The ID of the StandardVariable to be retrieved"),
    user: str = Query(None, description="Username"),
    standard_variable: StandardVariable = Body(None, description="An old StandardVariableto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> StandardVariable:
    """Updates an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""
    ...


@router.post(
    "/standardvariables",
    responses={
        201: {"model": StandardVariable, "description": "Created"},
    },
    tags=["StandardVariable"],
    summary="Create one StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_post(
    user: str = Query(None, description="Username"),
    standard_variable: StandardVariable = Body(None, description="Information about the StandardVariableto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> StandardVariable:
    """Create a new instance of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""
    ...
