# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.catalog_identifier_has_maximum_accepted_value_inner import CatalogIdentifierHasMaximumAcceptedValueInner
from openapi_server.models.intervention import Intervention
from openapi_server.models.unit import Unit
from openapi_server.models.variable import Variable
from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.models.visualization_value_inner import VisualizationValueInner


class CatalogIdentifier(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CatalogIdentifier - a model defined in OpenAPI

        has_default_value: The has_default_value of this CatalogIdentifier [Optional].
        has_maximum_accepted_value: The has_maximum_accepted_value of this CatalogIdentifier [Optional].
        description: The description of this CatalogIdentifier [Optional].
        has_data_type: The has_data_type of this CatalogIdentifier [Optional].
        has_fixed_value: The has_fixed_value of this CatalogIdentifier [Optional].
        has_presentation: The has_presentation of this CatalogIdentifier [Optional].
        label: The label of this CatalogIdentifier [Optional].
        recommended_increment: The recommended_increment of this CatalogIdentifier [Optional].
        type: The type of this CatalogIdentifier [Optional].
        has_minimum_accepted_value: The has_minimum_accepted_value of this CatalogIdentifier [Optional].
        has_accepted_values: The has_accepted_values of this CatalogIdentifier [Optional].
        adjusts_variable: The adjusts_variable of this CatalogIdentifier [Optional].
        relevant_for_intervention: The relevant_for_intervention of this CatalogIdentifier [Optional].
        position: The position of this CatalogIdentifier [Optional].
        id: The id of this CatalogIdentifier [Optional].
        uses_unit: The uses_unit of this CatalogIdentifier [Optional].
        has_step_size: The has_step_size of this CatalogIdentifier [Optional].
    """

    has_default_value: Optional[List[VisualizationValueInner]] = Field(alias="hasDefaultValue", default=None)
    has_maximum_accepted_value: Optional[List[CatalogIdentifierHasMaximumAcceptedValueInner]] = Field(alias="hasMaximumAcceptedValue", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    has_data_type: Optional[List[str]] = Field(alias="hasDataType", default=None)
    has_fixed_value: Optional[List[VisualizationValueInner]] = Field(alias="hasFixedValue", default=None)
    has_presentation: Optional[List[VariablePresentation]] = Field(alias="hasPresentation", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    recommended_increment: Optional[List[float]] = Field(alias="recommendedIncrement", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    has_minimum_accepted_value: Optional[List[CatalogIdentifierHasMaximumAcceptedValueInner]] = Field(alias="hasMinimumAcceptedValue", default=None)
    has_accepted_values: Optional[List[str]] = Field(alias="hasAcceptedValues", default=None)
    adjusts_variable: Optional[List[Variable]] = Field(alias="adjustsVariable", default=None)
    relevant_for_intervention: Optional[List[Intervention]] = Field(alias="relevantForIntervention", default=None)
    position: Optional[List[int]] = Field(alias="position", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    uses_unit: Optional[List[Unit]] = Field(alias="usesUnit", default=None)
    has_step_size: Optional[List[float]] = Field(alias="hasStepSize", default=None)

CatalogIdentifier.update_forward_refs()
