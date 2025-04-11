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
from openapi_server.utils.vars import POINTBASEDGRID_TYPE_NAME, POINTBASEDGRID_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.point_based_grid import PointBasedGrid
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/pointbasedgrids",
    responses={
        200: {"model": List[PointBasedGrid], "description": "Successful response - returns an array with the instances of PointBasedGrid."},
    },
    tags=["PointBasedGrid"],
    summary="List all instances of PointBasedGrid",
    response_model_by_alias=True,
)
@cache(namespace="PointBasedGrid", expire=1800)
async def pointbasedgrids_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[PointBasedGrid]:
    """Gets a list of all instances of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)"""

    return query_manager.get_resource(

        username=username,label=label,page=page,per_page=per_page,

        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME,
        kls=PointBasedGrid
        )



@router.delete(
    "/pointbasedgrids/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["PointBasedGrid"],
    summary="Delete an existing PointBasedGrid",
    response_model_by_alias=True,
)
async def pointbasedgrids_id_delete(
    id: str = Path( description="The ID of the PointBasedGrid to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)"""

    await FastAPICache.clear(namespace="PointBasedGrid")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME,
        kls=PointBasedGrid
        )



@router.get(
    "/pointbasedgrids/{id}",
    responses={
        200: {"model": PointBasedGrid, "description": "Gets the details of a given PointBasedGrid"},
    },
    tags=["PointBasedGrid"],
    summary="Get a single PointBasedGrid by its id",
    response_model_by_alias=True,
)
@cache(namespace="PointBasedGrid", expire=1800)
async def pointbasedgrids_id_get(
    id: str = Path( description="The ID of the PointBasedGrid to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> PointBasedGrid:
    """Gets the details of a given PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME,
        kls=PointBasedGrid
        )



@router.put(
    "/pointbasedgrids/{id}",
    responses={
        200: {"model": PointBasedGrid, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["PointBasedGrid"],
    summary="Update an existing PointBasedGrid",
    response_model_by_alias=True,
)
async def pointbasedgrids_id_put(
    id: str = Path( description="The ID of the PointBasedGrid to be retrieved"),
    user: str = Query(None, description="Username"),
    point_based_grid: PointBasedGrid = Body(None, description="An old PointBasedGridto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> PointBasedGrid:
    """Updates an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)"""

    await FastAPICache.clear(namespace="PointBasedGrid")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME,
        kls=PointBasedGrid
        )



@router.post(
    "/pointbasedgrids",
    responses={
        201: {"model": PointBasedGrid, "description": "Created"},
    },
    tags=["PointBasedGrid"],
    summary="Create one PointBasedGrid",
    response_model_by_alias=True,
)
async def pointbasedgrids_post(
    user: str = Query(None, description="Username"),
    point_based_grid: PointBasedGrid = Body(None, description="Information about the PointBasedGridto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> PointBasedGrid:
    """Create a new instance of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)"""

    await FastAPICache.clear(namespace="PointBasedGrid")
    return query_manager.post_resource(

        user=user,
        body=point_based_grid,
        rdf_type_uri=POINTBASEDGRID_TYPE_URI,
        rdf_type_name=POINTBASEDGRID_TYPE_NAME,
        kls=PointBasedGrid
        )

