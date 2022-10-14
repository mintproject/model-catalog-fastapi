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
from openapi_server.models.model_category import ModelCategory
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/modelcategorys",
    responses={
        200: {"model": List[ModelCategory], "description": "Successful response - returns an array with the instances of ModelCategory."},
    },
    tags=["ModelCategory"],
    summary="List all instances of ModelCategory",
    response_model_by_alias=True,
)
async def modelcategorys_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[ModelCategory]:
    """Gets a list of all instances of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)"""
    ...


@router.delete(
    "/modelcategorys/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["ModelCategory"],
    summary="Delete an existing ModelCategory",
    response_model_by_alias=True,
)
async def modelcategorys_id_delete(
    id: str = Path(None, description="The ID of the ModelCategory to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)"""
    ...


@router.get(
    "/modelcategorys/{id}",
    responses={
        200: {"model": ModelCategory, "description": "Gets the details of a given ModelCategory"},
    },
    tags=["ModelCategory"],
    summary="Get a single ModelCategory by its id",
    response_model_by_alias=True,
)
async def modelcategorys_id_get(
    id: str = Path(None, description="The ID of the ModelCategory to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> ModelCategory:
    """Gets the details of a given ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)"""
    ...


@router.put(
    "/modelcategorys/{id}",
    responses={
        200: {"model": ModelCategory, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["ModelCategory"],
    summary="Update an existing ModelCategory",
    response_model_by_alias=True,
)
async def modelcategorys_id_put(
    id: str = Path(None, description="The ID of the ModelCategory to be retrieved"),
    user: str = Query(None, description="Username"),
    model_category: ModelCategory = Body(None, description="An old ModelCategoryto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelCategory:
    """Updates an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)"""
    ...


@router.post(
    "/modelcategorys",
    responses={
        201: {"model": ModelCategory, "description": "Created"},
    },
    tags=["ModelCategory"],
    summary="Create one ModelCategory",
    response_model_by_alias=True,
)
async def modelcategorys_post(
    user: str = Query(None, description="Username"),
    model_category: ModelCategory = Body(None, description="Information about the ModelCategoryto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> ModelCategory:
    """Create a new instance of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)"""
    ...
