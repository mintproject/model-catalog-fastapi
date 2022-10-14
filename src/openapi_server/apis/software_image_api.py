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
from openapi_server.models.software_image import SoftwareImage
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/softwareimages",
    responses={
        200: {"model": List[SoftwareImage], "description": "Successful response - returns an array with the instances of SoftwareImage."},
    },
    tags=["SoftwareImage"],
    summary="List all instances of SoftwareImage",
    response_model_by_alias=True,
)
async def softwareimages_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SoftwareImage]:
    """Gets a list of all instances of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)"""
    ...


@router.delete(
    "/softwareimages/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareImage"],
    summary="Delete an existing SoftwareImage",
    response_model_by_alias=True,
)
async def softwareimages_id_delete(
    id: str = Path(None, description="The ID of the SoftwareImage to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)"""
    ...


@router.get(
    "/softwareimages/{id}",
    responses={
        200: {"model": SoftwareImage, "description": "Gets the details of a given SoftwareImage"},
    },
    tags=["SoftwareImage"],
    summary="Get a single SoftwareImage by its id",
    response_model_by_alias=True,
)
async def softwareimages_id_get(
    id: str = Path(None, description="The ID of the SoftwareImage to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SoftwareImage:
    """Gets the details of a given SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)"""
    ...


@router.put(
    "/softwareimages/{id}",
    responses={
        200: {"model": SoftwareImage, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareImage"],
    summary="Update an existing SoftwareImage",
    response_model_by_alias=True,
)
async def softwareimages_id_put(
    id: str = Path(None, description="The ID of the SoftwareImage to be retrieved"),
    user: str = Query(None, description="Username"),
    software_image: SoftwareImage = Body(None, description="An old SoftwareImageto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareImage:
    """Updates an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)"""
    ...


@router.post(
    "/softwareimages",
    responses={
        201: {"model": SoftwareImage, "description": "Created"},
    },
    tags=["SoftwareImage"],
    summary="Create one SoftwareImage",
    response_model_by_alias=True,
)
async def softwareimages_post(
    user: str = Query(None, description="Username"),
    software_image: SoftwareImage = Body(None, description="Information about the SoftwareImageto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareImage:
    """Create a new instance of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)"""
    ...
