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
from openapi_server.utils.vars import MODELCONFIGURATION_TYPE_NAME, MODELCONFIGURATION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.model_configuration import ModelConfiguration
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/custom/modelconfigurations/{id}",
    responses={
        200: {"model": ModelConfiguration, "description": "Gets the details of a single instance of ModelConfiguration"},
    },
    tags=["ModelConfiguration"],
    summary="Get a ModelConfiguration",
    response_model_by_alias=True,
)
@cache(namespace="ModelConfiguration", expire=1800)
async def custom_modelconfigurations_id_get(
    id: str = Path(None, description="The ID of the resource"),
    username: str = Query(None, description="Username to query"),
    custom_query_name: str = Query("custom_modelconfigurations", description="Name of the custom query"),
) -> ModelConfiguration:
    """Gets the details of a single instance of a ModelConfiguration"""
    
    return query_manager.get_resource(
        id=id,
        username=username,custom_query_name=custom_query_name,
        
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        


@router.get(
    "/modelconfigurations",
    responses={
        200: {"model": List[ModelConfiguration], "description": "Successful response - returns an array with the instances of ModelConfiguration."},
    },
    tags=["ModelConfiguration"],
    summary="List all instances of ModelConfiguration",
    response_model_by_alias=True,
)
@cache(namespace="ModelConfiguration", expire=1800)
async def modelconfigurations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[ModelConfiguration]:
    """Gets a list of all instances of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        


@router.delete(
    "/modelconfigurations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["ModelConfiguration"],
    summary="Delete an existing ModelConfiguration",
    response_model_by_alias=True,
)
async def modelconfigurations_id_delete(
    id: str = Path(None, description="The ID of the ModelConfiguration to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)"""
    
    await FastAPICache.clear(namespace="ModelConfiguration")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        


@router.get(
    "/modelconfigurations/{id}",
    responses={
        200: {"model": ModelConfiguration, "description": "Gets the details of a given ModelConfiguration"},
    },
    tags=["ModelConfiguration"],
    summary="Get a single ModelConfiguration by its id",
    response_model_by_alias=True,
)
@cache(namespace="ModelConfiguration", expire=1800)
async def modelconfigurations_id_get(
    id: str = Path(None, description="The ID of the ModelConfiguration to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> ModelConfiguration:
    """Gets the details of a given ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        


@router.put(
    "/modelconfigurations/{id}",
    responses={
        200: {"model": ModelConfiguration, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["ModelConfiguration"],
    summary="Update an existing ModelConfiguration",
    response_model_by_alias=True,
)
async def modelconfigurations_id_put(
    id: str = Path(None, description="The ID of the ModelConfiguration to be retrieved"),
    user: str = Query(None, description="Username"),
    model_configuration: ModelConfiguration = Body(None, description="An old ModelConfigurationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelConfiguration:
    """Updates an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)"""
    
    await FastAPICache.clear(namespace="ModelConfiguration")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        


@router.post(
    "/modelconfigurations",
    responses={
        201: {"model": ModelConfiguration, "description": "Created"},
    },
    tags=["ModelConfiguration"],
    summary="Create one ModelConfiguration",
    response_model_by_alias=True,
)
async def modelconfigurations_post(
    user: str = Query(None, description="Username"),
    model_configuration: ModelConfiguration = Body(None, description="Information about the ModelConfigurationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelConfiguration:
    """Create a new instance of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)"""
    
    await FastAPICache.clear(namespace="ModelConfiguration")
    return query_manager.post_resource(
        
        user=user,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME, 
        kls=ModelConfiguration
        )
        
