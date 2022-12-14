# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class SourceCode(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SourceCode - a model defined in OpenAPI

        license: The license of this SourceCode [Optional].
        programming_language: The programming_language of this SourceCode [Optional].
        description: The description of this SourceCode [Optional].
        code_repository: The code_repository of this SourceCode [Optional].
        id: The id of this SourceCode [Optional].
        label: The label of this SourceCode [Optional].
        type: The type of this SourceCode [Optional].
    """

    license: Optional[List[str]] = Field(alias="license", default=None)
    programming_language: Optional[List[str]] = Field(alias="programmingLanguage", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    code_repository: Optional[List[str]] = Field(alias="codeRepository", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



SourceCode.update_forward_refs()
