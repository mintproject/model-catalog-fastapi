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
from openapi_server.models.funding_information import FundingInformation
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/fundinginformations",
    responses={
        200: {"model": List[FundingInformation], "description": "Successful response - returns an array with the instances of FundingInformation."},
    },
    tags=["FundingInformation"],
    summary="List all instances of FundingInformation",
    response_model_by_alias=True,
)
async def fundinginformations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[FundingInformation]:
    """Gets a list of all instances of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)"""
    ...


@router.delete(
    "/fundinginformations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["FundingInformation"],
    summary="Delete an existing FundingInformation",
    response_model_by_alias=True,
)
async def fundinginformations_id_delete(
    id: str = Path(None, description="The ID of the FundingInformation to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)"""
    ...


@router.get(
    "/fundinginformations/{id}",
    responses={
        200: {"model": FundingInformation, "description": "Gets the details of a given FundingInformation"},
    },
    tags=["FundingInformation"],
    summary="Get a single FundingInformation by its id",
    response_model_by_alias=True,
)
async def fundinginformations_id_get(
    id: str = Path(None, description="The ID of the FundingInformation to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> FundingInformation:
    """Gets the details of a given FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)"""
    ...


@router.put(
    "/fundinginformations/{id}",
    responses={
        200: {"model": FundingInformation, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["FundingInformation"],
    summary="Update an existing FundingInformation",
    response_model_by_alias=True,
)
async def fundinginformations_id_put(
    id: str = Path(None, description="The ID of the FundingInformation to be retrieved"),
    user: str = Query(None, description="Username"),
    funding_information: FundingInformation = Body(None, description="An old FundingInformationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> FundingInformation:
    """Updates an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)"""
    ...


@router.post(
    "/fundinginformations",
    responses={
        201: {"model": FundingInformation, "description": "Created"},
    },
    tags=["FundingInformation"],
    summary="Create one FundingInformation",
    response_model_by_alias=True,
)
async def fundinginformations_post(
    user: str = Query(None, description="Username"),
    funding_information: FundingInformation = Body(None, description="Information about the FundingInformationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> FundingInformation:
    """Create a new instance of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)"""
    ...
