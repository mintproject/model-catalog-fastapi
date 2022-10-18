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
from openapi_server.utils.vars import COUPLEDMODEL_TYPE_NAME, COUPLEDMODEL_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.coupled_model import CoupledModel
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/coupledmodels",
    responses={
        200: {"model": List[CoupledModel], "description": "Successful response - returns an array with the instances of CoupledModel."},
    },
    tags=["CoupledModel"],
    summary="List all instances of CoupledModel",
    response_model_by_alias=True,
)
async def coupledmodels_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[CoupledModel]:
    """Gets a list of all instances of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel
        )
        


@router.delete(
    "/coupledmodels/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["CoupledModel"],
    summary="Delete an existing CoupledModel",
    response_model_by_alias=True,
)
async def coupledmodels_id_delete(
    id: str = Path(None, description="The ID of the CoupledModel to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel
        )
        


@router.get(
    "/coupledmodels/{id}",
    responses={
        200: {"model": CoupledModel, "description": "Gets the details of a given CoupledModel"},
    },
    tags=["CoupledModel"],
    summary="Get a single CoupledModel by its id",
    response_model_by_alias=True,
)
async def coupledmodels_id_get(
    id: str = Path(None, description="The ID of the CoupledModel to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> CoupledModel:
    """Gets the details of a given CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel
        )
        


@router.put(
    "/coupledmodels/{id}",
    responses={
        200: {"model": CoupledModel, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["CoupledModel"],
    summary="Update an existing CoupledModel",
    response_model_by_alias=True,
)
async def coupledmodels_id_put(
    id: str = Path(None, description="The ID of the CoupledModel to be retrieved"),
    user: str = Query(None, description="Username"),
    coupled_model: CoupledModel = Body(None, description="An old CoupledModelto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CoupledModel:
    """Updates an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=coupled_model,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel
        )
        


@router.post(
    "/coupledmodels",
    responses={
        201: {"model": CoupledModel, "description": "Created"},
    },
    tags=["CoupledModel"],
    summary="Create one CoupledModel",
    response_model_by_alias=True,
)
async def coupledmodels_post(
    user: str = Query(None, description="Username"),
    coupled_model: CoupledModel = Body(None, description="Information about the CoupledModelto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CoupledModel:
    """Create a new instance of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)"""
    return query_manager.post_resource(
        
        user=user,
        body=coupled_model,
        rdf_type_uri=COUPLEDMODEL_TYPE_URI,
        rdf_type_name=COUPLEDMODEL_TYPE_NAME, 
        kls=CoupledModel
        )
        
