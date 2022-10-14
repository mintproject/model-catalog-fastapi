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
from openapi_server.utils.vars import CATALOGIDENTIFIER_TYPE_NAME, CATALOGIDENTIFIER_TYPE_URI
from openapi_server.connector import query_manager

from openapi_server.models.catalog_identifier import CatalogIdentifier
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/catalogidentifiers",
    responses={
        200: {"model": List[CatalogIdentifier], "description": "Successful response - returns an array with the instances of CatalogIdentifier."},
    },
    tags=["CatalogIdentifier"],
    summary="List all instances of CatalogIdentifier",
    response_model_by_alias=True,
)
async def catalogidentifiers_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[CatalogIdentifier]:
    """Gets a list of all instances of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier
        )
        


@router.delete(
    "/catalogidentifiers/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["CatalogIdentifier"],
    summary="Delete an existing CatalogIdentifier",
    response_model_by_alias=True,
)
async def catalogidentifiers_id_delete(
    id: str = Path(None, description="The ID of the CatalogIdentifier to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier
        )
        


@router.get(
    "/catalogidentifiers/{id}",
    responses={
        200: {"model": CatalogIdentifier, "description": "Gets the details of a given CatalogIdentifier"},
    },
    tags=["CatalogIdentifier"],
    summary="Get a single CatalogIdentifier by its id",
    response_model_by_alias=True,
)
async def catalogidentifiers_id_get(
    id: str = Path(None, description="The ID of the CatalogIdentifier to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> CatalogIdentifier:
    """Gets the details of a given CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier
        )
        


@router.put(
    "/catalogidentifiers/{id}",
    responses={
        200: {"model": CatalogIdentifier, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["CatalogIdentifier"],
    summary="Update an existing CatalogIdentifier",
    response_model_by_alias=True,
)
async def catalogidentifiers_id_put(
    id: str = Path(None, description="The ID of the CatalogIdentifier to be retrieved"),
    user: str = Query(None, description="Username"),
    catalog_identifier: CatalogIdentifier = Body(None, description="An old CatalogIdentifierto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CatalogIdentifier:
    """Updates an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=catalog_identifier,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier
        )
        


@router.post(
    "/catalogidentifiers",
    responses={
        201: {"model": CatalogIdentifier, "description": "Created"},
    },
    tags=["CatalogIdentifier"],
    summary="Create one CatalogIdentifier",
    response_model_by_alias=True,
)
async def catalogidentifiers_post(
    user: str = Query(None, description="Username"),
    catalog_identifier: CatalogIdentifier = Body(None, description="Information about the CatalogIdentifierto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> CatalogIdentifier:
    """Create a new instance of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)"""
    return query_manager.post_resource(
        
        user=user,
        body=catalog_identifier,
        rdf_type_uri=CATALOGIDENTIFIER_TYPE_URI,
        rdf_type_name=CATALOGIDENTIFIER_TYPE_NAME, 
        kls=CatalogIdentifier
        )
        
