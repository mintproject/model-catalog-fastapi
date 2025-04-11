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
from openapi_server.utils.vars import CONSTRAINT_TYPE_NAME, CONSTRAINT_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.constraint import Constraint
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/constraints",
    responses={
        200: {"model": List[Constraint], "description": "Successful response - returns an array with the instances of Constraint."},
    },
    tags=["Constraint"],
    summary="List all instances of Constraint",
    response_model_by_alias=True,
)
@cache(namespace="Constraint", expire=1800)
async def constraints_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Constraint]:
    """Gets a list of all instances of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""

    return query_manager.get_resource(

        username=username,label=label,page=page,per_page=per_page,

        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME,
        kls=Constraint
        )



@router.delete(
    "/constraints/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Constraint"],
    summary="Delete an existing Constraint",
    response_model_by_alias=True,
)
async def constraints_id_delete(
    id: str = Path( description="The ID of the Constraint to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""

    await FastAPICache.clear(namespace="Constraint")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME,
        kls=Constraint
        )



@router.get(
    "/constraints/{id}",
    responses={
        200: {"model": Constraint, "description": "Gets the details of a given Constraint"},
    },
    tags=["Constraint"],
    summary="Get a single Constraint by its id",
    response_model_by_alias=True,
)
@cache(namespace="Constraint", expire=1800)
async def constraints_id_get(
    id: str = Path( description="The ID of the Constraint to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Constraint:
    """Gets the details of a given Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME,
        kls=Constraint
        )



@router.put(
    "/constraints/{id}",
    responses={
        200: {"model": Constraint, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Constraint"],
    summary="Update an existing Constraint",
    response_model_by_alias=True,
)
async def constraints_id_put(
    id: str = Path( description="The ID of the Constraint to be retrieved"),
    user: str = Query(None, description="Username"),
    constraint: Constraint = Body(None, description="An old Constraintto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Constraint:
    """Updates an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""

    await FastAPICache.clear(namespace="Constraint")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=constraint,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME,
        kls=Constraint
        )



@router.post(
    "/constraints",
    responses={
        201: {"model": Constraint, "description": "Created"},
    },
    tags=["Constraint"],
    summary="Create one Constraint",
    response_model_by_alias=True,
)
async def constraints_post(
    user: str = Query(None, description="Username"),
    constraint: Constraint = Body(None, description="Information about the Constraintto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Constraint:
    """Create a new instance of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)"""

    await FastAPICache.clear(namespace="Constraint")
    return query_manager.post_resource(

        user=user,
        body=constraint,
        rdf_type_uri=CONSTRAINT_TYPE_URI,
        rdf_type_name=CONSTRAINT_TYPE_NAME,
        kls=Constraint
        )

