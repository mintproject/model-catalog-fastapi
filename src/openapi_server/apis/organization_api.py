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
from openapi_server.models.organization import Organization
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/organizations",
    responses={
        200: {"model": List[Organization], "description": "Successful response - returns an array with the instances of Organization."},
    },
    tags=["Organization"],
    summary="List all instances of Organization",
    response_model_by_alias=True,
)
async def organizations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Organization]:
    """Gets a list of all instances of Organization (more information in https://w3id.org/okn/o/sd#Organization)"""
    ...


@router.delete(
    "/organizations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Organization"],
    summary="Delete an existing Organization",
    response_model_by_alias=True,
)
async def organizations_id_delete(
    id: str = Path(None, description="The ID of the Organization to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Organization (more information in https://w3id.org/okn/o/sd#Organization)"""
    ...


@router.get(
    "/organizations/{id}",
    responses={
        200: {"model": Organization, "description": "Gets the details of a given Organization"},
    },
    tags=["Organization"],
    summary="Get a single Organization by its id",
    response_model_by_alias=True,
)
async def organizations_id_get(
    id: str = Path(None, description="The ID of the Organization to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Organization:
    """Gets the details of a given Organization (more information in https://w3id.org/okn/o/sd#Organization)"""
    ...


@router.put(
    "/organizations/{id}",
    responses={
        200: {"model": Organization, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Organization"],
    summary="Update an existing Organization",
    response_model_by_alias=True,
)
async def organizations_id_put(
    id: str = Path(None, description="The ID of the Organization to be retrieved"),
    user: str = Query(None, description="Username"),
    organization: Organization = Body(None, description="An old Organizationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Organization:
    """Updates an existing Organization (more information in https://w3id.org/okn/o/sd#Organization)"""
    ...


@router.post(
    "/organizations",
    responses={
        201: {"model": Organization, "description": "Created"},
    },
    tags=["Organization"],
    summary="Create one Organization",
    response_model_by_alias=True,
)
async def organizations_post(
    user: str = Query(None, description="Username"),
    organization: Organization = Body(None, description="Information about the Organizationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Organization:
    """Create a new instance of Organization (more information in https://w3id.org/okn/o/sd#Organization)"""
    ...
