# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Process(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Process - a model defined in OpenAPI

        influences: The influences of this Process [Optional].
        description: The description of this Process [Optional].
        id: The id of this Process [Optional].
        label: The label of this Process [Optional].
        type: The type of this Process [Optional].
    """

    influences: Optional[List[Process]] = Field(alias="influences", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)

Process.update_forward_refs()
