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
from openapi_server.utils.vars import REGION_TYPE_NAME, REGION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.region import Region
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/regions",
    responses={
        200: {"model": List[Region], "description": "Successful response - returns an array with the instances of Region."},
    },
    tags=["Region"],
    summary="List all instances of Region",
    response_model_by_alias=True,
)
async def regions_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Region]:
    """Gets a list of all instances of Region (more information in https://w3id.org/okn/o/sdm#Region)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region
        )
        


@router.delete(
    "/regions/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Region"],
    summary="Delete an existing Region",
    response_model_by_alias=True,
)
async def regions_id_delete(
    id: str = Path(None, description="The ID of the Region to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Region (more information in https://w3id.org/okn/o/sdm#Region)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region
        )
        


@router.get(
    "/regions/{id}",
    responses={
        200: {"model": Region, "description": "Gets the details of a given Region"},
    },
    tags=["Region"],
    summary="Get a single Region by its id",
    response_model_by_alias=True,
)
async def regions_id_get(
    id: str = Path(None, description="The ID of the Region to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Region:
    """Gets the details of a given Region (more information in https://w3id.org/okn/o/sdm#Region)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region
        )
        


@router.put(
    "/regions/{id}",
    responses={
        200: {"model": Region, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Region"],
    summary="Update an existing Region",
    response_model_by_alias=True,
)
async def regions_id_put(
    id: str = Path(None, description="The ID of the Region to be retrieved"),
    user: str = Query(None, description="Username"),
    region: Region = Body(None, description="An old Regionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Region:
    """Updates an existing Region (more information in https://w3id.org/okn/o/sdm#Region)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region
        )
        


@router.post(
    "/regions",
    responses={
        201: {"model": Region, "description": "Created"},
    },
    tags=["Region"],
    summary="Create one Region",
    response_model_by_alias=True,
)
async def regions_post(
    user: str = Query(None, description="Username"),
    region: Region = Body(None, description="Information about the Regionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Region:
    """Create a new instance of Region (more information in https://w3id.org/okn/o/sdm#Region)"""
    return query_manager.post_resource(
        
        user=user,
        body=region,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region
        )
        
