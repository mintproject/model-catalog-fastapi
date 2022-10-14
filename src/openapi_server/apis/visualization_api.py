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
from openapi_server.utils.vars import VISUALIZATION_TYPE_NAME, VISUALIZATION_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.visualization import Visualization
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/visualizations",
    responses={
        200: {"model": List[Visualization], "description": "Successful response - returns an array with the instances of Visualization."},
    },
    tags=["Visualization"],
    summary="List all instances of Visualization",
    response_model_by_alias=True,
)
async def visualizations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Visualization]:
    """Gets a list of all instances of Visualization (more information in https://w3id.org/okn/o/sd#Visualization)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization
        )
        


@router.delete(
    "/visualizations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Visualization"],
    summary="Delete an existing Visualization",
    response_model_by_alias=True,
)
async def visualizations_id_delete(
    id: str = Path(None, description="The ID of the Visualization to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization
        )
        


@router.get(
    "/visualizations/{id}",
    responses={
        200: {"model": Visualization, "description": "Gets the details of a given Visualization"},
    },
    tags=["Visualization"],
    summary="Get a single Visualization by its id",
    response_model_by_alias=True,
)
async def visualizations_id_get(
    id: str = Path(None, description="The ID of the Visualization to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Visualization:
    """Gets the details of a given Visualization (more information in https://w3id.org/okn/o/sd#Visualization)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization
        )
        


@router.put(
    "/visualizations/{id}",
    responses={
        200: {"model": Visualization, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Visualization"],
    summary="Update an existing Visualization",
    response_model_by_alias=True,
)
async def visualizations_id_put(
    id: str = Path(None, description="The ID of the Visualization to be retrieved"),
    user: str = Query(None, description="Username"),
    visualization: Visualization = Body(None, description="An old Visualizationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Visualization:
    """Updates an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization
        )
        


@router.post(
    "/visualizations",
    responses={
        201: {"model": Visualization, "description": "Created"},
    },
    tags=["Visualization"],
    summary="Create one Visualization",
    response_model_by_alias=True,
)
async def visualizations_post(
    user: str = Query(None, description="Username"),
    visualization: Visualization = Body(None, description="Information about the Visualizationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Visualization:
    """Create a new instance of Visualization (more information in https://w3id.org/okn/o/sd#Visualization)"""
    return query_manager.post_resource(
        
        user=user,
        body=visualization,
        rdf_type_uri=VISUALIZATION_TYPE_URI,
        rdf_type_name=VISUALIZATION_TYPE_NAME, 
        kls=Visualization
        )
        
