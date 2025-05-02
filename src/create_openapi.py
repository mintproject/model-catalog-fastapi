from fastapi.openapi.utils import get_openapi
from openapi_server.main import app
import json




# Remove all the AnyOf from the schema, loop through the schema and remove the anyOf key
def remove_anyof(schema):
    for key, value in schema.items():
        if 'anyOf' in value:
            del value['anyOf']
        elif isinstance(value, dict):
            remove_anyof(value)
        elif key == 'properties' and isinstance(value, dict):
            for prop_key, prop_value in value.items():
                if 'anyOf' in prop_value:
                    del prop_value['anyOf']
                elif isinstance(prop_value, dict):
                    remove_anyof(prop_value)

    return schema



with open('../openapi.json', 'w') as f:
    openapi = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )

    # remove_anyof(openapi['components']['schemas'])

    json.dump(openapi, f, indent=2)
