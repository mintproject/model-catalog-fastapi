#!/usr/bin/env bash
set -e
dir=${PWD}
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v6.2.0 \
     generate  \
     -i /local/model-catalog.yaml\
     -g python-fastapi \
     -o /local/ \
     --git-repo-id model-catalog-api \
     --git-user-id mintproject-new 
