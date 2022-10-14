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
from openapi_server.models.hybrid_model import HybridModel
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/hybridmodels",
    responses={
        200: {"model": List[HybridModel], "description": "Successful response - returns an array with the instances of HybridModel."},
    },
    tags=["HybridModel"],
    summary="List all instances of HybridModel",
    response_model_by_alias=True,
)
async def hybridmodels_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[HybridModel]:
    """Gets a list of all instances of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)"""
    ...


@router.delete(
    "/hybridmodels/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["HybridModel"],
    summary="Delete an existing HybridModel",
    response_model_by_alias=True,
)
async def hybridmodels_id_delete(
    id: str = Path(None, description="The ID of the HybridModel to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)"""
    ...


@router.get(
    "/hybridmodels/{id}",
    responses={
        200: {"model": HybridModel, "description": "Gets the details of a given HybridModel"},
    },
    tags=["HybridModel"],
    summary="Get a single HybridModel by its id",
    response_model_by_alias=True,
)
async def hybridmodels_id_get(
    id: str = Path(None, description="The ID of the HybridModel to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> HybridModel:
    """Gets the details of a given HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)"""
    ...


@router.put(
    "/hybridmodels/{id}",
    responses={
        200: {"model": HybridModel, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["HybridModel"],
    summary="Update an existing HybridModel",
    response_model_by_alias=True,
)
async def hybridmodels_id_put(
    id: str = Path(None, description="The ID of the HybridModel to be retrieved"),
    user: str = Query(None, description="Username"),
    hybrid_model: HybridModel = Body(None, description="An old HybridModelto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> HybridModel:
    """Updates an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)"""
    ...


@router.post(
    "/hybridmodels",
    responses={
        201: {"model": HybridModel, "description": "Created"},
    },
    tags=["HybridModel"],
    summary="Create one HybridModel",
    response_model_by_alias=True,
)
async def hybridmodels_post(
    user: str = Query(None, description="Username"),
    hybrid_model: HybridModel = Body(None, description="Information about the HybridModelto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> HybridModel:
    """Create a new instance of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)"""
    ...
