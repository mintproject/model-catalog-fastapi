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
from openapi_server.utils.vars import NUMERICALINDEX_TYPE_NAME, NUMERICALINDEX_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.numerical_index import NumericalIndex
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/numericalindexs",
    responses={
        200: {"model": List[NumericalIndex], "description": "Successful response - returns an array with the instances of NumericalIndex."},
    },
    tags=["NumericalIndex"],
    summary="List all instances of NumericalIndex",
    response_model_by_alias=True,
)
async def numericalindexs_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[NumericalIndex]:
    """Gets a list of all instances of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex
        )
        


@router.delete(
    "/numericalindexs/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["NumericalIndex"],
    summary="Delete an existing NumericalIndex",
    response_model_by_alias=True,
)
async def numericalindexs_id_delete(
    id: str = Path(None, description="The ID of the NumericalIndex to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex
        )
        


@router.get(
    "/numericalindexs/{id}",
    responses={
        200: {"model": NumericalIndex, "description": "Gets the details of a given NumericalIndex"},
    },
    tags=["NumericalIndex"],
    summary="Get a single NumericalIndex by its id",
    response_model_by_alias=True,
)
async def numericalindexs_id_get(
    id: str = Path(None, description="The ID of the NumericalIndex to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> NumericalIndex:
    """Gets the details of a given NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex
        )
        


@router.put(
    "/numericalindexs/{id}",
    responses={
        200: {"model": NumericalIndex, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["NumericalIndex"],
    summary="Update an existing NumericalIndex",
    response_model_by_alias=True,
)
async def numericalindexs_id_put(
    id: str = Path(None, description="The ID of the NumericalIndex to be retrieved"),
    user: str = Query(None, description="Username"),
    numerical_index: NumericalIndex = Body(None, description="An old NumericalIndexto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> NumericalIndex:
    """Updates an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex
        )
        


@router.post(
    "/numericalindexs",
    responses={
        201: {"model": NumericalIndex, "description": "Created"},
    },
    tags=["NumericalIndex"],
    summary="Create one NumericalIndex",
    response_model_by_alias=True,
)
async def numericalindexs_post(
    user: str = Query(None, description="Username"),
    numerical_index: NumericalIndex = Body(None, description="Information about the NumericalIndexto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> NumericalIndex:
    """Create a new instance of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)"""
    return query_manager.post_resource(
        
        user=user,
        body=numerical_index,
        rdf_type_uri=NUMERICALINDEX_TYPE_URI,
        rdf_type_name=NUMERICALINDEX_TYPE_NAME, 
        kls=NumericalIndex
        )
        
