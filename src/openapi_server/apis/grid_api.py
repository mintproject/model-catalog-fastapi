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
from openapi_server.utils.vars import GRID_TYPE_NAME, GRID_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.grid import Grid
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/grids",
    responses={
        200: {"model": List[Grid], "description": "Successful response - returns an array with the instances of Grid."},
    },
    tags=["Grid"],
    summary="List all instances of Grid",
    response_model_by_alias=True,
)
@cache(namespace="Grid", expire=1800)
async def grids_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Grid]:
    """Gets a list of all instances of Grid (more information in https://w3id.org/okn/o/sdm#Grid)"""

    return query_manager.get_resource(

        username=username,label=label,page=page,per_page=per_page,

        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME,
        kls=Grid
        )



@router.delete(
    "/grids/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Grid"],
    summary="Delete an existing Grid",
    response_model_by_alias=True,
)
async def grids_id_delete(
    id: str = Path( description="The ID of the Grid to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid)"""

    await FastAPICache.clear(namespace="Grid")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME,
        kls=Grid
        )



@router.get(
    "/grids/{id}",
    responses={
        200: {"model": Grid, "description": "Gets the details of a given Grid"},
    },
    tags=["Grid"],
    summary="Get a single Grid by its id",
    response_model_by_alias=True,
)
@cache(namespace="Grid", expire=1800)
async def grids_id_get(
    id: str = Path( description="The ID of the Grid to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Grid:
    """Gets the details of a given Grid (more information in https://w3id.org/okn/o/sdm#Grid)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME,
        kls=Grid
        )



@router.put(
    "/grids/{id}",
    responses={
        200: {"model": Grid, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Grid"],
    summary="Update an existing Grid",
    response_model_by_alias=True,
)
async def grids_id_put(
    id: str = Path( description="The ID of the Grid to be retrieved"),
    user: str = Query(None, description="Username"),
    grid: Grid = Body(None, description="An old Gridto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Grid:
    """Updates an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid)"""

    await FastAPICache.clear(namespace="Grid")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME,
        kls=Grid
        )



@router.post(
    "/grids",
    responses={
        201: {"model": Grid, "description": "Created"},
    },
    tags=["Grid"],
    summary="Create one Grid",
    response_model_by_alias=True,
)
async def grids_post(
    user: str = Query(None, description="Username"),
    grid: Grid = Body(None, description="Information about the Gridto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Grid:
    """Create a new instance of Grid (more information in https://w3id.org/okn/o/sdm#Grid)"""

    await FastAPICache.clear(namespace="Grid")
    return query_manager.post_resource(

        user=user,
        body=grid,
        rdf_type_uri=GRID_TYPE_URI,
        rdf_type_name=GRID_TYPE_NAME,
        kls=Grid
        )

