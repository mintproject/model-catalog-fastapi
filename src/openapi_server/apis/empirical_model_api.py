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
from openapi_server.utils.vars import EMPIRICALMODEL_TYPE_NAME, EMPIRICALMODEL_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.empirical_model import EmpiricalModel
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/empiricalmodels",
    responses={
        200: {"model": List[EmpiricalModel], "description": "Successful response - returns an array with the instances of EmpiricalModel."},
    },
    tags=["EmpiricalModel"],
    summary="List all instances of EmpiricalModel",
    response_model_by_alias=True,
)
async def empiricalmodels_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[EmpiricalModel]:
    """Gets a list of all instances of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel
        )
        


@router.delete(
    "/empiricalmodels/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["EmpiricalModel"],
    summary="Delete an existing EmpiricalModel",
    response_model_by_alias=True,
)
async def empiricalmodels_id_delete(
    id: str = Path(None, description="The ID of the EmpiricalModel to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel
        )
        


@cache(expire=60)
@router.get(
    "/empiricalmodels/{id}",
    responses={
        200: {"model": EmpiricalModel, "description": "Gets the details of a given EmpiricalModel"},
    },
    tags=["EmpiricalModel"],
    summary="Get a single EmpiricalModel by its id",
    response_model_by_alias=True,
)
async def empiricalmodels_id_get(
    id: str = Path(None, description="The ID of the EmpiricalModel to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> EmpiricalModel:
    """Gets the details of a given EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel
        )
        


@router.put(
    "/empiricalmodels/{id}",
    responses={
        200: {"model": EmpiricalModel, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["EmpiricalModel"],
    summary="Update an existing EmpiricalModel",
    response_model_by_alias=True,
)
async def empiricalmodels_id_put(
    id: str = Path(None, description="The ID of the EmpiricalModel to be retrieved"),
    user: str = Query(None, description="Username"),
    empirical_model: EmpiricalModel = Body(None, description="An old EmpiricalModelto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> EmpiricalModel:
    """Updates an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel
        )
        


@router.post(
    "/empiricalmodels",
    responses={
        201: {"model": EmpiricalModel, "description": "Created"},
    },
    tags=["EmpiricalModel"],
    summary="Create one EmpiricalModel",
    response_model_by_alias=True,
)
async def empiricalmodels_post(
    user: str = Query(None, description="Username"),
    empirical_model: EmpiricalModel = Body(None, description="Information about the EmpiricalModelto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> EmpiricalModel:
    """Create a new instance of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)"""
    return query_manager.post_resource(
        
        user=user,
        body=empirical_model,
        rdf_type_uri=EMPIRICALMODEL_TYPE_URI,
        rdf_type_name=EMPIRICALMODEL_TYPE_NAME, 
        kls=EmpiricalModel
        )
        
