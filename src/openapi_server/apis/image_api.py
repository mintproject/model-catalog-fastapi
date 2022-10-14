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
from openapi_server.models.image import Image
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/images",
    responses={
        200: {"model": List[Image], "description": "Successful response - returns an array with the instances of Image."},
    },
    tags=["Image"],
    summary="List all instances of Image",
    response_model_by_alias=True,
)
async def images_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Image]:
    """Gets a list of all instances of Image (more information in https://w3id.org/okn/o/sd#Image)"""
    ...


@router.delete(
    "/images/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Image"],
    summary="Delete an existing Image",
    response_model_by_alias=True,
)
async def images_id_delete(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Image (more information in https://w3id.org/okn/o/sd#Image)"""
    ...


@router.get(
    "/images/{id}",
    responses={
        200: {"model": Image, "description": "Gets the details of a given Image"},
    },
    tags=["Image"],
    summary="Get a single Image by its id",
    response_model_by_alias=True,
)
async def images_id_get(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Image:
    """Gets the details of a given Image (more information in https://w3id.org/okn/o/sd#Image)"""
    ...


@router.put(
    "/images/{id}",
    responses={
        200: {"model": Image, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Image"],
    summary="Update an existing Image",
    response_model_by_alias=True,
)
async def images_id_put(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    user: str = Query(None, description="Username"),
    image: Image = Body(None, description="An old Imageto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Image:
    """Updates an existing Image (more information in https://w3id.org/okn/o/sd#Image)"""
    ...


@router.post(
    "/images",
    responses={
        201: {"model": Image, "description": "Created"},
    },
    tags=["Image"],
    summary="Create one Image",
    response_model_by_alias=True,
)
async def images_post(
    user: str = Query(None, description="Username"),
    image: Image = Body(None, description="Information about the Imageto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Image:
    """Create a new instance of Image (more information in https://w3id.org/okn/o/sd#Image)"""
    ...
