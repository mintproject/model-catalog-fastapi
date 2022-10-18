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
from openapi_server.utils.vars import IMAGE_TYPE_NAME, IMAGE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.image import Image
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/images",
    responses={
        200: {"model": List[Image], "description": "Successful response - returns an array with the instances of Image."},
    },
    tags=["Image"],
    summary="List all instances of Image",
    response_model_by_alias=True,
)
async def images_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Image]:
    """Gets a list of all instances of Image (more information in https://w3id.org/okn/o/sd#Image)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image
        )
        


@router.delete(
    "/images/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Image"],
    summary="Delete an existing Image",
    response_model_by_alias=True,
)
async def images_id_delete(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Image (more information in https://w3id.org/okn/o/sd#Image)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image
        )
        


@cache(expire=60)
@router.get(
    "/images/{id}",
    responses={
        200: {"model": Image, "description": "Gets the details of a given Image"},
    },
    tags=["Image"],
    summary="Get a single Image by its id",
    response_model_by_alias=True,
)
async def images_id_get(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Image:
    """Gets the details of a given Image (more information in https://w3id.org/okn/o/sd#Image)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image
        )
        


@router.put(
    "/images/{id}",
    responses={
        200: {"model": Image, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Image"],
    summary="Update an existing Image",
    response_model_by_alias=True,
)
async def images_id_put(
    id: str = Path(None, description="The ID of the Image to be retrieved"),
    user: str = Query(None, description="Username"),
    image: Image = Body(None, description="An old Imageto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Image:
    """Updates an existing Image (more information in https://w3id.org/okn/o/sd#Image)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image
        )
        


@router.post(
    "/images",
    responses={
        201: {"model": Image, "description": "Created"},
    },
    tags=["Image"],
    summary="Create one Image",
    response_model_by_alias=True,
)
async def images_post(
    user: str = Query(None, description="Username"),
    image: Image = Body(None, description="Information about the Imageto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Image:
    """Create a new instance of Image (more information in https://w3id.org/okn/o/sd#Image)"""
    return query_manager.post_resource(
        
        user=user,
        body=image,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image
        )
        
