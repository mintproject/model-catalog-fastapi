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
from openapi_server.models.geo_shape import GeoShape
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/geoshapes",
    responses={
        200: {"model": List[GeoShape], "description": "Successful response - returns an array with the instances of GeoShape."},
    },
    tags=["GeoShape"],
    summary="List all instances of GeoShape",
    response_model_by_alias=True,
)
async def geoshapes_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[GeoShape]:
    """Gets a list of all instances of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)"""
    ...


@router.delete(
    "/geoshapes/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["GeoShape"],
    summary="Delete an existing GeoShape",
    response_model_by_alias=True,
)
async def geoshapes_id_delete(
    id: str = Path(None, description="The ID of the GeoShape to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)"""
    ...


@router.get(
    "/geoshapes/{id}",
    responses={
        200: {"model": GeoShape, "description": "Gets the details of a given GeoShape"},
    },
    tags=["GeoShape"],
    summary="Get a single GeoShape by its id",
    response_model_by_alias=True,
)
async def geoshapes_id_get(
    id: str = Path(None, description="The ID of the GeoShape to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> GeoShape:
    """Gets the details of a given GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)"""
    ...


@router.put(
    "/geoshapes/{id}",
    responses={
        200: {"model": GeoShape, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["GeoShape"],
    summary="Update an existing GeoShape",
    response_model_by_alias=True,
)
async def geoshapes_id_put(
    id: str = Path(None, description="The ID of the GeoShape to be retrieved"),
    user: str = Query(None, description="Username"),
    geo_shape: GeoShape = Body(None, description="An old GeoShapeto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GeoShape:
    """Updates an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)"""
    ...


@router.post(
    "/geoshapes",
    responses={
        201: {"model": GeoShape, "description": "Created"},
    },
    tags=["GeoShape"],
    summary="Create one GeoShape",
    response_model_by_alias=True,
)
async def geoshapes_post(
    user: str = Query(None, description="Username"),
    geo_shape: GeoShape = Body(None, description="Information about the GeoShapeto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GeoShape:
    """Create a new instance of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)"""
    ...
