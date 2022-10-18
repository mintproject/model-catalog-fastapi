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
from openapi_server.utils.vars import EMULATOR_TYPE_NAME, EMULATOR_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.emulator import Emulator
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@cache(expire=60)
@router.get(
    "/emulators",
    responses={
        200: {"model": List[Emulator], "description": "Successful response - returns an array with the instances of Emulator."},
    },
    tags=["Emulator"],
    summary="List all instances of Emulator",
    response_model_by_alias=True,
)
async def emulators_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[Emulator]:
    """Gets a list of all instances of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)"""
    return query_manager.get_resource(
        
        username=username,label=label,page=page,per_page=per_page,
        
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator
        )
        


@router.delete(
    "/emulators/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["Emulator"],
    summary="Delete an existing Emulator",
    response_model_by_alias=True,
)
async def emulators_id_delete(
    id: str = Path(None, description="The ID of the Emulator to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)"""
    return query_manager.delete_resource(
        id=id,
        user=user,
        
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator
        )
        


@cache(expire=60)
@router.get(
    "/emulators/{id}",
    responses={
        200: {"model": Emulator, "description": "Gets the details of a given Emulator"},
    },
    tags=["Emulator"],
    summary="Get a single Emulator by its id",
    response_model_by_alias=True,
)
async def emulators_id_get(
    id: str = Path(None, description="The ID of the Emulator to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> Emulator:
    """Gets the details of a given Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)"""
    return query_manager.get_resource(
        id=id,
        username=username,
        
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator
        )
        


@router.put(
    "/emulators/{id}",
    responses={
        200: {"model": Emulator, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["Emulator"],
    summary="Update an existing Emulator",
    response_model_by_alias=True,
)
async def emulators_id_put(
    id: str = Path(None, description="The ID of the Emulator to be retrieved"),
    user: str = Query(None, description="Username"),
    emulator: Emulator = Body(None, description="An old Emulatorto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Emulator:
    """Updates an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)"""
    return query_manager.put_resource(
        id=id,
        user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator
        )
        


@router.post(
    "/emulators",
    responses={
        201: {"model": Emulator, "description": "Created"},
    },
    tags=["Emulator"],
    summary="Create one Emulator",
    response_model_by_alias=True,
)
async def emulators_post(
    user: str = Query(None, description="Username"),
    emulator: Emulator = Body(None, description="Information about the Emulatorto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> Emulator:
    """Create a new instance of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)"""
    return query_manager.post_resource(
        
        user=user,
        body=emulator,
        rdf_type_uri=EMULATOR_TYPE_URI,
        rdf_type_name=EMULATOR_TYPE_NAME, 
        kls=Emulator
        )
        
