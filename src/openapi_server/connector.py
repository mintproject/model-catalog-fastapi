from obasparql import QueryManager
from openapi_server.settings import ENDPOINT, ENDPOINT_GRAPH_BASE, \
    ENDPOINT_PASSWORD, ENDPOINT_RESOURCE_PREFIX, ENDPOINT_USERNAME, \
    CONTEXT_DIRECTORY, QUERY_DIRECTORY

query_manager = QueryManager(
    endpoint=ENDPOINT,
    endpoint_username=ENDPOINT_USERNAME,
    endpoint_password=ENDPOINT_PASSWORD,
    queries_dir=QUERY_DIRECTORY,
    context_dir=CONTEXT_DIRECTORY,
    named_graph_base=ENDPOINT_GRAPH_BASE,
    uri_prefix=ENDPOINT_RESOURCE_PREFIX)