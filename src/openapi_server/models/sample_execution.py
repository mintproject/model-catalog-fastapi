# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class SampleExecution(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SampleExecution - a model defined in OpenAPI

        description: The description of this SampleExecution [Optional].
        id: The id of this SampleExecution [Optional].
        label: The label of this SampleExecution [Optional].
        type: The type of this SampleExecution [Optional].
        has_execution_command: The has_execution_command of this SampleExecution [Optional].
    """

    description: Optional[List[str]] = Field(alias="description", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    has_execution_command: Optional[List[str]] = Field(alias="hasExecutionCommand", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



SampleExecution.update_forward_refs()
