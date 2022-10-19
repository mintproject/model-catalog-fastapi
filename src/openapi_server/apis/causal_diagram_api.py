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
from openapi_server.utils.vars import CAUSALDIAGRAM_TYPE_NAME, CAUSALDIAGRAM_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.causal_diagram import CausalDiagram
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/causaldiagrams",
    responses={
        200: {"model": List[CausalDiagram], "description": "Successful response - returns an array with the instances of CausalDiagram."},
    },
    tags=["CausalDiagram"],
    summary="List all instances of CausalDiagram",
    response_model_by_alias=True,
)
@cache(namespace="CausalDiagram", expire=1800)
async def causaldiagrams_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[CausalDiagram]:
    """Gets a list of all instances of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram
        )
        


@router.delete(
    "/causaldiagrams/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["CausalDiagram"],
    summary="Delete an existing CausalDiagram",
    response_model_by_alias=True,
)
async def causaldiagrams_id_delete(
    id: str = Path(None, description="The ID of the CausalDiagram to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)"""
    
    await FastAPICache.clear(namespace="CausalDiagram")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram
        )
        


@router.get(
    "/causaldiagrams/{id}",
    responses={
        200: {"model": CausalDiagram, "description": "Gets the details of a given CausalDiagram"},
    },
    tags=["CausalDiagram"],
    summary="Get a single CausalDiagram by its id",
    response_model_by_alias=True,
)
@cache(namespace="CausalDiagram", expire=1800)
async def causaldiagrams_id_get(
    id: str = Path(None, description="The ID of the CausalDiagram to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> CausalDiagram:
    """Gets the details of a given CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram
        )
        


@router.put(
    "/causaldiagrams/{id}",
    responses={
        200: {"model": CausalDiagram, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["CausalDiagram"],
    summary="Update an existing CausalDiagram",
    response_model_by_alias=True,
)
async def causaldiagrams_id_put(
    id: str = Path(None, description="The ID of the CausalDiagram to be retrieved"),
    user: str = Query(None, description="Username"),
    causal_diagram: CausalDiagram = Body(None, description="An old CausalDiagramto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CausalDiagram:
    """Updates an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)"""
    
    await FastAPICache.clear(namespace="CausalDiagram")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram
        )
        


@router.post(
    "/causaldiagrams",
    responses={
        201: {"model": CausalDiagram, "description": "Created"},
    },
    tags=["CausalDiagram"],
    summary="Create one CausalDiagram",
    response_model_by_alias=True,
)
async def causaldiagrams_post(
    user: str = Query(None, description="Username"),
    causal_diagram: CausalDiagram = Body(None, description="Information about the CausalDiagramto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CausalDiagram:
    """Create a new instance of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)"""
    
    await FastAPICache.clear(namespace="CausalDiagram")
    return query_manager.post_resource(
        
        user=user,
        body=causal_diagram,
        rdf_type_uri=CAUSALDIAGRAM_TYPE_URI,
        rdf_type_name=CAUSALDIAGRAM_TYPE_NAME, 
        kls=CausalDiagram
        )
        
