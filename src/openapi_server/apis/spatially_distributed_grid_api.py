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
from openapi_server.models.spatially_distributed_grid import SpatiallyDistributedGrid
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/spatiallydistributedgrids",
    responses={
        200: {"model": List[SpatiallyDistributedGrid], "description": "Successful response - returns an array with the instances of SpatiallyDistributedGrid."},
    },
    tags=["SpatiallyDistributedGrid"],
    summary="List all instances of SpatiallyDistributedGrid",
    response_model_by_alias=True,
)
async def spatiallydistributedgrids_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[SpatiallyDistributedGrid]:
    """Gets a list of all instances of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)"""
    ...


@router.delete(
    "/spatiallydistributedgrids/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["SpatiallyDistributedGrid"],
    summary="Delete an existing SpatiallyDistributedGrid",
    response_model_by_alias=True,
)
async def spatiallydistributedgrids_id_delete(
    id: str = Path(None, description="The ID of the SpatiallyDistributedGrid to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)"""
    ...


@router.get(
    "/spatiallydistributedgrids/{id}",
    responses={
        200: {"model": SpatiallyDistributedGrid, "description": "Gets the details of a given SpatiallyDistributedGrid"},
    },
    tags=["SpatiallyDistributedGrid"],
    summary="Get a single SpatiallyDistributedGrid by its id",
    response_model_by_alias=True,
)
async def spatiallydistributedgrids_id_get(
    id: str = Path(None, description="The ID of the SpatiallyDistributedGrid to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> SpatiallyDistributedGrid:
    """Gets the details of a given SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)"""
    ...


@router.put(
    "/spatiallydistributedgrids/{id}",
    responses={
        200: {"model": SpatiallyDistributedGrid, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["SpatiallyDistributedGrid"],
    summary="Update an existing SpatiallyDistributedGrid",
    response_model_by_alias=True,
)
async def spatiallydistributedgrids_id_put(
    id: str = Path(None, description="The ID of the SpatiallyDistributedGrid to be retrieved"),
    user: str = Query(None, description="Username"),
    spatially_distributed_grid: SpatiallyDistributedGrid = Body(None, description="An old SpatiallyDistributedGridto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SpatiallyDistributedGrid:
    """Updates an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)"""
    ...


@router.post(
    "/spatiallydistributedgrids",
    responses={
        201: {"model": SpatiallyDistributedGrid, "description": "Created"},
    },
    tags=["SpatiallyDistributedGrid"],
    summary="Create one SpatiallyDistributedGrid",
    response_model_by_alias=True,
)
async def spatiallydistributedgrids_post(
    user: str = Query(None, description="Username"),
    spatially_distributed_grid: SpatiallyDistributedGrid = Body(None, description="Information about the SpatiallyDistributedGridto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> SpatiallyDistributedGrid:
    """Create a new instance of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)"""
    ...
