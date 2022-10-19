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
from openapi_server.utils.vars import INTERVENTION_TYPE_NAME, INTERVENTION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.intervention import Intervention
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/interventions",
    responses={
        200: {"model": List[Intervention], "description": "Successful response - returns an array with the instances of Intervention."},
    },
    tags=["Intervention"],
    summary="List all instances of Intervention",
    response_model_by_alias=True,
)
@cache(namespace="Intervention", expire=1800)
async def interventions_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Intervention]:
    """Gets a list of all instances of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention
        )
        


@router.delete(
    "/interventions/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Intervention"],
    summary="Delete an existing Intervention",
    response_model_by_alias=True,
)
async def interventions_id_delete(
    id: str = Path(None, description="The ID of the Intervention to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)"""
    
    await FastAPICache.clear(namespace="Intervention")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention
        )
        


@router.get(
    "/interventions/{id}",
    responses={
        200: {"model": Intervention, "description": "Gets the details of a given Intervention"},
    },
    tags=["Intervention"],
    summary="Get a single Intervention by its id",
    response_model_by_alias=True,
)
@cache(namespace="Intervention", expire=1800)
async def interventions_id_get(
    id: str = Path(None, description="The ID of the Intervention to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Intervention:
    """Gets the details of a given Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention
        )
        


@router.put(
    "/interventions/{id}",
    responses={
        200: {"model": Intervention, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Intervention"],
    summary="Update an existing Intervention",
    response_model_by_alias=True,
)
async def interventions_id_put(
    id: str = Path(None, description="The ID of the Intervention to be retrieved"),
    user: str = Query(None, description="Username"),
    intervention: Intervention = Body(None, description="An old Interventionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Intervention:
    """Updates an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)"""
    
    await FastAPICache.clear(namespace="Intervention")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention
        )
        


@router.post(
    "/interventions",
    responses={
        201: {"model": Intervention, "description": "Created"},
    },
    tags=["Intervention"],
    summary="Create one Intervention",
    response_model_by_alias=True,
)
async def interventions_post(
    user: str = Query(None, description="Username"),
    intervention: Intervention = Body(None, description="Information about the Interventionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Intervention:
    """Create a new instance of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)"""
    
    await FastAPICache.clear(namespace="Intervention")
    return query_manager.post_resource(
        
        user=user,
        body=intervention,
        rdf_type_uri=INTERVENTION_TYPE_URI,
        rdf_type_name=INTERVENTION_TYPE_NAME, 
        kls=Intervention
        )
        
