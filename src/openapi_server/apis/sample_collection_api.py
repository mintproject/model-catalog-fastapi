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
from openapi_server.models.sample_collection import SampleCollection
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/samplecollections",
    responses={
        200: {"model": List[SampleCollection], "description": "Successful response - returns an array with the instances of SampleCollection."},
    },
    tags=["SampleCollection"],
    summary="List all instances of SampleCollection",
    response_model_by_alias=True,
)
async def samplecollections_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SampleCollection]:
    """Gets a list of all instances of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)"""
    ...


@router.delete(
    "/samplecollections/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SampleCollection"],
    summary="Delete an existing SampleCollection",
    response_model_by_alias=True,
)
async def samplecollections_id_delete(
    id: str = Path(None, description="The ID of the SampleCollection to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)"""
    ...


@router.get(
    "/samplecollections/{id}",
    responses={
        200: {"model": SampleCollection, "description": "Gets the details of a given SampleCollection"},
    },
    tags=["SampleCollection"],
    summary="Get a single SampleCollection by its id",
    response_model_by_alias=True,
)
async def samplecollections_id_get(
    id: str = Path(None, description="The ID of the SampleCollection to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SampleCollection:
    """Gets the details of a given SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)"""
    ...


@router.put(
    "/samplecollections/{id}",
    responses={
        200: {"model": SampleCollection, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SampleCollection"],
    summary="Update an existing SampleCollection",
    response_model_by_alias=True,
)
async def samplecollections_id_put(
    id: str = Path(None, description="The ID of the SampleCollection to be retrieved"),
    user: str = Query(None, description="Username"),
    sample_collection: SampleCollection = Body(None, description="An old SampleCollectionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleCollection:
    """Updates an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)"""
    ...


@router.post(
    "/samplecollections",
    responses={
        201: {"model": SampleCollection, "description": "Created"},
    },
    tags=["SampleCollection"],
    summary="Create one SampleCollection",
    response_model_by_alias=True,
)
async def samplecollections_post(
    user: str = Query(None, description="Username"),
    sample_collection: SampleCollection = Body(None, description="Information about the SampleCollectionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleCollection:
    """Create a new instance of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)"""
    ...
