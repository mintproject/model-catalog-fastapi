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

from openapi_server.models.dataset_specification import DatasetSpecification
from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.parameter import Parameter
from openapi_server.models.tapis_app import FileInput, ParameterSet, TapisApp
from openapi_server.utils.vars import DATASETSPECIFICATION_TYPE_NAME, DATASETSPECIFICATION_TYPE_URI, MODELCONFIGURATION_TYPE_NAME, MODELCONFIGURATION_TYPE_URI, PARAMETER_TYPE_NAME, PARAMETER_TYPE_URI
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
    id: str = Path( description="The ID of the resource"),
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
    id: str = Path( description="The ID of the ModelConfiguration to be retrieved"),
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
    id: str = Path( description="The ID of the ModelConfiguration to be retrieved"),
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
    id: str = Path( description="The ID of the ModelConfiguration to be retrieved"),
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


@router.post(
    "/modelconfigurations/{id}/tapis/sync",
    responses={
        201: {"model": ModelConfiguration, "description": "Created"},
    },
    tags=["ModelConfiguration"],
    summary="Create one ModelConfiguration",
    response_model_by_alias=True,
)
async def modelconfigurations_tapis_sync_post(
    id: str = Path( description="The ID of the ModelConfiguration to be retrieved"),
    username: str = Query(None, description="Username"),
    tapis_app: TapisApp = Body(None, description="Information about the ModelConfigurationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelConfiguration:
    """Sync a ModelConfiguration with a Tapis App"""

    tapis_parameters = tapis_app.jobAttributes.parameterSet
    tapis_inputs = tapis_app.jobAttributes.fileInputs

    await FastAPICache.clear(namespace="ModelConfiguration")
    await FastAPICache.clear(namespace="DatasetSpecification")
    await FastAPICache.clear(namespace="Parameter")

    model_configuration = ModelConfiguration(**query_manager.get_resource(
        id=id,
        username=username,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME,
        kls=ModelConfiguration
        ))

    remove_inputs(model_configuration, username)
    remove_parameters(model_configuration, username)

    model_configuration.has_input = convert_inputs_from_tapis(tapis_inputs, username)
    model_configuration.has_parameter = convert_parameters_from_tapis(tapis_parameters, username)
    query_manager.put_resource(
        id=id,
        user=username,
        body=model_configuration,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME,
        kls=ModelConfiguration
        )
    return query_manager.get_resource(
        id=id,
        username=username,
        rdf_type_uri=MODELCONFIGURATION_TYPE_URI,
        rdf_type_name=MODELCONFIGURATION_TYPE_NAME,
        kls=ModelConfiguration
        )


def convert_inputs_from_tapis(tapis_inputs: List[FileInput], username: str) -> List[DatasetSpecification]:
    inputs = []
    for tapis_input in tapis_inputs:
        mint_input = query_manager.post_resource(
            user=username,
            body=DatasetSpecification(
                label=[tapis_input.name],
                description=[tapis_input.description] if tapis_input.description else None
            ),
            rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
            rdf_type_name=DATASETSPECIFICATION_TYPE_NAME,
            kls=DatasetSpecification
        )
        inputs.append(mint_input)
    return inputs

def convert_parameters_from_tapis(tapis_parameters: ParameterSet, username: str) -> List[Parameter]:
    parameters = []
    for tapis_parameter in tapis_parameters.appArgs:
        mint_parameter = query_manager.post_resource(
            user=username,
            body=Parameter(
                label=[tapis_parameter.name],
                description=[tapis_parameter.description] if tapis_parameter.description else None
            ),
            rdf_type_uri=PARAMETER_TYPE_URI,
            rdf_type_name=PARAMETER_TYPE_NAME,
            kls=Parameter
        )
        parameters.append(mint_parameter)
    return parameters

def remove_inputs(model_configuration: ModelConfiguration, username: str):
    if model_configuration.has_input:
        for mint_input in model_configuration.has_input:
            query_manager.delete_resource(
            id=mint_input.id,
            user=username,
            rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
            rdf_type_name=DATASETSPECIFICATION_TYPE_NAME,
            kls=DatasetSpecification
            )

def remove_parameters(model_configuration: ModelConfiguration, username: str):
    if model_configuration.has_parameter:
        for mint_parameter in model_configuration.has_parameter:
            query_manager.delete_resource(
            id=mint_parameter.id,
            user=username,
            rdf_type_uri=PARAMETER_TYPE_URI,
            rdf_type_name=PARAMETER_TYPE_NAME,
            kls=Parameter
            )
