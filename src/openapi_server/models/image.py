# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class Image(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Image - a model defined in OpenAPI

        has_dimensionality: The has_dimensionality of this Image [Optional].
        has_format: The has_format of this Image [Optional].
        path_location: The path_location of this Image [Optional].
        has_file_structure: The has_file_structure of this Image [Optional].
        description: The description of this Image [Optional].
        has_data_transformation: The has_data_transformation of this Image [Optional].
        has_presentation: The has_presentation of this Image [Optional].
        label: The label of this Image [Optional].
        type: The type of this Image [Optional].
        has_fixed_resource: The has_fixed_resource of this Image [Optional].
        is_transformed_from: The is_transformed_from of this Image [Optional].
        had_primary_source: The had_primary_source of this Image [Optional].
        has_data_transformation_setup: The has_data_transformation_setup of this Image [Optional].
        position: The position of this Image [Optional].
        id: The id of this Image [Optional].
        value: The value of this Image [Optional].
    """

    has_dimensionality: Optional[List[int]] = Field(alias="hasDimensionality", default=None)
    has_format: Optional[List[str]] = Field(alias="hasFormat", default=None)
    path_location: Optional[List[str]] = Field(alias="pathLocation", default=None)
    has_file_structure: Optional[List[object]] = Field(alias="hasFileStructure", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    has_data_transformation: Optional[List[DataTransformation]] = Field(alias="hasDataTransformation", default=None)
    has_presentation: Optional[List[VariablePresentation]] = Field(alias="hasPresentation", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    has_fixed_resource: Optional[List[SampleResource]] = Field(alias="hasFixedResource", default=None)
    is_transformed_from: Optional[List[DatasetSpecification]] = Field(alias="isTransformedFrom", default=None)
    had_primary_source: Optional[List[object]] = Field(alias="hadPrimarySource", default=None)
    has_data_transformation_setup: Optional[List[DataTransformationSetup]] = Field(alias="hasDataTransformationSetup", default=None)
    position: Optional[List[int]] = Field(alias="position", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    value: Optional[List[VisualizationValueInner]] = Field(alias="value", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



from openapi_server.models.data_transformation import DataTransformation
from openapi_server.models.data_transformation_setup import DataTransformationSetup
from openapi_server.models.dataset_specification import DatasetSpecification
from openapi_server.models.sample_resource import SampleResource
from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.models.visualization_value_inner import VisualizationValueInner
Image.update_forward_refs()
