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
from openapi_server.models.sample_execution import SampleExecution
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/sampleexecutions",
    responses={
        200: {"model": List[SampleExecution], "description": "Successful response - returns an array with the instances of SampleExecution."},
    },
    tags=["SampleExecution"],
    summary="List all instances of SampleExecution",
    response_model_by_alias=True,
)
async def sampleexecutions_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SampleExecution]:
    """Gets a list of all instances of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)"""
    ...


@router.delete(
    "/sampleexecutions/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SampleExecution"],
    summary="Delete an existing SampleExecution",
    response_model_by_alias=True,
)
async def sampleexecutions_id_delete(
    id: str = Path(None, description="The ID of the SampleExecution to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)"""
    ...


@router.get(
    "/sampleexecutions/{id}",
    responses={
        200: {"model": SampleExecution, "description": "Gets the details of a given SampleExecution"},
    },
    tags=["SampleExecution"],
    summary="Get a single SampleExecution by its id",
    response_model_by_alias=True,
)
async def sampleexecutions_id_get(
    id: str = Path(None, description="The ID of the SampleExecution to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SampleExecution:
    """Gets the details of a given SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)"""
    ...


@router.put(
    "/sampleexecutions/{id}",
    responses={
        200: {"model": SampleExecution, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SampleExecution"],
    summary="Update an existing SampleExecution",
    response_model_by_alias=True,
)
async def sampleexecutions_id_put(
    id: str = Path(None, description="The ID of the SampleExecution to be retrieved"),
    user: str = Query(None, description="Username"),
    sample_execution: SampleExecution = Body(None, description="An old SampleExecutionto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleExecution:
    """Updates an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)"""
    ...


@router.post(
    "/sampleexecutions",
    responses={
        201: {"model": SampleExecution, "description": "Created"},
    },
    tags=["SampleExecution"],
    summary="Create one SampleExecution",
    response_model_by_alias=True,
)
async def sampleexecutions_post(
    user: str = Query(None, description="Username"),
    sample_execution: SampleExecution = Body(None, description="Information about the SampleExecutionto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SampleExecution:
    """Create a new instance of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)"""
    ...
