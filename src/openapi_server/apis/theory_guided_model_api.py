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
from openapi_server.utils.vars import THEORY_GUIDEDMODEL_TYPE_NAME, THEORY_GUIDEDMODEL_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.theory_guided_model import TheoryGuidedModel
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/theory-guidedmodels",
    responses={
        200: {"model": List[TheoryGuidedModel], "description": "Successful response - returns an array with the instances of Theory-GuidedModel."},
    },
    tags=["Theory-GuidedModel"],
    summary="List all instances of Theory-GuidedModel",
    response_model_by_alias=True,
)
@cache(namespace="Theory_GuidedModel", expire=1800)
async def theory_guidedmodels_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[TheoryGuidedModel]:
    """Gets a list of all instances of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)"""
    
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=THEORY_GUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORY_GUIDEDMODEL_TYPE_NAME, 
        kls=Theory_GuidedModel
        )
        


@router.delete(
    "/theory-guidedmodels/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Theory-GuidedModel"],
    summary="Delete an existing Theory-GuidedModel",
    response_model_by_alias=True,
)
async def theory_guidedmodels_id_delete(
    id: str = Path(None, description="The ID of the Theory-GuidedModel to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)"""
    
    await FastAPICache.clear(namespace="Theory_GuidedModel")
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=THEORY_GUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORY_GUIDEDMODEL_TYPE_NAME, 
        kls=Theory_GuidedModel
        )
        


@router.get(
    "/theory-guidedmodels/{id}",
    responses={
        200: {"model": TheoryGuidedModel, "description": "Gets the details of a given Theory-GuidedModel"},
    },
    tags=["Theory-GuidedModel"],
    summary="Get a single Theory-GuidedModel by its id",
    response_model_by_alias=True,
)
@cache(namespace="Theory_GuidedModel", expire=1800)
async def theory_guidedmodels_id_get(
    id: str = Path(None, description="The ID of the Theory-GuidedModel to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> TheoryGuidedModel:
    """Gets the details of a given Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)"""
    
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=THEORY_GUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORY_GUIDEDMODEL_TYPE_NAME, 
        kls=Theory_GuidedModel
        )
        


@router.put(
    "/theory-guidedmodels/{id}",
    responses={
        200: {"model": TheoryGuidedModel, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Theory-GuidedModel"],
    summary="Update an existing Theory-GuidedModel",
    response_model_by_alias=True,
)
async def theory_guidedmodels_id_put(
    id: str = Path(None, description="The ID of the Theory-GuidedModel to be retrieved"),
    user: str = Query(None, description="Username"),
    theory_guided_model: TheoryGuidedModel = Body(None, description="An old Theory-GuidedModelto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> TheoryGuidedModel:
    """Updates an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)"""
    
    await FastAPICache.clear(namespace="Theory_GuidedModel")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORY_GUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORY_GUIDEDMODEL_TYPE_NAME, 
        kls=Theory_GuidedModel
        )
        


@router.post(
    "/theory-guidedmodels",
    responses={
        201: {"model": TheoryGuidedModel, "description": "Created"},
    },
    tags=["Theory-GuidedModel"],
    summary="Create one Theory-GuidedModel",
    response_model_by_alias=True,
)
async def theory_guidedmodels_post(
    user: str = Query(None, description="Username"),
    theory_guided_model: TheoryGuidedModel = Body(None, description="Information about the Theory-GuidedModelto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> TheoryGuidedModel:
    """Create a new instance of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)"""
    
    await FastAPICache.clear(namespace="Theory_GuidedModel")
    return query_manager.post_resource(
        
        user=user,
        body=theory_guided_model,
        rdf_type_uri=THEORY_GUIDEDMODEL_TYPE_URI,
        rdf_type_name=THEORY_GUIDEDMODEL_TYPE_NAME, 
        kls=Theory_GuidedModel
        )
        
