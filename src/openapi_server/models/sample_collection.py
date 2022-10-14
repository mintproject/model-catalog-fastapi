# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class SampleCollection(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SampleCollection - a model defined in OpenAPI

        data_catalog_identifier: The data_catalog_identifier of this SampleCollection [Optional].
        has_part: The has_part of this SampleCollection [Optional].
        description: The description of this SampleCollection [Optional].
        id: The id of this SampleCollection [Optional].
        label: The label of this SampleCollection [Optional].
        type: The type of this SampleCollection [Optional].
        value: The value of this SampleCollection [Optional].
    """

    data_catalog_identifier: Optional[List[str]] = Field(alias="dataCatalogIdentifier", default=None)
    has_part: Optional[List[SampleResource]] = Field(alias="hasPart", default=None)
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



from openapi_server.models.sample_resource import SampleResource
from openapi_server.models.visualization_value_inner import VisualizationValueInner
SampleCollection.update_forward_refs()
