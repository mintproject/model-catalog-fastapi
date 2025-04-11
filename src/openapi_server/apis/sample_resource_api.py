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
from openapi_server.utils.vars import SAMPLERESOURCE_TYPE_NAME, SAMPLERESOURCE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.sample_resource import SampleResource
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/sampleresources",
    responses={
        200: {"model": List[SampleResource], "description": "Successful response - returns an array with the instances of SampleResource."},
    },
    tags=["SampleResource"],
    summary="List all instances of SampleResource",
    response_model_by_alias=True,
)
@cache(namespace="SampleResource", expire=1800)
async def sampleresources_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SampleResource]:
    """Gets a list of all instances of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)"""

    return query_manager.get_resource(

        username=username,label=label,page=page,per_page=per_page,

        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME,
        kls=SampleResource
        )



@router.delete(
    "/sampleresources/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SampleResource"],
    summary="Delete an existing SampleResource",
    response_model_by_alias=True,
)
async def sampleresources_id_delete(
    id: str = Path( description="The ID of the SampleResource to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)"""

    await FastAPICache.clear(namespace="SampleResource")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME,
        kls=SampleResource
        )



@router.get(
    "/sampleresources/{id}",
    responses={
        200: {"model": SampleResource, "description": "Gets the details of a given SampleResource"},
    },
    tags=["SampleResource"],
    summary="Get a single SampleResource by its id",
    response_model_by_alias=True,
)
@cache(namespace="SampleResource", expire=1800)
async def sampleresources_id_get(
    id: str = Path( description="The ID of the SampleResource to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SampleResource:
    """Gets the details of a given SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME,
        kls=SampleResource
        )



@router.put(
    "/sampleresources/{id}",
    responses={
        200: {"model": SampleResource, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SampleResource"],
    summary="Update an existing SampleResource",
    response_model_by_alias=True,
)
async def sampleresources_id_put(
    id: str = Path( description="The ID of the SampleResource to be retrieved"),
    user: str = Query(None, description="Username"),
    sample_resource: SampleResource = Body(None, description="An old SampleResourceto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleResource:
    """Updates an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)"""

    await FastAPICache.clear(namespace="SampleResource")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME,
        kls=SampleResource
        )



@router.post(
    "/sampleresources",
    responses={
        201: {"model": SampleResource, "description": "Created"},
    },
    tags=["SampleResource"],
    summary="Create one SampleResource",
    response_model_by_alias=True,
)
async def sampleresources_post(
    user: str = Query(None, description="Username"),
    sample_resource: SampleResource = Body(None, description="Information about the SampleResourceto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleResource:
    """Create a new instance of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)"""

    await FastAPICache.clear(namespace="SampleResource")
    return query_manager.post_resource(

        user=user,
        body=sample_resource,
        rdf_type_uri=SAMPLERESOURCE_TYPE_URI,
        rdf_type_name=SAMPLERESOURCE_TYPE_NAME,
        kls=SampleResource
        )

