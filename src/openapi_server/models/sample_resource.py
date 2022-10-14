# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.visualization_value_inner import VisualizationValueInner


class SampleResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SampleResource - a model defined in OpenAPI

        data_catalog_identifier: The data_catalog_identifier of this SampleResource [Optional].
        description: The description of this SampleResource [Optional].
        id: The id of this SampleResource [Optional].
        label: The label of this SampleResource [Optional].
        type: The type of this SampleResource [Optional].
        value: The value of this SampleResource [Optional].
    """

    data_catalog_identifier: Optional[List[str]] = Field(alias="dataCatalogIdentifier", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    value: Optional[List[VisualizationValueInner]] = Field(alias="value", default=None)

SampleResource.update_forward_refs()
