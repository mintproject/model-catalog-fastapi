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
from openapi_server.utils.vars import DATASETSPECIFICATION_TYPE_NAME, DATASETSPECIFICATION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.dataset_specification import DatasetSpecification
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/custom/configuration/{id}/inputs",
    responses={
        200: {"model": List[DatasetSpecification], "description": "Gets all inputs of a configuration"},
    },
    tags=["DatasetSpecification"],
    summary="Gets all inputs of a configuration",
    response_model_by_alias=True,
)
async def custom_configuration_id_inputs_get(
    id: str = Path(None, description="The ID of the resource"),
    username: str = Query(None, description="Username to query"),
    custom_query_name: str = Query("search_datasetspecification_by_configurationid", description="Name of the custom query"),
) -> List[DatasetSpecification]:
    """Gets all inputs of a configuration"""
    return query_manager.get_resource(
        id=id,
        username=username,custom_query_name=custom_query_name,
        
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@cache(expire=60)
@router.get(
    "/custom/datasetspecifications",
    responses={
        200: {"model": List[DatasetSpecification], "description": "Gets all inputs of a configuration"},
    },
    tags=["DatasetSpecification"],
    summary="Gets all inputs of a configuration",
    response_model_by_alias=True,
)
async def custom_datasetspecifications_get(
    configurationid: str = Query(None, description="The ID of the configuration"),
    username: str = Query(None, description="Username to query"),
    custom_query_name: str = Query("custom_allinputs", description="Name of the custom query"),
) -> List[DatasetSpecification]:
    """Gets all inputs of a configuration"""
    return query_manager.get_resource(
        
        username=username,configurationid=configurationid,custom_query_name=custom_query_name,
        
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@cache(expire=60)
@router.get(
    "/datasetspecifications",
    responses={
        200: {"model": List[DatasetSpecification], "description": "Successful response - returns an array with the instances of DatasetSpecification."},
    },
    tags=["DatasetSpecification"],
    summary="List all instances of DatasetSpecification",
    response_model_by_alias=True,
)
async def datasetspecifications_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[DatasetSpecification]:
    """Gets a list of all instances of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@router.delete(
    "/datasetspecifications/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["DatasetSpecification"],
    summary="Delete an existing DatasetSpecification",
    response_model_by_alias=True,
)
async def datasetspecifications_id_delete(
    id: str = Path(None, description="The ID of the DatasetSpecification to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@cache(expire=60)
@router.get(
    "/datasetspecifications/{id}",
    responses={
        200: {"model": DatasetSpecification, "description": "Gets the details of a given DatasetSpecification"},
    },
    tags=["DatasetSpecification"],
    summary="Get a single DatasetSpecification by its id",
    response_model_by_alias=True,
)
async def datasetspecifications_id_get(
    id: str = Path(None, description="The ID of the DatasetSpecification to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> DatasetSpecification:
    """Gets the details of a given DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@router.put(
    "/datasetspecifications/{id}",
    responses={
        200: {"model": DatasetSpecification, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["DatasetSpecification"],
    summary="Update an existing DatasetSpecification",
    response_model_by_alias=True,
)
async def datasetspecifications_id_put(
    id: str = Path(None, description="The ID of the DatasetSpecification to be retrieved"),
    user: str = Query(None, description="Username"),
    dataset_specification: DatasetSpecification = Body(None, description="An old DatasetSpecificationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DatasetSpecification:
    """Updates an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        


@router.post(
    "/datasetspecifications",
    responses={
        201: {"model": DatasetSpecification, "description": "Created"},
    },
    tags=["DatasetSpecification"],
    summary="Create one DatasetSpecification",
    response_model_by_alias=True,
)
async def datasetspecifications_post(
    user: str = Query(None, description="Username"),
    dataset_specification: DatasetSpecification = Body(None, description="Information about the DatasetSpecificationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DatasetSpecification:
    """Create a new instance of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)"""
    return query_manager.post_resource(
        
        user=user,
        body=dataset_specification,
        rdf_type_uri=DATASETSPECIFICATION_TYPE_URI,
        rdf_type_name=DATASETSPECIFICATION_TYPE_NAME, 
        kls=DatasetSpecification
        )
        
