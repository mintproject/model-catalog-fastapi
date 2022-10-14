# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class Visualization(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Visualization - a model defined in OpenAPI

        has_format: The has_format of this Visualization [Optional].
        had_primary_source: The had_primary_source of this Visualization [Optional].
        was_derived_from_software: The was_derived_from_software of this Visualization [Optional].
        description: The description of this Visualization [Optional].
        id: The id of this Visualization [Optional].
        label: The label of this Visualization [Optional].
        type: The type of this Visualization [Optional].
        value: The value of this Visualization [Optional].
    """

    has_format: Optional[List[str]] = Field(alias="hasFormat", default=None)
    had_primary_source: Optional[List[object]] = Field(alias="hadPrimarySource", default=None)
    was_derived_from_software: Optional[List[Software]] = Field(alias="wasDerivedFromSoftware", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    value: Optional[List[VisualizationValueInner]] = Field(alias="value", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



from openapi_server.models.software import Software
from openapi_server.models.visualization_value_inner import VisualizationValueInner
Visualization.update_forward_refs()
