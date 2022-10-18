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
from openapi_server.utils.vars import DATATRANSFORMATION_TYPE_NAME, DATATRANSFORMATION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.data_transformation import DataTransformation
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/custom/datasetspecifications/{id}/datatransformations",
    responses={
        200: {"model": List[DataTransformation], "description": "Gets a list of data transformations filter related a dataset."},
    },
    tags=["DataTransformation"],
    summary="Gets a list of data transformations related a dataset",
    response_model_by_alias=True,
)
async def custom_datasetspecifications_id_datatransformations_get(
    id: str = Path(None, description="The ID of the dataspecification"),
    custom_query_name: str = Query(&#39;custom_datatransformations&#39;, description="Name of the custom query"),
    username: str = Query(None, description="Username to query"),
) -> List[DataTransformation]:
    """Gets a list of data transformations related a dataset"""
    return query_manager.get_resource(
        id=id,
        custom_query_name=custom_query_name,username=username,
        
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        


@cache(expire=60)
@router.get(
    "/datatransformations",
    responses={
        200: {"model": List[DataTransformation], "description": "Successful response - returns an array with the instances of DataTransformation."},
    },
    tags=["DataTransformation"],
    summary="List all instances of DataTransformation",
    response_model_by_alias=True,
)
async def datatransformations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[DataTransformation]:
    """Gets a list of all instances of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        


@router.delete(
    "/datatransformations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["DataTransformation"],
    summary="Delete an existing DataTransformation",
    response_model_by_alias=True,
)
async def datatransformations_id_delete(
    id: str = Path(None, description="The ID of the DataTransformation to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        


@cache(expire=60)
@router.get(
    "/datatransformations/{id}",
    responses={
        200: {"model": DataTransformation, "description": "Gets the details of a given DataTransformation"},
    },
    tags=["DataTransformation"],
    summary="Get a single DataTransformation by its id",
    response_model_by_alias=True,
)
async def datatransformations_id_get(
    id: str = Path(None, description="The ID of the DataTransformation to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> DataTransformation:
    """Gets the details of a given DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        


@router.put(
    "/datatransformations/{id}",
    responses={
        200: {"model": DataTransformation, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["DataTransformation"],
    summary="Update an existing DataTransformation",
    response_model_by_alias=True,
)
async def datatransformations_id_put(
    id: str = Path(None, description="The ID of the DataTransformation to be retrieved"),
    user: str = Query(None, description="Username"),
    data_transformation: DataTransformation = Body(None, description="An old DataTransformationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DataTransformation:
    """Updates an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=data_transformation,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        


@router.post(
    "/datatransformations",
    responses={
        201: {"model": DataTransformation, "description": "Created"},
    },
    tags=["DataTransformation"],
    summary="Create one DataTransformation",
    response_model_by_alias=True,
)
async def datatransformations_post(
    user: str = Query(None, description="Username"),
    data_transformation: DataTransformation = Body(None, description="Information about the DataTransformationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DataTransformation:
    """Create a new instance of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)"""
    return query_manager.post_resource(
        
        user=user,
        body=data_transformation,
        rdf_type_uri=DATATRANSFORMATION_TYPE_URI,
        rdf_type_name=DATATRANSFORMATION_TYPE_NAME, 
        kls=DataTransformation
        )
        
