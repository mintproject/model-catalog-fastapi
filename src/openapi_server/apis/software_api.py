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
from openapi_server.utils.vars import SOFTWARE_TYPE_NAME, SOFTWARE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.software import Software
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/softwares",
    responses={
        200: {"model": List[Software], "description": "Successful response - returns an array with the instances of Software."},
    },
    tags=["Software"],
    summary="List all instances of Software",
    response_model_by_alias=True,
)
@cache(namespace="Software", expire=1800)
async def softwares_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Software]:
    """Gets a list of all instances of Software (more information in https://w3id.org/okn/o/sd#Software)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software
        )
        


@router.delete(
    "/softwares/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Software"],
    summary="Delete an existing Software",
    response_model_by_alias=True,
)
async def softwares_id_delete(
    id: str = Path(None, description="The ID of the Software to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Software (more information in https://w3id.org/okn/o/sd#Software)"""
    
    await FastAPICache.clear(namespace="Software")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software
        )
        


@router.get(
    "/softwares/{id}",
    responses={
        200: {"model": Software, "description": "Gets the details of a given Software"},
    },
    tags=["Software"],
    summary="Get a single Software by its id",
    response_model_by_alias=True,
)
@cache(namespace="Software", expire=1800)
async def softwares_id_get(
    id: str = Path(None, description="The ID of the Software to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Software:
    """Gets the details of a given Software (more information in https://w3id.org/okn/o/sd#Software)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software
        )
        


@router.put(
    "/softwares/{id}",
    responses={
        200: {"model": Software, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Software"],
    summary="Update an existing Software",
    response_model_by_alias=True,
)
async def softwares_id_put(
    id: str = Path(None, description="The ID of the Software to be retrieved"),
    user: str = Query(None, description="Username"),
    software: Software = Body(None, description="An old Softwareto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Software:
    """Updates an existing Software (more information in https://w3id.org/okn/o/sd#Software)"""
    
    await FastAPICache.clear(namespace="Software")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software
        )
        


@router.post(
    "/softwares",
    responses={
        201: {"model": Software, "description": "Created"},
    },
    tags=["Software"],
    summary="Create one Software",
    response_model_by_alias=True,
)
async def softwares_post(
    user: str = Query(None, description="Username"),
    software: Software = Body(None, description="Information about the Softwareto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Software:
    """Create a new instance of Software (more information in https://w3id.org/okn/o/sd#Software)"""
    
    await FastAPICache.clear(namespace="Software")
    return query_manager.post_resource(
        
        user=user,
        body=software,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software
        )
        
