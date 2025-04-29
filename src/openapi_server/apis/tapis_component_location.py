# coding: utf-8
from fastapi import APIRouter, Depends, Query
from tapipy.tapis import Tapis

from openapi_server.models.tapis_app import TapisApp
from openapi_server.security_api import get_token_BearerAuth


router = APIRouter()


@router.get(
    "/tapis/{tenant}/apps",
    responses={
        200: {"model": list[TapisApp], "description": "Successful response - returns an array with the instances of TapisApp."},
    },
    tags=["TapisApp"],
    summary="List all instances of TapisApp",
    response_model_by_alias=True,
    dependencies=[Depends(get_token_BearerAuth)]
)
async def tapis_apps_get(tenant: str = Query(default='tacc'), token: str = Depends(get_token_BearerAuth)) -> list[TapisApp]:
    tapis = Tapis(base_url=f'https://{tenant}.tapis.io')
    tapis.set_jwt(token)
    apps = tapis.apps.getApps()
    return [TapisApp(tenant=tenant, id=app.id, version=app.version) for app in apps]


@router.get(
    "/tapis/{tenant}/apps/{app_id}/{app_version}",
    responses={
        200: {"model": TapisApp, "description": "Successful response - returns an instance of TapisApp."},
    },
    tags=["TapisApp"],
    summary="Get a single TapisApp by its id",
    response_model_by_alias=True,
    dependencies=[Depends(get_token_BearerAuth)]
)
async def tapis_apps_id_get(app_id: str, app_version: str, tenant: str = Query(default='tacc'), token: str = Depends(get_token_BearerAuth)) -> TapisApp:
    tapis = Tapis(base_url=f'https://{tenant}.tapis.io')
    tapis.set_jwt(token)
    app = tapis.apps.getApp(appId=app_id, appVersion=app_version)
    return app
