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
from openapi_server.models.software_version import SoftwareVersion
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/softwareversions",
    responses={
        200: {"model": List[SoftwareVersion], "description": "Successful response - returns an array with the instances of SoftwareVersion."},
    },
    tags=["SoftwareVersion"],
    summary="List all instances of SoftwareVersion",
    response_model_by_alias=True,
)
async def softwareversions_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SoftwareVersion]:
    """Gets a list of all instances of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)"""
    ...


@router.delete(
    "/softwareversions/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareVersion"],
    summary="Delete an existing SoftwareVersion",
    response_model_by_alias=True,
)
async def softwareversions_id_delete(
    id: str = Path(None, description="The ID of the SoftwareVersion to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)"""
    ...


@router.get(
    "/softwareversions/{id}",
    responses={
        200: {"model": SoftwareVersion, "description": "Gets the details of a given SoftwareVersion"},
    },
    tags=["SoftwareVersion"],
    summary="Get a single SoftwareVersion by its id",
    response_model_by_alias=True,
)
async def softwareversions_id_get(
    id: str = Path(None, description="The ID of the SoftwareVersion to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SoftwareVersion:
    """Gets the details of a given SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)"""
    ...


@router.put(
    "/softwareversions/{id}",
    responses={
        200: {"model": SoftwareVersion, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareVersion"],
    summary="Update an existing SoftwareVersion",
    response_model_by_alias=True,
)
async def softwareversions_id_put(
    id: str = Path(None, description="The ID of the SoftwareVersion to be retrieved"),
    user: str = Query(None, description="Username"),
    software_version: SoftwareVersion = Body(None, description="An old SoftwareVersionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareVersion:
    """Updates an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)"""
    ...


@router.post(
    "/softwareversions",
    responses={
        201: {"model": SoftwareVersion, "description": "Created"},
    },
    tags=["SoftwareVersion"],
    summary="Create one SoftwareVersion",
    response_model_by_alias=True,
)
async def softwareversions_post(
    user: str = Query(None, description="Username"),
    software_version: SoftwareVersion = Body(None, description="Information about the SoftwareVersionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareVersion:
    """Create a new instance of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)"""
    ...
