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
from openapi_server.utils.vars import SOFTWARECONFIGURATION_TYPE_NAME, SOFTWARECONFIGURATION_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.software_configuration import SoftwareConfiguration
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/softwareconfigurations",
    responses={
        200: {"model": List[SoftwareConfiguration], "description": "Successful response - returns an array with the instances of SoftwareConfiguration."},
    },
    tags=["SoftwareConfiguration"],
    summary="List all instances of SoftwareConfiguration",
    response_model_by_alias=True,
)
async def softwareconfigurations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SoftwareConfiguration]:
    """Gets a list of all instances of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration
        )
        


@router.delete(
    "/softwareconfigurations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareConfiguration"],
    summary="Delete an existing SoftwareConfiguration",
    response_model_by_alias=True,
)
async def softwareconfigurations_id_delete(
    id: str = Path(None, description="The ID of the SoftwareConfiguration to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration
        )
        


@router.get(
    "/softwareconfigurations/{id}",
    responses={
        200: {"model": SoftwareConfiguration, "description": "Gets the details of a given SoftwareConfiguration"},
    },
    tags=["SoftwareConfiguration"],
    summary="Get a single SoftwareConfiguration by its id",
    response_model_by_alias=True,
)
async def softwareconfigurations_id_get(
    id: str = Path(None, description="The ID of the SoftwareConfiguration to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SoftwareConfiguration:
    """Gets the details of a given SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration
        )
        


@router.put(
    "/softwareconfigurations/{id}",
    responses={
        200: {"model": SoftwareConfiguration, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SoftwareConfiguration"],
    summary="Update an existing SoftwareConfiguration",
    response_model_by_alias=True,
)
async def softwareconfigurations_id_put(
    id: str = Path(None, description="The ID of the SoftwareConfiguration to be retrieved"),
    user: str = Query(None, description="Username"),
    software_configuration: SoftwareConfiguration = Body(None, description="An old SoftwareConfigurationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareConfiguration:
    """Updates an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration
        )
        


@router.post(
    "/softwareconfigurations",
    responses={
        201: {"model": SoftwareConfiguration, "description": "Created"},
    },
    tags=["SoftwareConfiguration"],
    summary="Create one SoftwareConfiguration",
    response_model_by_alias=True,
)
async def softwareconfigurations_post(
    user: str = Query(None, description="Username"),
    software_configuration: SoftwareConfiguration = Body(None, description="Information about the SoftwareConfigurationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SoftwareConfiguration:
    """Create a new instance of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)"""
    return query_manager.post_resource(
        
        user=user,
        body=software_configuration,
        rdf_type_uri=SOFTWARECONFIGURATION_TYPE_URI,
        rdf_type_name=SOFTWARECONFIGURATION_TYPE_NAME, 
        kls=SoftwareConfiguration
        )
        
