# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi_cache import FastAPICache
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
from openapi_server.utils.vars import SPATIALRESOLUTION_TYPE_NAME, SPATIALRESOLUTION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.spatial_resolution import SpatialResolution
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/spatialresolutions",
    responses={
        200: {"model": List[SpatialResolution], "description": "Successful response - returns an array with the instances of SpatialResolution."},
    },
    tags=["SpatialResolution"],
    summary="List all instances of SpatialResolution",
    response_model_by_alias=True,
)
@cache(namespace="SpatialResolution", expire=1800)
async def spatialresolutions_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SpatialResolution]:
    """Gets a list of all instances of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution
        )
        


@router.delete(
    "/spatialresolutions/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SpatialResolution"],
    summary="Delete an existing SpatialResolution",
    response_model_by_alias=True,
)
async def spatialresolutions_id_delete(
    id: str = Path(None, description="The ID of the SpatialResolution to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)"""
    
    await FastAPICache.clear(namespace="SpatialResolution")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution
        )
        


@router.get(
    "/spatialresolutions/{id}",
    responses={
        200: {"model": SpatialResolution, "description": "Gets the details of a given SpatialResolution"},
    },
    tags=["SpatialResolution"],
    summary="Get a single SpatialResolution by its id",
    response_model_by_alias=True,
)
@cache(namespace="SpatialResolution", expire=1800)
async def spatialresolutions_id_get(
    id: str = Path(None, description="The ID of the SpatialResolution to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SpatialResolution:
    """Gets the details of a given SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution
        )
        


@router.put(
    "/spatialresolutions/{id}",
    responses={
        200: {"model": SpatialResolution, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SpatialResolution"],
    summary="Update an existing SpatialResolution",
    response_model_by_alias=True,
)
async def spatialresolutions_id_put(
    id: str = Path(None, description="The ID of the SpatialResolution to be retrieved"),
    user: str = Query(None, description="Username"),
    spatial_resolution: SpatialResolution = Body(None, description="An old SpatialResolutionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SpatialResolution:
    """Updates an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)"""
    
    await FastAPICache.clear(namespace="SpatialResolution")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution
        )
        


@router.post(
    "/spatialresolutions",
    responses={
        201: {"model": SpatialResolution, "description": "Created"},
    },
    tags=["SpatialResolution"],
    summary="Create one SpatialResolution",
    response_model_by_alias=True,
)
async def spatialresolutions_post(
    user: str = Query(None, description="Username"),
    spatial_resolution: SpatialResolution = Body(None, description="Information about the SpatialResolutionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SpatialResolution:
    """Create a new instance of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)"""
    
    await FastAPICache.clear(namespace="SpatialResolution")
    return query_manager.post_resource(
        
        user=user,
        body=spatial_resolution,
        rdf_type_uri=SPATIALRESOLUTION_TYPE_URI,
        rdf_type_name=SPATIALRESOLUTION_TYPE_NAME, 
        kls=SpatialResolution
        )
        
