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
from openapi_server.utils.vars import VARIABLE_TYPE_NAME, VARIABLE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.variable import Variable
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/variables",
    responses={
        200: {"model": List[Variable], "description": "Successful response - returns an array with the instances of Variable."},
    },
    tags=["Variable"],
    summary="List all instances of Variable",
    response_model_by_alias=True,
)
async def variables_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Variable]:
    """Gets a list of all instances of Variable (more information in https://w3id.org/okn/o/sd#Variable)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable
        )
        


@router.delete(
    "/variables/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Variable"],
    summary="Delete an existing Variable",
    response_model_by_alias=True,
)
async def variables_id_delete(
    id: str = Path(None, description="The ID of the Variable to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Variable (more information in https://w3id.org/okn/o/sd#Variable)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable
        )
        


@cache(expire=60)
@router.get(
    "/variables/{id}",
    responses={
        200: {"model": Variable, "description": "Gets the details of a given Variable"},
    },
    tags=["Variable"],
    summary="Get a single Variable by its id",
    response_model_by_alias=True,
)
async def variables_id_get(
    id: str = Path(None, description="The ID of the Variable to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Variable:
    """Gets the details of a given Variable (more information in https://w3id.org/okn/o/sd#Variable)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable
        )
        


@router.put(
    "/variables/{id}",
    responses={
        200: {"model": Variable, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Variable"],
    summary="Update an existing Variable",
    response_model_by_alias=True,
)
async def variables_id_put(
    id: str = Path(None, description="The ID of the Variable to be retrieved"),
    user: str = Query(None, description="Username"),
    variable: Variable = Body(None, description="An old Variableto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Variable:
    """Updates an existing Variable (more information in https://w3id.org/okn/o/sd#Variable)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable
        )
        


@router.post(
    "/variables",
    responses={
        201: {"model": Variable, "description": "Created"},
    },
    tags=["Variable"],
    summary="Create one Variable",
    response_model_by_alias=True,
)
async def variables_post(
    user: str = Query(None, description="Username"),
    variable: Variable = Body(None, description="Information about the Variableto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Variable:
    """Create a new instance of Variable (more information in https://w3id.org/okn/o/sd#Variable)"""
    return query_manager.post_resource(
        
        user=user,
        body=variable,
        rdf_type_uri=VARIABLE_TYPE_URI,
        rdf_type_name=VARIABLE_TYPE_NAME, 
        kls=Variable
        )
        
