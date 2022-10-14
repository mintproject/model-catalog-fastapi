# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class Emulator(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Emulator - a model defined in OpenAPI

        has_download_instructions: The has_download_instructions of this Emulator [Optional].
        keywords: The keywords of this Emulator [Optional].
        has_documentation: The has_documentation of this Emulator [Optional].
        has_grid: The has_grid of this Emulator [Optional].
        software_requirements: The software_requirements of this Emulator [Optional].
        has_download_url: The has_download_url of this Emulator [Optional].
        type: The type of this Emulator [Optional].
        has_installation_instructions: The has_installation_instructions of this Emulator [Optional].
        compatible_visualization_software: The compatible_visualization_software of this Emulator [Optional].
        copyright_holder: The copyright_holder of this Emulator [Optional].
        has_faq: The has_faq of this Emulator [Optional].
        logo: The logo of this Emulator [Optional].
        has_contact_person: The has_contact_person of this Emulator [Optional].
        id: The id of this Emulator [Optional].
        limitations: The limitations of this Emulator [Optional].
        identifier: The identifier of this Emulator [Optional].
        author: The author of this Emulator [Optional].
        has_build_file: The has_build_file of this Emulator [Optional].
        short_description: The short_description of this Emulator [Optional].
        date_published: The date_published of this Emulator [Optional].
        theoretical_basis: The theoretical_basis of this Emulator [Optional].
        license: The license of this Emulator [Optional].
        has_source_code: The has_source_code of this Emulator [Optional].
        has_explanation_diagram: The has_explanation_diagram of this Emulator [Optional].
        has_example: The has_example of this Emulator [Optional].
        publisher: The publisher of this Emulator [Optional].
        runtime_estimation: The runtime_estimation of this Emulator [Optional].
        doi: The doi of this Emulator [Optional].
        has_funding: The has_funding of this Emulator [Optional].
        has_process: The has_process of this Emulator [Optional].
        support_details: The support_details of this Emulator [Optional].
        has_version: The has_version of this Emulator [Optional].
        has_typical_data_source: The has_typical_data_source of this Emulator [Optional].
        description: The description of this Emulator [Optional].
        reference_publication: The reference_publication of this Emulator [Optional].
        screenshot: The screenshot of this Emulator [Optional].
        has_model_category: The has_model_category of this Emulator [Optional].
        had_primary_source: The had_primary_source of this Emulator [Optional].
        issue_tracker: The issue_tracker of this Emulator [Optional].
        date_created: The date_created of this Emulator [Optional].
        contributor: The contributor of this Emulator [Optional].
        has_input_variable: The has_input_variable of this Emulator [Optional].
        has_purpose: The has_purpose of this Emulator [Optional].
        has_executable_instructions: The has_executable_instructions of this Emulator [Optional].
        has_sample_visualization: The has_sample_visualization of this Emulator [Optional].
        memory_requirements: The memory_requirements of this Emulator [Optional].
        website: The website of this Emulator [Optional].
        citation: The citation of this Emulator [Optional].
        processor_requirements: The processor_requirements of this Emulator [Optional].
        parameterization: The parameterization of this Emulator [Optional].
        has_usage_notes: The has_usage_notes of this Emulator [Optional].
        readme: The readme of this Emulator [Optional].
        label: The label of this Emulator [Optional].
        has_assumption: The has_assumption of this Emulator [Optional].
        operating_systems: The operating_systems of this Emulator [Optional].
        has_executable_notebook: The has_executable_notebook of this Emulator [Optional].
        has_equation: The has_equation of this Emulator [Optional].
        useful_for_calculating_index: The useful_for_calculating_index of this Emulator [Optional].
        has_output_variable: The has_output_variable of this Emulator [Optional].
    """

    has_download_instructions: Optional[List[str]] = Field(alias="hasDownloadInstructions", default=None)
    keywords: Optional[List[str]] = Field(alias="keywords", default=None)
    has_documentation: Optional[List[str]] = Field(alias="hasDocumentation", default=None)
    has_grid: Optional[List[Grid]] = Field(alias="hasGrid", default=None)
    software_requirements: Optional[List[str]] = Field(alias="softwareRequirements", default=None)
    has_download_url: Optional[List[str]] = Field(alias="hasDownloadURL", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    has_installation_instructions: Optional[List[str]] = Field(alias="hasInstallationInstructions", default=None)
    compatible_visualization_software: Optional[List[Software]] = Field(alias="compatibleVisualizationSoftware", default=None)
    copyright_holder: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="copyrightHolder", default=None)
    has_faq: Optional[List[str]] = Field(alias="hasFAQ", default=None)
    logo: Optional[List[Image]] = Field(alias="logo", default=None)
    has_contact_person: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="hasContactPerson", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    limitations: Optional[List[str]] = Field(alias="limitations", default=None)
    identifier: Optional[List[str]] = Field(alias="identifier", default=None)
    author: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="author", default=None)
    has_build_file: Optional[List[str]] = Field(alias="hasBuildFile", default=None)
    short_description: Optional[List[str]] = Field(alias="shortDescription", default=None)
    date_published: Optional[List[str]] = Field(alias="datePublished", default=None)
    theoretical_basis: Optional[List[str]] = Field(alias="theoreticalBasis", default=None)
    license: Optional[List[str]] = Field(alias="license", default=None)
    has_source_code: Optional[List[SourceCode]] = Field(alias="hasSourceCode", default=None)
    has_explanation_diagram: Optional[List[Image]] = Field(alias="hasExplanationDiagram", default=None)
    has_example: Optional[List[str]] = Field(alias="hasExample", default=None)
    publisher: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="publisher", default=None)
    runtime_estimation: Optional[List[str]] = Field(alias="runtimeEstimation", default=None)
    doi: Optional[List[str]] = Field(alias="doi", default=None)
    has_funding: Optional[List[FundingInformation]] = Field(alias="hasFunding", default=None)
    has_process: Optional[List[Process]] = Field(alias="hasProcess", default=None)
    support_details: Optional[List[str]] = Field(alias="supportDetails", default=None)
    has_version: Optional[List[SoftwareVersion]] = Field(alias="hasVersion", default=None)
    has_typical_data_source: Optional[List[str]] = Field(alias="hasTypicalDataSource", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    reference_publication: Optional[List[str]] = Field(alias="referencePublication", default=None)
    screenshot: Optional[List[Image]] = Field(alias="screenshot", default=None)
    has_model_category: Optional[List[ModelCategory]] = Field(alias="hasModelCategory", default=None)
    had_primary_source: Optional[List[object]] = Field(alias="hadPrimarySource", default=None)
    issue_tracker: Optional[List[str]] = Field(alias="issueTracker", default=None)
    date_created: Optional[List[str]] = Field(alias="dateCreated", default=None)
    contributor: Optional[List[Person]] = Field(alias="contributor", default=None)
    has_input_variable: Optional[List[VariablePresentation]] = Field(alias="hasInputVariable", default=None)
    has_purpose: Optional[List[str]] = Field(alias="hasPurpose", default=None)
    has_executable_instructions: Optional[List[str]] = Field(alias="hasExecutableInstructions", default=None)
    has_sample_visualization: Optional[List[Visualization]] = Field(alias="hasSampleVisualization", default=None)
    memory_requirements: Optional[List[str]] = Field(alias="memoryRequirements", default=None)
    website: Optional[List[str]] = Field(alias="website", default=None)
    citation: Optional[List[str]] = Field(alias="citation", default=None)
    processor_requirements: Optional[List[str]] = Field(alias="processorRequirements", default=None)
    parameterization: Optional[List[str]] = Field(alias="parameterization", default=None)
    has_usage_notes: Optional[List[str]] = Field(alias="hasUsageNotes", default=None)
    readme: Optional[List[str]] = Field(alias="readme", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    has_assumption: Optional[List[str]] = Field(alias="hasAssumption", default=None)
    operating_systems: Optional[List[str]] = Field(alias="operatingSystems", default=None)
    has_executable_notebook: Optional[List[str]] = Field(alias="hasExecutableNotebook", default=None)
    has_equation: Optional[List[Equation]] = Field(alias="hasEquation", default=None)
    useful_for_calculating_index: Optional[List[NumericalIndex]] = Field(alias="usefulForCalculatingIndex", default=None)
    has_output_variable: Optional[List[VariablePresentation]] = Field(alias="hasOutputVariable", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



from openapi_server.models.emulator_copyright_holder_inner import EmulatorCopyrightHolderInner
from openapi_server.models.equation import Equation
from openapi_server.models.funding_information import FundingInformation
from openapi_server.models.grid import Grid
from openapi_server.models.image import Image
from openapi_server.models.model_category import ModelCategory
from openapi_server.models.numerical_index import NumericalIndex
from openapi_server.models.person import Person
from openapi_server.models.process import Process
from openapi_server.models.software import Software
from openapi_server.models.software_version import SoftwareVersion
from openapi_server.models.source_code import SourceCode
from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.models.visualization import Visualization
Emulator.update_forward_refs()
