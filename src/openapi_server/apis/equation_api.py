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
from openapi_server.utils.vars import EQUATION_TYPE_NAME, EQUATION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.equation import Equation
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/equations",
    responses={
        200: {"model": List[Equation], "description": "Successful response - returns an array with the instances of Equation."},
    },
    tags=["Equation"],
    summary="List all instances of Equation",
    response_model_by_alias=True,
)
async def equations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Equation]:
    """Gets a list of all instances of Equation (more information in https://w3id.org/okn/o/sdm#Equation)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation
        )
        


@router.delete(
    "/equations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Equation"],
    summary="Delete an existing Equation",
    response_model_by_alias=True,
)
async def equations_id_delete(
    id: str = Path(None, description="The ID of the Equation to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation
        )
        


@router.get(
    "/equations/{id}",
    responses={
        200: {"model": Equation, "description": "Gets the details of a given Equation"},
    },
    tags=["Equation"],
    summary="Get a single Equation by its id",
    response_model_by_alias=True,
)
async def equations_id_get(
    id: str = Path(None, description="The ID of the Equation to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Equation:
    """Gets the details of a given Equation (more information in https://w3id.org/okn/o/sdm#Equation)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation
        )
        


@router.put(
    "/equations/{id}",
    responses={
        200: {"model": Equation, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Equation"],
    summary="Update an existing Equation",
    response_model_by_alias=True,
)
async def equations_id_put(
    id: str = Path(None, description="The ID of the Equation to be retrieved"),
    user: str = Query(None, description="Username"),
    equation: Equation = Body(None, description="An old Equationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Equation:
    """Updates an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation
        )
        


@router.post(
    "/equations",
    responses={
        201: {"model": Equation, "description": "Created"},
    },
    tags=["Equation"],
    summary="Create one Equation",
    response_model_by_alias=True,
)
async def equations_post(
    user: str = Query(None, description="Username"),
    equation: Equation = Body(None, description="Information about the Equationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Equation:
    """Create a new instance of Equation (more information in https://w3id.org/okn/o/sdm#Equation)"""
    return query_manager.post_resource(
        
        user=user,
        body=equation,
        rdf_type_uri=EQUATION_TYPE_URI,
        rdf_type_name=EQUATION_TYPE_NAME, 
        kls=Equation
        )
        
