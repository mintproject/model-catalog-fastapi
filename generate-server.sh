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

rm ${dir}/src/openapi_server/models/catalog_identifier_has_maximum_accepted_value_inner.py
rm ${dir}/src/openapi_server/models/time_interval_interval_value_inner.py

read -p "Do you want to checkout the changes on the model? (y/n) " answer

#If yes
if [[ $answer = y ]] ; then
    git checkout -- ${dir}/src/openapi_server/models
fi


echo "WARNING src/openapi_server/apis/theory_guided_model_api.py changes are not applied. Please comment the line 33 and 34 on generate-server.sh"
git checkout -- src/openapi_server/apis/theory_guided_model_api.py