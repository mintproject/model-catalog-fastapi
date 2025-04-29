# coding: utf-8
from fastapi import APIRouter, Depends
from openapi_server.models.resp_apps import RespApps
from openapi_server.models.tapis_app import TapisApp
from tapipy.tapis import Tapis

from openapi_server.security_api import get_token_BearerAuth

router = APIRouter()


@router.get(
    "/tapis/apps",
    responses={
        200: {"model": RespApps, "description": "Successful response - returns an array with the instances of TapisApp."},
    },
    tags=["TapisApp"],
    summary="List all instances of TapisApp",
    response_model_by_alias=True,
    dependencies=[Depends(get_token_BearerAuth)]
)
async def tapis_apps_get(token: str = Depends(get_token_BearerAuth)) -> RespApps:
    print(token)
    tapis = Tapis(base_url='https://tacc.tapis.io')
    tapis.set_jwt(token)
    apps = tapis.apps.getApps()
    return apps


@router.get(
    "/tapis/apps/{app_id}/{app_version}",
    responses={
        200: {"model": TapisApp, "description": "Successful response - returns an instance of TapisApp."},
    },
    tags=["TapisApp"],
    summary="Get a single TapisApp by its id",
    response_model_by_alias=True,
    dependencies=[Depends(get_token_BearerAuth)]
)
async def tapis_apps_id_get(app_id: str, app_version: str, token: str = Depends(get_token_BearerAuth)) -> TapisApp:
    print(token)
    tapis = Tapis(base_url='https://tacc.tapis.io')
    tapis.set_jwt(token)
    print(app_id, app_version)
    app = tapis.apps.getApp(appId=app_id, appVersion=app_version)
    return app
