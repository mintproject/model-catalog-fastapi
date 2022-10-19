#!/usr/bin/env bash
set -e
dir=${PWD}
docker run \
    --user "$(id -u):$(id -g)" \
    -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v6.2.0 \
    generate \
    -i /local/model-catalog.yaml -g python-fastapi \
    -o /local/ \
    --template-dir /local/.openapi-generator/template \
    --git-repo-id model-catalog-api \
    --git-user-id mintproject-new \
    --additional-properties=allowUnicodeIdentifiers=true

# Patch: the default values are corrected weirdly
sed -i 's/&#39;/"/g'  ${dir}/src/openapi_server/apis/*.py
#sed -i '/^async def .*_get(/i @cache(expire=600)' ${dir}/src/openapi_server/apis/*.py
rm ${dir}/src/openapi_server/apis/default_api.py
sed -i '/openapi_server.apis.default_ap/d'  ${dir}/src/openapi_server/main.py
sed -i '/app.include_router(DefaultApiRouter)/d '  ${dir}/src/openapi_server/main.py