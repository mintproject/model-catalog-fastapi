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
from openapi_server.utils.vars import SOURCECODE_TYPE_NAME, SOURCECODE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.source_code import SourceCode
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/sourcecodes",
    responses={
        200: {"model": List[SourceCode], "description": "Successful response - returns an array with the instances of SourceCode."},
    },
    tags=["SourceCode"],
    summary="List all instances of SourceCode",
    response_model_by_alias=True,
)
async def sourcecodes_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SourceCode]:
    """Gets a list of all instances of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode
        )
        


@router.delete(
    "/sourcecodes/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SourceCode"],
    summary="Delete an existing SourceCode",
    response_model_by_alias=True,
)
async def sourcecodes_id_delete(
    id: str = Path(None, description="The ID of the SourceCode to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode
        )
        


@router.get(
    "/sourcecodes/{id}",
    responses={
        200: {"model": SourceCode, "description": "Gets the details of a given SourceCode"},
    },
    tags=["SourceCode"],
    summary="Get a single SourceCode by its id",
    response_model_by_alias=True,
)
async def sourcecodes_id_get(
    id: str = Path(None, description="The ID of the SourceCode to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SourceCode:
    """Gets the details of a given SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode
        )
        


@router.put(
    "/sourcecodes/{id}",
    responses={
        200: {"model": SourceCode, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SourceCode"],
    summary="Update an existing SourceCode",
    response_model_by_alias=True,
)
async def sourcecodes_id_put(
    id: str = Path(None, description="The ID of the SourceCode to be retrieved"),
    user: str = Query(None, description="Username"),
    source_code: SourceCode = Body(None, description="An old SourceCodeto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SourceCode:
    """Updates an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode
        )
        


@router.post(
    "/sourcecodes",
    responses={
        201: {"model": SourceCode, "description": "Created"},
    },
    tags=["SourceCode"],
    summary="Create one SourceCode",
    response_model_by_alias=True,
)
async def sourcecodes_post(
    user: str = Query(None, description="Username"),
    source_code: SourceCode = Body(None, description="Information about the SourceCodeto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SourceCode:
    """Create a new instance of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)"""
    return query_manager.post_resource(
        
        user=user,
        body=source_code,
        rdf_type_uri=SOURCECODE_TYPE_URI,
        rdf_type_name=SOURCECODE_TYPE_NAME, 
        kls=SourceCode
        )
        
