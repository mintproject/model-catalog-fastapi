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
from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/variablepresentations",
    responses={
        200: {"model": List[VariablePresentation], "description": "Successful response - returns an array with the instances of VariablePresentation."},
    },
    tags=["VariablePresentation"],
    summary="List all instances of VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[VariablePresentation]:
    """Gets a list of all instances of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""
    ...


@router.delete(
    "/variablepresentations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["VariablePresentation"],
    summary="Delete an existing VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_id_delete(
    id: str = Path(None, description="The ID of the VariablePresentation to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""
    ...


@router.get(
    "/variablepresentations/{id}",
    responses={
        200: {"model": VariablePresentation, "description": "Gets the details of a given VariablePresentation"},
    },
    tags=["VariablePresentation"],
    summary="Get a single VariablePresentation by its id",
    response_model_by_alias=True,
)
async def variablepresentations_id_get(
    id: str = Path(None, description="The ID of the VariablePresentation to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> VariablePresentation:
    """Gets the details of a given VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""
    ...


@router.put(
    "/variablepresentations/{id}",
    responses={
        200: {"model": VariablePresentation, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["VariablePresentation"],
    summary="Update an existing VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_id_put(
    id: str = Path(None, description="The ID of the VariablePresentation to be retrieved"),
    user: str = Query(None, description="Username"),
    variable_presentation: VariablePresentation = Body(None, description="An old VariablePresentationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> VariablePresentation:
    """Updates an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""
    ...


@router.post(
    "/variablepresentations",
    responses={
        201: {"model": VariablePresentation, "description": "Created"},
    },
    tags=["VariablePresentation"],
    summary="Create one VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_post(
    user: str = Query(None, description="Username"),
    variable_presentation: VariablePresentation = Body(None, description="Information about the VariablePresentationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> VariablePresentation:
    """Create a new instance of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""
    ...
