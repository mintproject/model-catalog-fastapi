# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class PointBasedGrid(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PointBasedGrid - a model defined in OpenAPI

        has_dimensionality: The has_dimensionality of this PointBasedGrid [Optional].
        has_format: The has_format of this PointBasedGrid [Optional].
        path_location: The path_location of this PointBasedGrid [Optional].
        has_file_structure: The has_file_structure of this PointBasedGrid [Optional].
        description: The description of this PointBasedGrid [Optional].
        has_data_transformation: The has_data_transformation of this PointBasedGrid [Optional].
        has_presentation: The has_presentation of this PointBasedGrid [Optional].
        label: The label of this PointBasedGrid [Optional].
        type: The type of this PointBasedGrid [Optional].
        has_fixed_resource: The has_fixed_resource of this PointBasedGrid [Optional].
        has_coordinate_system: The has_coordinate_system of this PointBasedGrid [Optional].
        has_spatial_resolution: The has_spatial_resolution of this PointBasedGrid [Optional].
        is_transformed_from: The is_transformed_from of this PointBasedGrid [Optional].
        has_shape: The has_shape of this PointBasedGrid [Optional].
        has_dimension: The has_dimension of this PointBasedGrid [Optional].
        has_data_transformation_setup: The has_data_transformation_setup of this PointBasedGrid [Optional].
        position: The position of this PointBasedGrid [Optional].
        id: The id of this PointBasedGrid [Optional].
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
    has_coordinate_system: Optional[List[str]] = Field(alias="hasCoordinateSystem", default=None)
    has_spatial_resolution: Optional[List[str]] = Field(alias="hasSpatialResolution", default=None)
    is_transformed_from: Optional[List[DatasetSpecification]] = Field(alias="isTransformedFrom", default=None)
    has_shape: Optional[List[str]] = Field(alias="hasShape", default=None)
    has_dimension: Optional[List[str]] = Field(alias="hasDimension", default=None)
    has_data_transformation_setup: Optional[List[DataTransformationSetup]] = Field(alias="hasDataTransformationSetup", default=None)
    position: Optional[List[int]] = Field(alias="position", default=None)
    id: Optional[str] = Field(alias="id", default=None)

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
PointBasedGrid.update_forward_refs()
