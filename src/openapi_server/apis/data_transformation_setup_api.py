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
from openapi_server.utils.vars import DATATRANSFORMATIONSETUP_TYPE_NAME, DATATRANSFORMATIONSETUP_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.data_transformation_setup import DataTransformationSetup
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/datatransformationsetups",
    responses={
        200: {"model": List[DataTransformationSetup], "description": "Successful response - returns an array with the instances of DataTransformationSetup."},
    },
    tags=["DataTransformationSetup"],
    summary="List all instances of DataTransformationSetup",
    response_model_by_alias=True,
)
@cache(namespace="DataTransformationSetup", expire=1800)
async def datatransformationsetups_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[DataTransformationSetup]:
    """Gets a list of all instances of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)"""

    return query_manager.get_resource(

        username=username,label=label,page=page,per_page=per_page,

        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME,
        kls=DataTransformationSetup
        )



@router.delete(
    "/datatransformationsetups/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["DataTransformationSetup"],
    summary="Delete an existing DataTransformationSetup",
    response_model_by_alias=True,
)
async def datatransformationsetups_id_delete(
    id: str = Path( description="The ID of the DataTransformationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)"""

    await FastAPICache.clear(namespace="DataTransformationSetup")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME,
        kls=DataTransformationSetup
        )



@router.get(
    "/datatransformationsetups/{id}",
    responses={
        200: {"model": DataTransformationSetup, "description": "Gets the details of a given DataTransformationSetup"},
    },
    tags=["DataTransformationSetup"],
    summary="Get a single DataTransformationSetup by its id",
    response_model_by_alias=True,
)
@cache(namespace="DataTransformationSetup", expire=1800)
async def datatransformationsetups_id_get(
    id: str = Path( description="The ID of the DataTransformationSetup to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> DataTransformationSetup:
    """Gets the details of a given DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME,
        kls=DataTransformationSetup
        )



@router.put(
    "/datatransformationsetups/{id}",
    responses={
        200: {"model": DataTransformationSetup, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["DataTransformationSetup"],
    summary="Update an existing DataTransformationSetup",
    response_model_by_alias=True,
)
async def datatransformationsetups_id_put(
    id: str = Path( description="The ID of the DataTransformationSetup to be retrieved"),
    user: str = Query(None, description="Username"),
    data_transformation_setup: DataTransformationSetup = Body(None, description="An old DataTransformationSetupto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DataTransformationSetup:
    """Updates an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)"""

    await FastAPICache.clear(namespace="DataTransformationSetup")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=data_transformation_setup,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME,
        kls=DataTransformationSetup
        )



@router.post(
    "/datatransformationsetups",
    responses={
        201: {"model": DataTransformationSetup, "description": "Created"},
    },
    tags=["DataTransformationSetup"],
    summary="Create one DataTransformationSetup",
    response_model_by_alias=True,
)
async def datatransformationsetups_post(
    user: str = Query(None, description="Username"),
    data_transformation_setup: DataTransformationSetup = Body(None, description="Information about the DataTransformationSetupto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> DataTransformationSetup:
    """Create a new instance of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)"""

    await FastAPICache.clear(namespace="DataTransformationSetup")
    return query_manager.post_resource(

        user=user,
        body=data_transformation_setup,
        rdf_type_uri=DATATRANSFORMATIONSETUP_TYPE_URI,
        rdf_type_name=DATATRANSFORMATIONSETUP_TYPE_NAME,
        kls=DataTransformationSetup
        )

