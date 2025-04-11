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

from openapi_server.models.ckan_response import CKANItem, CKANResponse
from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.settings import ENDPOINT_GRAPH_BASE
from openapi_server.utils.vars import STANDARDVARIABLE_TYPE_NAME, STANDARDVARIABLE_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.standard_variable import StandardVariable
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/standardvariables",
    responses={
        200: {"model": List[StandardVariable], "description": "Successful response - returns an array with the instances of StandardVariable."},
    },
    tags=["StandardVariable"],
    summary="List all instances of StandardVariable",
    response_model_by_alias=True,
)
#@cache(namespace="StandardVariable", expire=1800)
async def standardvariables_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
    enable_ckan: bool = Query(False, description="Enable CKAN output"),
) -> List[StandardVariable] | CKANResponse:
    """Gets a list of all instances of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""

    query_template = """
        CONSTRUCT {
        ?item ?predicate ?prop .
        ?prop a ?type
    }
    WHERE {
        GRAPH ?_g_iri {
            {
                SELECT DISTINCT ?item where {
                    ?item a ?_type_iri .
                    ?item <http://www.w3.org/2000/01/rdf-schema#label> ?label .
                    FILTER(CONTAINS(LCASE(?label), LCASE(?_label)))
                }
                LIMIT 100
                OFFSET 0
            }
            ?item ?predicate ?prop
            OPTIONAL {
                ?prop a ?type
            }
            FILTER (!isBlank(?prop))
            FILTER NOT EXISTS { ?item <https://w3id.org/okn/o/sdm#influences> ?prop }
        }
    }
    """
    request_args = {
        'page': page,
        'per_page': per_page,
        'type': STANDARDVARIABLE_TYPE_URI,
        'g': ENDPOINT_GRAPH_BASE + username,
        'offset': (page - 1) * per_page,
        'label': label
    }

    sparql_response = query_manager.dispatch_sparql_query(
        query_template, request_args)
    variables = query_manager.frame_results(sparql_response, STANDARDVARIABLE_TYPE_URI)

    if enable_ckan:
        if len(variables) > 0:
            return CKANResponse(ResultSet=[CKANItem(Name=variable['label'][0]) for variable in variables])
        else:
            return CKANResponse(ResultSet=[])
    else:
        return variables



@router.delete(
    "/standardvariables/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["StandardVariable"],
    summary="Delete an existing StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_id_delete(
    id: str = Path( description="The ID of the StandardVariable to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""

    await FastAPICache.clear(namespace="StandardVariable")
    return query_manager.delete_resource(
        id=id,
        user=user,

        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME,
        kls=StandardVariable
        )



@router.get(
    "/standardvariables/{id}",
    responses={
        200: {"model": StandardVariable, "description": "Gets the details of a given StandardVariable"},
    },
    tags=["StandardVariable"],
    summary="Get a single StandardVariable by its id",
    response_model_by_alias=True,
)
@cache(namespace="StandardVariable", expire=1800)
async def standardvariables_id_get(
    id: str = Path( description="The ID of the StandardVariable to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> StandardVariable:
    """Gets the details of a given StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME,
        kls=StandardVariable
        )



@router.put(
    "/standardvariables/{id}",
    responses={
        200: {"model": StandardVariable, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["StandardVariable"],
    summary="Update an existing StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_id_put(
    id: str = Path( description="The ID of the StandardVariable to be retrieved"),
    user: str = Query(None, description="Username"),
    standard_variable: StandardVariable = Body(None, description="An old StandardVariableto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> StandardVariable:
    """Updates an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""

    await FastAPICache.clear(namespace="StandardVariable")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME,
        kls=StandardVariable
        )



@router.post(
    "/standardvariables",
    responses={
        201: {"model": StandardVariable, "description": "Created"},
    },
    tags=["StandardVariable"],
    summary="Create one StandardVariable",
    response_model_by_alias=True,
)
async def standardvariables_post(
    user: str = Query(None, description="Username"),
    standard_variable: StandardVariable = Body(None, description="Information about the StandardVariableto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> StandardVariable:
    """Create a new instance of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)"""

    await FastAPICache.clear(namespace="StandardVariable")
    return query_manager.post_resource(

        user=user,
        body=standard_variable,
        rdf_type_uri=STANDARDVARIABLE_TYPE_URI,
        rdf_type_name=STANDARDVARIABLE_TYPE_NAME,
        kls=StandardVariable
        )

