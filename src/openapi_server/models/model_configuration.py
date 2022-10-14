# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401

class ModelConfiguration(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ModelConfiguration - a model defined in OpenAPI

        has_download_instructions: The has_download_instructions of this ModelConfiguration [Optional].
        keywords: The keywords of this ModelConfiguration [Optional].
        has_documentation: The has_documentation of this ModelConfiguration [Optional].
        has_grid: The has_grid of this ModelConfiguration [Optional].
        has_implementation_script_location: The has_implementation_script_location of this ModelConfiguration [Optional].
        software_requirements: The software_requirements of this ModelConfiguration [Optional].
        has_download_url: The has_download_url of this ModelConfiguration [Optional].
        type: The type of this ModelConfiguration [Optional].
        has_installation_instructions: The has_installation_instructions of this ModelConfiguration [Optional].
        compatible_visualization_software: The compatible_visualization_software of this ModelConfiguration [Optional].
        copyright_holder: The copyright_holder of this ModelConfiguration [Optional].
        has_region: The has_region of this ModelConfiguration [Optional].
        has_faq: The has_faq of this ModelConfiguration [Optional].
        logo: The logo of this ModelConfiguration [Optional].
        has_contact_person: The has_contact_person of this ModelConfiguration [Optional].
        tag: The tag of this ModelConfiguration [Optional].
        id: The id of this ModelConfiguration [Optional].
        limitations: The limitations of this ModelConfiguration [Optional].
        identifier: The identifier of this ModelConfiguration [Optional].
        has_sample_execution: The has_sample_execution of this ModelConfiguration [Optional].
        has_sample_result: The has_sample_result of this ModelConfiguration [Optional].
        author: The author of this ModelConfiguration [Optional].
        has_constraint: The has_constraint of this ModelConfiguration [Optional].
        has_build_file: The has_build_file of this ModelConfiguration [Optional].
        short_description: The short_description of this ModelConfiguration [Optional].
        has_execution_command: The has_execution_command of this ModelConfiguration [Optional].
        date_published: The date_published of this ModelConfiguration [Optional].
        theoretical_basis: The theoretical_basis of this ModelConfiguration [Optional].
        license: The license of this ModelConfiguration [Optional].
        has_source_code: The has_source_code of this ModelConfiguration [Optional].
        has_setup: The has_setup of this ModelConfiguration [Optional].
        has_explanation_diagram: The has_explanation_diagram of this ModelConfiguration [Optional].
        has_example: The has_example of this ModelConfiguration [Optional].
        publisher: The publisher of this ModelConfiguration [Optional].
        has_output: The has_output of this ModelConfiguration [Optional].
        runtime_estimation: The runtime_estimation of this ModelConfiguration [Optional].
        has_output_time_interval: The has_output_time_interval of this ModelConfiguration [Optional].
        doi: The doi of this ModelConfiguration [Optional].
        has_funding: The has_funding of this ModelConfiguration [Optional].
        has_component_location: The has_component_location of this ModelConfiguration [Optional].
        has_process: The has_process of this ModelConfiguration [Optional].
        support_details: The support_details of this ModelConfiguration [Optional].
        has_version: The has_version of this ModelConfiguration [Optional].
        has_typical_data_source: The has_typical_data_source of this ModelConfiguration [Optional].
        description: The description of this ModelConfiguration [Optional].
        reference_publication: The reference_publication of this ModelConfiguration [Optional].
        screenshot: The screenshot of this ModelConfiguration [Optional].
        has_model_category: The has_model_category of this ModelConfiguration [Optional].
        had_primary_source: The had_primary_source of this ModelConfiguration [Optional].
        issue_tracker: The issue_tracker of this ModelConfiguration [Optional].
        has_software_image: The has_software_image of this ModelConfiguration [Optional].
        date_created: The date_created of this ModelConfiguration [Optional].
        contributor: The contributor of this ModelConfiguration [Optional].
        has_input_variable: The has_input_variable of this ModelConfiguration [Optional].
        has_model_result_table: The has_model_result_table of this ModelConfiguration [Optional].
        has_purpose: The has_purpose of this ModelConfiguration [Optional].
        has_executable_instructions: The has_executable_instructions of this ModelConfiguration [Optional].
        has_sample_visualization: The has_sample_visualization of this ModelConfiguration [Optional].
        has_causal_diagram: The has_causal_diagram of this ModelConfiguration [Optional].
        memory_requirements: The memory_requirements of this ModelConfiguration [Optional].
        website: The website of this ModelConfiguration [Optional].
        citation: The citation of this ModelConfiguration [Optional].
        processor_requirements: The processor_requirements of this ModelConfiguration [Optional].
        parameterization: The parameterization of this ModelConfiguration [Optional].
        has_usage_notes: The has_usage_notes of this ModelConfiguration [Optional].
        has_support_script_location: The has_support_script_location of this ModelConfiguration [Optional].
        readme: The readme of this ModelConfiguration [Optional].
        label: The label of this ModelConfiguration [Optional].
        has_assumption: The has_assumption of this ModelConfiguration [Optional].
        has_parameter: The has_parameter of this ModelConfiguration [Optional].
        operating_systems: The operating_systems of this ModelConfiguration [Optional].
        has_executable_notebook: The has_executable_notebook of this ModelConfiguration [Optional].
        has_equation: The has_equation of this ModelConfiguration [Optional].
        useful_for_calculating_index: The useful_for_calculating_index of this ModelConfiguration [Optional].
        has_input: The has_input of this ModelConfiguration [Optional].
        has_output_variable: The has_output_variable of this ModelConfiguration [Optional].
    """

    has_download_instructions: Optional[List[str]] = Field(alias="hasDownloadInstructions", default=None)
    keywords: Optional[List[str]] = Field(alias="keywords", default=None)
    has_documentation: Optional[List[str]] = Field(alias="hasDocumentation", default=None)
    has_grid: Optional[List[Grid]] = Field(alias="hasGrid", default=None)
    has_implementation_script_location: Optional[List[str]] = Field(alias="hasImplementationScriptLocation", default=None)
    software_requirements: Optional[List[str]] = Field(alias="softwareRequirements", default=None)
    has_download_url: Optional[List[str]] = Field(alias="hasDownloadURL", default=None)
    type: Optional[List[str]] = Field(alias="type", default=None)
    has_installation_instructions: Optional[List[str]] = Field(alias="hasInstallationInstructions", default=None)
    compatible_visualization_software: Optional[List[Software]] = Field(alias="compatibleVisualizationSoftware", default=None)
    copyright_holder: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="copyrightHolder", default=None)
    has_region: Optional[List[Region]] = Field(alias="hasRegion", default=None)
    has_faq: Optional[List[str]] = Field(alias="hasFAQ", default=None)
    logo: Optional[List[Image]] = Field(alias="logo", default=None)
    has_contact_person: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="hasContactPerson", default=None)
    tag: Optional[List[str]] = Field(alias="tag", default=None)
    id: Optional[str] = Field(alias="id", default=None)
    limitations: Optional[List[str]] = Field(alias="limitations", default=None)
    identifier: Optional[List[str]] = Field(alias="identifier", default=None)
    has_sample_execution: Optional[List[SampleExecution]] = Field(alias="hasSampleExecution", default=None)
    has_sample_result: Optional[List[SampleResource]] = Field(alias="hasSampleResult", default=None)
    author: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="author", default=None)
    has_constraint: Optional[List[Constraint]] = Field(alias="hasConstraint", default=None)
    has_build_file: Optional[List[str]] = Field(alias="hasBuildFile", default=None)
    short_description: Optional[List[str]] = Field(alias="shortDescription", default=None)
    has_execution_command: Optional[List[str]] = Field(alias="hasExecutionCommand", default=None)
    date_published: Optional[List[str]] = Field(alias="datePublished", default=None)
    theoretical_basis: Optional[List[str]] = Field(alias="theoreticalBasis", default=None)
    license: Optional[List[str]] = Field(alias="license", default=None)
    has_source_code: Optional[List[SourceCode]] = Field(alias="hasSourceCode", default=None)
    has_setup: Optional[List[ConfigurationSetup]] = Field(alias="hasSetup", default=None)
    has_explanation_diagram: Optional[List[Image]] = Field(alias="hasExplanationDiagram", default=None)
    has_example: Optional[List[str]] = Field(alias="hasExample", default=None)
    publisher: Optional[List[EmulatorCopyrightHolderInner]] = Field(alias="publisher", default=None)
    has_output: Optional[List[DatasetSpecification]] = Field(alias="hasOutput", default=None)
    runtime_estimation: Optional[List[str]] = Field(alias="runtimeEstimation", default=None)
    has_output_time_interval: Optional[List[TimeInterval]] = Field(alias="hasOutputTimeInterval", default=None)
    doi: Optional[List[str]] = Field(alias="doi", default=None)
    has_funding: Optional[List[FundingInformation]] = Field(alias="hasFunding", default=None)
    has_component_location: Optional[List[str]] = Field(alias="hasComponentLocation", default=None)
    has_process: Optional[List[Process]] = Field(alias="hasProcess", default=None)
    support_details: Optional[List[str]] = Field(alias="supportDetails", default=None)
    has_version: Optional[List[SoftwareVersion]] = Field(alias="hasVersion", default=None)
    has_typical_data_source: Optional[List[str]] = Field(alias="hasTypicalDataSource", default=None)
    description: Optional[List[str]] = Field(alias="description", default=None)
    reference_publication: Optional[List[str]] = Field(alias="referencePublication", default=None)
    screenshot: Optional[List[Image]] = Field(alias="screenshot", default=None)
    has_model_category: Optional[List[ModelCategory]] = Field(alias="hasModelCategory", default=None)
    had_primary_source: Optional[List[BaseModel]] = Field(alias="hadPrimarySource", default=None)
    issue_tracker: Optional[List[str]] = Field(alias="issueTracker", default=None)
    has_software_image: Optional[List[SoftwareImage]] = Field(alias="hasSoftwareImage", default=None)
    date_created: Optional[List[str]] = Field(alias="dateCreated", default=None)
    contributor: Optional[List[Person]] = Field(alias="contributor", default=None)
    has_input_variable: Optional[List[VariablePresentation]] = Field(alias="hasInputVariable", default=None)
    has_model_result_table: Optional[List[str]] = Field(alias="hasModelResultTable", default=None)
    has_purpose: Optional[List[str]] = Field(alias="hasPurpose", default=None)
    has_executable_instructions: Optional[List[str]] = Field(alias="hasExecutableInstructions", default=None)
    has_sample_visualization: Optional[List[Visualization]] = Field(alias="hasSampleVisualization", default=None)
    has_causal_diagram: Optional[List[CausalDiagram]] = Field(alias="hasCausalDiagram", default=None)
    memory_requirements: Optional[List[str]] = Field(alias="memoryRequirements", default=None)
    website: Optional[List[str]] = Field(alias="website", default=None)
    citation: Optional[List[str]] = Field(alias="citation", default=None)
    processor_requirements: Optional[List[str]] = Field(alias="processorRequirements", default=None)
    parameterization: Optional[List[str]] = Field(alias="parameterization", default=None)
    has_usage_notes: Optional[List[str]] = Field(alias="hasUsageNotes", default=None)
    has_support_script_location: Optional[List[str]] = Field(alias="hasSupportScriptLocation", default=None)
    readme: Optional[List[str]] = Field(alias="readme", default=None)
    label: Optional[List[str]] = Field(alias="label", default=None)
    has_assumption: Optional[List[str]] = Field(alias="hasAssumption", default=None)
    has_parameter: Optional[List[Parameter]] = Field(alias="hasParameter", default=None)
    operating_systems: Optional[List[str]] = Field(alias="operatingSystems", default=None)
    has_executable_notebook: Optional[List[str]] = Field(alias="hasExecutableNotebook", default=None)
    has_equation: Optional[List[Equation]] = Field(alias="hasEquation", default=None)
    useful_for_calculating_index: Optional[List[NumericalIndex]] = Field(alias="usefulForCalculatingIndex", default=None)
    has_input: Optional[List[DatasetSpecification]] = Field(alias="hasInput", default=None)
    has_output_variable: Optional[List[VariablePresentation]] = Field(alias="hasOutputVariable", default=None)

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



from openapi_server.models.causal_diagram import CausalDiagram
from openapi_server.models.configuration_setup import ConfigurationSetup
from openapi_server.models.constraint import Constraint
from openapi_server.models.dataset_specification import DatasetSpecification
from openapi_server.models.emulator_copyright_holder_inner import EmulatorCopyrightHolderInner
from openapi_server.models.equation import Equation
from openapi_server.models.funding_information import FundingInformation
from openapi_server.models.grid import Grid
from openapi_server.models.image import Image
from openapi_server.models.model_category import ModelCategory
from openapi_server.models.numerical_index import NumericalIndex
from openapi_server.models.parameter import Parameter
from openapi_server.models.person import Person
from openapi_server.models.process import Process
from openapi_server.models.region import Region
from openapi_server.models.sample_execution import SampleExecution
from openapi_server.models.sample_resource import SampleResource
from openapi_server.models.software import Software
from openapi_server.models.software_image import SoftwareImage
from openapi_server.models.software_version import SoftwareVersion
from openapi_server.models.source_code import SourceCode
from openapi_server.models.time_interval import TimeInterval
from openapi_server.models.variable_presentation import VariablePresentation
from openapi_server.models.visualization import Visualization
ModelConfiguration.update_forward_refs()
