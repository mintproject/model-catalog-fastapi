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
from openapi_server.utils.vars import CONFIGURATIONSETUP_TYPE_NAME, CONFIGURATIONSETUP_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.configuration_setup import ConfigurationSetup
from openapi_server.models.model_configuration_setup import ModelConfigurationSetup
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/configurationsetups",
    responses={
        200: {"model": List[ConfigurationSetup], "description": "Successful response - returns an array with the instances of ConfigurationSetup."},
    },
    tags=["ConfigurationSetup"],
    summary="List all instances of ConfigurationSetup",
    response_model_by_alias=True,
)
async def configurationsetups_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[ConfigurationSetup]:
    """Gets a list of all instances of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        


@router.delete(
    "/configurationsetups/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["ConfigurationSetup"],
    summary="Delete an existing ConfigurationSetup",
    response_model_by_alias=True,
)
async def configurationsetups_id_delete(
    id: str = Path(None, description="The ID of the ConfigurationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        


@router.get(
    "/configurationsetups/{id}",
    responses={
        200: {"model": ConfigurationSetup, "description": "Gets the details of a given ConfigurationSetup"},
    },
    tags=["ConfigurationSetup"],
    summary="Get a single ConfigurationSetup by its id",
    response_model_by_alias=True,
)
async def configurationsetups_id_get(
    id: str = Path(None, description="The ID of the ConfigurationSetup to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> ConfigurationSetup:
    """Gets the details of a given ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        


@router.put(
    "/configurationsetups/{id}",
    responses={
        200: {"model": ConfigurationSetup, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["ConfigurationSetup"],
    summary="Update an existing ConfigurationSetup",
    response_model_by_alias=True,
)
async def configurationsetups_id_put(
    id: str = Path(None, description="The ID of the ConfigurationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    configuration_setup: ConfigurationSetup = Body(None, description="An old ConfigurationSetupto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ConfigurationSetup:
    """Updates an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        


@router.post(
    "/configurationsetups",
    responses={
        201: {"model": ConfigurationSetup, "description": "Created"},
    },
    tags=["ConfigurationSetup"],
    summary="Create one ConfigurationSetup",
    response_model_by_alias=True,
)
async def configurationsetups_post(
    user: str = Query(None, description="Username"),
    configuration_setup: ConfigurationSetup = Body(None, description="Information about the ConfigurationSetupto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ConfigurationSetup:
    """Create a new instance of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)"""
    return query_manager.post_resource(
        
        user=user,
        body=configuration_setup,
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        


@router.get(
    "/custom/configurationsetups/{id}",
    responses={
        200: {"model": ModelConfigurationSetup, "description": "Gets the details of a single instance of  ModelConfigurationSetup"},
    },
    tags=["ConfigurationSetup"],
    summary="Get a ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def custom_configurationsetups_id_get(
    id: str = Path(None, description="The ID of the resource"),
    username: str = Query(None, description="Username to query"),
    custom_query_name: str = Query("custom_configurationsetups", description="Name of the custom query"),
) -> ModelConfigurationSetup:
    """Gets the details of a single instance of a ModelConfigurationSetup"""
    return query_manager.get_resource(
        id=id,
        username=username,custom_query_name=custom_query_name,
        
        rdf_type_uri=CONFIGURATIONSETUP_TYPE_URI,
        rdf_type_name=CONFIGURATIONSETUP_TYPE_NAME, 
        kls=ConfigurationSetup
        )
        
