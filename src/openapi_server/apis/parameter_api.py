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
from openapi_server.utils.vars import PARAMETER_TYPE_NAME, PARAMETER_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.parameter import Parameter
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/parameters",
    responses={
        200: {"model": List[Parameter], "description": "Successful response - returns an array with the instances of Parameter."},
    },
    tags=["Parameter"],
    summary="List all instances of Parameter",
    response_model_by_alias=True,
)
async def parameters_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Parameter]:
    """Gets a list of all instances of Parameter (more information in https://w3id.org/okn/o/sd#Parameter)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter
        )
        


@router.delete(
    "/parameters/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Parameter"],
    summary="Delete an existing Parameter",
    response_model_by_alias=True,
)
async def parameters_id_delete(
    id: str = Path(None, description="The ID of the Parameter to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter
        )
        


@router.get(
    "/parameters/{id}",
    responses={
        200: {"model": Parameter, "description": "Gets the details of a given Parameter"},
    },
    tags=["Parameter"],
    summary="Get a single Parameter by its id",
    response_model_by_alias=True,
)
async def parameters_id_get(
    id: str = Path(None, description="The ID of the Parameter to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Parameter:
    """Gets the details of a given Parameter (more information in https://w3id.org/okn/o/sd#Parameter)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter
        )
        


@router.put(
    "/parameters/{id}",
    responses={
        200: {"model": Parameter, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Parameter"],
    summary="Update an existing Parameter",
    response_model_by_alias=True,
)
async def parameters_id_put(
    id: str = Path(None, description="The ID of the Parameter to be retrieved"),
    user: str = Query(None, description="Username"),
    parameter: Parameter = Body(None, description="An old Parameterto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Parameter:
    """Updates an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter
        )
        


@router.post(
    "/parameters",
    responses={
        201: {"model": Parameter, "description": "Created"},
    },
    tags=["Parameter"],
    summary="Create one Parameter",
    response_model_by_alias=True,
)
async def parameters_post(
    user: str = Query(None, description="Username"),
    parameter: Parameter = Body(None, description="Information about the Parameterto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Parameter:
    """Create a new instance of Parameter (more information in https://w3id.org/okn/o/sd#Parameter)"""
    return query_manager.post_resource(
        
        user=user,
        body=parameter,
        rdf_type_uri=PARAMETER_TYPE_URI,
        rdf_type_name=PARAMETER_TYPE_NAME, 
        kls=Parameter
        )
        
