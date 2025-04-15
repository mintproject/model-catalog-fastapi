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
from openapi_server.settings import ENDPOINT_GRAPH_BASE
from openapi_server.utils.vars import VARIABLEPRESENTATION_TYPE_NAME, VARIABLEPRESENTATION_TYPE_URI
from openapi_server.connector import query_manager
from fastapi_cache.decorator import cache

from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/variablepresentations",
    responses={
        200: {"model": List[VariablePresentation], "description": "Successful response - returns an array with the instances of VariablePresentation."},
    },
    tags=["VariablePresentation"],
    summary="List all instances of VariablePresentation",
    response_model_by_alias=True,
)
@cache(namespace="VariablePresentation", expire=1800)
async def variablepresentations_get(
    username: str = Query(None, description="Name of the user graph to query"),
    label: str = Query(None, description="Filter by label"),
    page: int = Query(1, description="Page number"),
    per_page: int = Query(100, description="Items per page", ge=1, le=200),
) -> List[VariablePresentation]:
    """Gets a list of all instances of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""

    request_args = {
        'page': page,
        'per_page': per_page,
        'type': VARIABLEPRESENTATION_TYPE_URI,
        'g': ENDPOINT_GRAPH_BASE + username,
        'offset': (page - 1) * per_page,
        'label': label
    }
    query_template = """
    CONSTRUCT {
        ?item ?itemPredicate ?itemProp .

        # StandardVariable and its properties
        ?standardVariable ?standardVariablePredicate ?standardVariableProp .

        # Connection between variable and standardVariable
        ?item <https://w3id.org/okn/o/sd#hasStandardVariable> ?standardVariable .

        # Unit and its properties
        ?item <https://w3id.org/okn/o/sd#usesUnit> ?unit .
        ?unit ?unitPredicate ?unitProp .
    }
    WHERE {
        GRAPH ?_g_iri {
            {
                SELECT DISTINCT ?item ?standardVariable where {
                    ?item a ?_type_iri .
                    ?item <http://www.w3.org/2000/01/rdf-schema#label> ?label .
                    ?item <https://w3id.org/okn/o/sd#hasStandardVariable> ?standardVariable .
                    ?standardVariable <http://www.w3.org/2000/01/rdf-schema#label> ?standardVariableLabel .
                    %s
                }
                LIMIT 100
                OFFSET 0
            }

            # Get all properties of the variable
            ?item ?itemPredicate ?itemProp .
            FILTER (!isBlank(?itemProp))
            FILTER NOT EXISTS { ?item <https://w3id.org/okn/o/sdm#influences> ?itemProp }

            # Get all properties of the standardVariable
            ?standardVariable ?standardVariablePredicate ?standardVariableProp .
            FILTER (!isBlank(?standardVariableProp))

            # Get all properties of the unit
            OPTIONAL {
                ?item <https://w3id.org/okn/o/sd#usesUnit> ?unit .
                ?unit ?unitPredicate ?unitProp .
                FILTER (!isBlank(?unitProp))
            }
        }
    }
    """

    label_filter = "FILTER(CONTAINS(LCASE(?label), LCASE(?_label)))" if label else ""
    query = query_template % label_filter

    sparql_response = query_manager.dispatch_sparql_query(
        query, request_args)

    variable_presentations = query_manager.frame_results(sparql_response, VARIABLEPRESENTATION_TYPE_URI)
    return variable_presentations



@router.delete(
    "/variablepresentations/{id}",
    responses={
        202: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["VariablePresentation"],
    summary="Delete an existing VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_id_delete(
    id: str = Path( description="The ID of the VariablePresentation to be retrieved"),
    user: str = Query(None, description="Username"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> None:
    """Delete an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""

    await FastAPICache.clear(namespace="VariablePresentation")
    return query_manager.delete_resource(
        id=id,
        user=user,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME,
        kls=VariablePresentation
        )



@router.get(
    "/variablepresentations/{id}",
    responses={
        200: {"model": VariablePresentation, "description": "Gets the details of a given VariablePresentation"},
    },
    tags=["VariablePresentation"],
    summary="Get a single VariablePresentation by its id",
    response_model_by_alias=True,
)
@cache(namespace="VariablePresentation", expire=1800)
async def variablepresentations_id_get(
    id: str = Path( description="The ID of the VariablePresentation to be retrieved"),
    username: str = Query(None, description="Name of the user graph to query"),
) -> VariablePresentation:
    """Gets the details of a given VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""

    return query_manager.get_resource(
        id=id,
        username=username,

        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME,
        kls=VariablePresentation
        )



@router.put(
    "/variablepresentations/{id}",
    responses={
        200: {"model": VariablePresentation, "description": "Updated"},
        404: {"description": "Not Found"},
    },
    tags=["VariablePresentation"],
    summary="Update an existing VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_id_put(
    id: str = Path( description="The ID of the VariablePresentation to be retrieved"),
    user: str = Query(None, description="Username"),
    variable_presentation: VariablePresentation = Body(None, description="An old VariablePresentationto be updated"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> VariablePresentation:
    """Updates an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""

    await FastAPICache.clear(namespace="VariablePresentation")
    return query_manager.put_resource(
        id=id,
        user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME,
        kls=VariablePresentation
        )



@router.post(
    "/variablepresentations",
    responses={
        201: {"model": VariablePresentation, "description": "Created"},
    },
    tags=["VariablePresentation"],
    summary="Create one VariablePresentation",
    response_model_by_alias=True,
)
async def variablepresentations_post(
    user: str = Query(None, description="Username"),
    variable_presentation: VariablePresentation = Body(None, description="Information about the VariablePresentationto be created"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> VariablePresentation:
    """Create a new instance of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)"""

    await FastAPICache.clear(namespace="VariablePresentation")
    return query_manager.post_resource(

        user=user,
        body=variable_presentation,
        rdf_type_uri=VARIABLEPRESENTATION_TYPE_URI,
        rdf_type_name=VARIABLEPRESENTATION_TYPE_NAME,
        kls=VariablePresentation
        )

