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
from openapi_server.utils.vars import MODEL_TYPE_NAME, MODEL_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.model import Model
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/custom/model/index",
    responses={
        200: {"model": List[Model], "description": "Gets the details of a single instance of Model"},
    },
    tags=["Model"],
    summary="Get a Model",
    response_model_by_alias=True,
)
async def custom_model_index_get(
    label: str = Query(None, description="Label of NumericalIndex"),
    custom_query_name: str = Query("custom_model_index", description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[Model]:
    """Gets the details of a single instance of a Model"""
    return query_manager.get_resource(
        
        custom_query_name=custom_query_name,username=username,label=label,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/custom/model/intervention",
    responses={
        200: {"model": List[Model], "description": "Gets the details of a single instance of Model"},
    },
    tags=["Model"],
    summary="Get a Model",
    response_model_by_alias=True,
)
async def custom_model_intervention_get(
    label: str = Query(None, description="Label of intervation"),
    custom_query_name: str = Query("custom_model_intervetion", description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[Model]:
    """Gets the details of a single instance of a Model"""
    return query_manager.get_resource(
        
        custom_query_name=custom_query_name,username=username,label=label,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/custom/model/region",
    responses={
        200: {"model": List[Model], "description": "Gets the details of a single instance of Model"},
    },
    tags=["Model"],
    summary="Get a Model",
    response_model_by_alias=True,
)
async def custom_model_region_get(
    label: str = Query(None, description="region to search"),
    custom_query_name: str = Query("custom_model_region", description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[Model]:
    """Gets the details of a single instance of a Model"""
    return query_manager.get_resource(
        
        custom_query_name=custom_query_name,username=username,label=label,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/custom/models/standard_variable",
    responses={
        200: {"model": List[Model], "description": "Gets a list of models"},
    },
    tags=["Model"],
    summary="Get a list of models",
    response_model_by_alias=True,
)
async def custom_models_standard_variable_get(
    label: str = Query(None, description="standard variable name"),
    custom_query_name: str = Query("custom_model_standard_variable", description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[Model]:
    """Gets a list of model filter by the label of a standard variable"""
    return query_manager.get_resource(
        
        custom_query_name=custom_query_name,username=username,label=label,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/custom/models/variable",
    responses={
        200: {"model": List[Model], "description": "Gets a list of instance of Model"},
    },
    tags=["Model"],
    summary="Get a list of Model",
    response_model_by_alias=True,
)
async def custom_models_variable_get(
    label: str = Query(None, description="variable to search"),
    custom_query_name: str = Query("custom_models_variable", description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[Model]:
    """Get models by variable name"""
    return query_manager.get_resource(
        
        custom_query_name=custom_query_name,username=username,label=label,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/models",
    responses={
        200: {"model": List[Model], "description": "Successful response - returns an array with the instances of Model."},
    },
    tags=["Model"],
    summary="List all instances of Model",
    response_model_by_alias=True,
)
async def models_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Model]:
    """Gets a list of all instances of Model (more information in https://w3id.org/okn/o/sdm#Model)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@router.delete(
    "/models/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Model"],
    summary="Delete an existing Model",
    response_model_by_alias=True,
)
async def models_id_delete(
    id: str = Path(None, description="The ID of the Model to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Model (more information in https://w3id.org/okn/o/sdm#Model)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@cache(expire=60)
@router.get(
    "/models/{id}",
    responses={
        200: {"model": Model, "description": "Gets the details of a given Model"},
    },
    tags=["Model"],
    summary="Get a single Model by its id",
    response_model_by_alias=True,
)
async def models_id_get(
    id: str = Path(None, description="The ID of the Model to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Model:
    """Gets the details of a given Model (more information in https://w3id.org/okn/o/sdm#Model)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@router.put(
    "/models/{id}",
    responses={
        200: {"model": Model, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Model"],
    summary="Update an existing Model",
    response_model_by_alias=True,
)
async def models_id_put(
    id: str = Path(None, description="The ID of the Model to be retrieved"),
    user: str = Query(None, description="Username"),
    model: Model = Body(None, description="An old Modelto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Model:
    """Updates an existing Model (more information in https://w3id.org/okn/o/sdm#Model)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        


@router.post(
    "/models",
    responses={
        201: {"model": Model, "description": "Created"},
    },
    tags=["Model"],
    summary="Create one Model",
    response_model_by_alias=True,
)
async def models_post(
    user: str = Query(None, description="Username"),
    model: Model = Body(None, description="Information about the Modelto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Model:
    """Create a new instance of Model (more information in https://w3id.org/okn/o/sdm#Model)"""
    return query_manager.post_resource(
        
        user=user,
        body=model,
        rdf_type_uri=MODEL_TYPE_URI,
        rdf_type_name=MODEL_TYPE_NAME, 
        kls=Model
        )
        
