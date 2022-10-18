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
from openapi_server.utils.vars import PERSON_TYPE_NAME, PERSON_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.person import Person
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/persons",
    responses={
        200: {"model": List[Person], "description": "Successful response - returns an array with the instances of Person."},
    },
    tags=["Person"],
    summary="List all instances of Person",
    response_model_by_alias=True,
)
async def persons_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Person]:
    """Gets a list of all instances of Person (more information in https://w3id.org/okn/o/sd#Person)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person
        )
        


@router.delete(
    "/persons/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Person"],
    summary="Delete an existing Person",
    response_model_by_alias=True,
)
async def persons_id_delete(
    id: str = Path(None, description="The ID of the Person to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Person (more information in https://w3id.org/okn/o/sd#Person)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person
        )
        


@cache(expire=60)
@router.get(
    "/persons/{id}",
    responses={
        200: {"model": Person, "description": "Gets the details of a given Person"},
    },
    tags=["Person"],
    summary="Get a single Person by its id",
    response_model_by_alias=True,
)
async def persons_id_get(
    id: str = Path(None, description="The ID of the Person to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Person:
    """Gets the details of a given Person (more information in https://w3id.org/okn/o/sd#Person)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person
        )
        


@router.put(
    "/persons/{id}",
    responses={
        200: {"model": Person, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Person"],
    summary="Update an existing Person",
    response_model_by_alias=True,
)
async def persons_id_put(
    id: str = Path(None, description="The ID of the Person to be retrieved"),
    user: str = Query(None, description="Username"),
    person: Person = Body(None, description="An old Personto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Person:
    """Updates an existing Person (more information in https://w3id.org/okn/o/sd#Person)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person
        )
        


@router.post(
    "/persons",
    responses={
        201: {"model": Person, "description": "Created"},
    },
    tags=["Person"],
    summary="Create one Person",
    response_model_by_alias=True,
)
async def persons_post(
    user: str = Query(None, description="Username"),
    person: Person = Body(None, description="Information about the Personto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Person:
    """Create a new instance of Person (more information in https://w3id.org/okn/o/sd#Person)"""
    return query_manager.post_resource(
        
        user=user,
        body=person,
        rdf_type_uri=PERSON_TYPE_URI,
        rdf_type_name=PERSON_TYPE_NAME, 
        kls=Person
        )
        
