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
from openapi_server.models.constraint import Constraint
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/constraints",
    responses={
        200: {"model": List[Constraint], "description": "Successful response - returns an array with the instances of Constraint."},
    },
    tags=["Constraint"],
    summary="List all instances of Constraint",
    response_model_by_alias=True,
)
async def constraints_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Constraint]:
    """Gets a list of all instances of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""
    ...


@router.delete(
    "/constraints/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Constraint"],
    summary="Delete an existing Constraint",
    response_model_by_alias=True,
)
async def constraints_id_delete(
    id: str = Path(None, description="The ID of the Constraint to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""
    ...


@router.get(
    "/constraints/{id}",
    responses={
        200: {"model": Constraint, "description": "Gets the details of a given Constraint"},
    },
    tags=["Constraint"],
    summary="Get a single Constraint by its id",
    response_model_by_alias=True,
)
async def constraints_id_get(
    id: str = Path(None, description="The ID of the Constraint to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Constraint:
    """Gets the details of a given Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""
    ...


@router.put(
    "/constraints/{id}",
    responses={
        200: {"model": Constraint, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Constraint"],
    summary="Update an existing Constraint",
    response_model_by_alias=True,
)
async def constraints_id_put(
    id: str = Path(None, description="The ID of the Constraint to be retrieved"),
    user: str = Query(None, description="Username"),
    constraint: Constraint = Body(None, description="An old Constraintto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Constraint:
    """Updates an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""
    ...


@router.post(
    "/constraints",
    responses={
        201: {"model": Constraint, "description": "Created"},
    },
    tags=["Constraint"],
    summary="Create one Constraint",
    response_model_by_alias=True,
)
async def constraints_post(
    user: str = Query(None, description="Username"),
    constraint: Constraint = Body(None, description="Information about the Constraintto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Constraint:
    """Create a new instance of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""
    ...
