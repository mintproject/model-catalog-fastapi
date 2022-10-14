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
from openapi_server.utils.vars import GEOCOORDINATES_TYPE_NAME, GEOCOORDINATES_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.geo_coordinates import GeoCoordinates
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/geocoordinatess",
    responses={
        200: {"model": List[GeoCoordinates], "description": "Successful response - returns an array with the instances of GeoCoordinates."},
    },
    tags=["GeoCoordinates"],
    summary="List all instances of GeoCoordinates",
    response_model_by_alias=True,
)
async def geocoordinatess_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[GeoCoordinates]:
    """Gets a list of all instances of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates
        )
        


@router.delete(
    "/geocoordinatess/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["GeoCoordinates"],
    summary="Delete an existing GeoCoordinates",
    response_model_by_alias=True,
)
async def geocoordinatess_id_delete(
    id: str = Path(None, description="The ID of the GeoCoordinates to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates
        )
        


@router.get(
    "/geocoordinatess/{id}",
    responses={
        200: {"model": GeoCoordinates, "description": "Gets the details of a given GeoCoordinates"},
    },
    tags=["GeoCoordinates"],
    summary="Get a single GeoCoordinates by its id",
    response_model_by_alias=True,
)
async def geocoordinatess_id_get(
    id: str = Path(None, description="The ID of the GeoCoordinates to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> GeoCoordinates:
    """Gets the details of a given GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates
        )
        


@router.put(
    "/geocoordinatess/{id}",
    responses={
        200: {"model": GeoCoordinates, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["GeoCoordinates"],
    summary="Update an existing GeoCoordinates",
    response_model_by_alias=True,
)
async def geocoordinatess_id_put(
    id: str = Path(None, description="The ID of the GeoCoordinates to be retrieved"),
    user: str = Query(None, description="Username"),
    geo_coordinates: GeoCoordinates = Body(None, description="An old GeoCoordinatesto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GeoCoordinates:
    """Updates an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates
        )
        


@router.post(
    "/geocoordinatess",
    responses={
        201: {"model": GeoCoordinates, "description": "Created"},
    },
    tags=["GeoCoordinates"],
    summary="Create one GeoCoordinates",
    response_model_by_alias=True,
)
async def geocoordinatess_post(
    user: str = Query(None, description="Username"),
    geo_coordinates: GeoCoordinates = Body(None, description="Information about the GeoCoordinatesto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GeoCoordinates:
    """Create a new instance of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)"""
    return query_manager.post_resource(
        
        user=user,
        body=geo_coordinates,
        rdf_type_uri=GEOCOORDINATES_TYPE_URI,
        rdf_type_name=GEOCOORDINATES_TYPE_NAME, 
        kls=GeoCoordinates
        )
        
