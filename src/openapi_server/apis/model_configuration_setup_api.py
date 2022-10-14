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
from openapi_server.models.model_configuration_setup import ModelConfigurationSetup
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/custom/modelconfigurationsetups/{id}",
    responses={
        200: {"model": ModelConfigurationSetup, "description": "Gets the details of a single instance of  ModelConfigurationSetup"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Get a ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def custom_modelconfigurationsetups_id_get(
    id: str = Path(None, description="The ID of the resource"),
    username: str = Query(None, description="Username to query"),
    custom_query_name: str = Query(&#39;custom_modelconfigurationsetups&#39;, description="Name of the custom query"),
) -> ModelConfigurationSetup:
    """Gets the details of a single instance of a ModelConfigurationSetup"""
    ...


@router.get(
    "/custom/modelconfigurationsetups/variable",
    responses={
        200: {"model": List[ModelConfigurationSetup], "description": "Gets a list of instance of ModelConfigurationSetup"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Get a list  Model",
    response_model_by_alias=True,
)
async def custom_modelconfigurationsetups_variable_get(
    label: str = Query(None, description="variable to search"),
    custom_query_name: str = Query(&#39;custom_modelconfigurationsetups_variable&#39;, description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[ModelConfigurationSetup]:
    """Get model configurations by variable name"""
    ...


@router.get(
    "/modelconfigurationsetups",
    responses={
        200: {"model": List[ModelConfigurationSetup], "description": "Successful response - returns an array with the instances of ModelConfigurationSetup."},
    },
    tags=["ModelConfigurationSetup"],
    summary="List all instances of ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def modelconfigurationsetups_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[ModelConfigurationSetup]:
    """Gets a list of all instances of ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)"""
    ...


@router.delete(
    "/modelconfigurationsetups/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Delete an existing ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def modelconfigurationsetups_id_delete(
    id: str = Path(None, description="The ID of the ModelConfigurationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)"""
    ...


@router.get(
    "/modelconfigurationsetups/{id}",
    responses={
        200: {"model": ModelConfigurationSetup, "description": "Gets the details of a given ModelConfigurationSetup"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Get a single ModelConfigurationSetup by its id",
    response_model_by_alias=True,
)
async def modelconfigurationsetups_id_get(
    id: str = Path(None, description="The ID of the ModelConfigurationSetup to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> ModelConfigurationSetup:
    """Gets the details of a given ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)"""
    ...


@router.put(
    "/modelconfigurationsetups/{id}",
    responses={
        200: {"model": ModelConfigurationSetup, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Update an existing ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def modelconfigurationsetups_id_put(
    id: str = Path(None, description="The ID of the ModelConfigurationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    model_configuration_setup: ModelConfigurationSetup = Body(None, description="An old ModelConfigurationSetupto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelConfigurationSetup:
    """Updates an existing ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)"""
    ...


@router.post(
    "/modelconfigurationsetups",
    responses={
        201: {"model": ModelConfigurationSetup, "description": "Created"},
    },
    tags=["ModelConfigurationSetup"],
    summary="Create one ModelConfigurationSetup",
    response_model_by_alias=True,
)
async def modelconfigurationsetups_post(
    user: str = Query(None, description="Username"),
    model_configuration_setup: ModelConfigurationSetup = Body(None, description="Information about the ModelConfigurationSetupto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelConfigurationSetup:
    """Create a new instance of ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)"""
    ...
