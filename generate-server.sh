#!/usr/bin/env bash
set -e
dir=${PWD}
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v5.4.0 \
     generate  \
     -i /local/model-catalog.yaml\
     -g typescript \
     -o /local/ \
     --git-repo-id model-catalog-api \
     --git-user-id mintproject-new 
