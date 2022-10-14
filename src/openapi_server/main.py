# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)

    The version of the OpenAPI document: v1.8.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from openapi_server.apis.catalog_identifier_api import router as CatalogIdentifierApiRouter
from openapi_server.apis.causal_diagram_api import router as CausalDiagramApiRouter
from openapi_server.apis.configuration_setup_api import router as ConfigurationSetupApiRouter
from openapi_server.apis.constraint_api import router as ConstraintApiRouter
from openapi_server.apis.coupled_model_api import router as CoupledModelApiRouter
from openapi_server.apis.data_transformation_api import router as DataTransformationApiRouter
from openapi_server.apis.data_transformation_setup_api import router as DataTransformationSetupApiRouter
from openapi_server.apis.dataset_specification_api import router as DatasetSpecificationApiRouter
from openapi_server.apis.empirical_model_api import router as EmpiricalModelApiRouter
from openapi_server.apis.emulator_api import router as EmulatorApiRouter
from openapi_server.apis.equation_api import router as EquationApiRouter
from openapi_server.apis.funding_information_api import router as FundingInformationApiRouter
from openapi_server.apis.geo_coordinates_api import router as GeoCoordinatesApiRouter
from openapi_server.apis.geo_shape_api import router as GeoShapeApiRouter
from openapi_server.apis.grid_api import router as GridApiRouter
from openapi_server.apis.hybrid_model_api import router as HybridModelApiRouter
from openapi_server.apis.image_api import router as ImageApiRouter
from openapi_server.apis.intervention_api import router as InterventionApiRouter
from openapi_server.apis.model_api import router as ModelApiRouter
from openapi_server.apis.model_category_api import router as ModelCategoryApiRouter
from openapi_server.apis.model_configuration_api import router as ModelConfigurationApiRouter
from openapi_server.apis.model_configuration_setup_api import router as ModelConfigurationSetupApiRouter
from openapi_server.apis.numerical_index_api import router as NumericalIndexApiRouter
from openapi_server.apis.organization_api import router as OrganizationApiRouter
from openapi_server.apis.parameter_api import router as ParameterApiRouter
from openapi_server.apis.person_api import router as PersonApiRouter
from openapi_server.apis.point_based_grid_api import router as PointBasedGridApiRouter
from openapi_server.apis.process_api import router as ProcessApiRouter
from openapi_server.apis.region_api import router as RegionApiRouter
from openapi_server.apis.sample_collection_api import router as SampleCollectionApiRouter
from openapi_server.apis.sample_execution_api import router as SampleExecutionApiRouter
from openapi_server.apis.sample_resource_api import router as SampleResourceApiRouter
from openapi_server.apis.software_api import router as SoftwareApiRouter
from openapi_server.apis.software_configuration_api import router as SoftwareConfigurationApiRouter
from openapi_server.apis.software_image_api import router as SoftwareImageApiRouter
from openapi_server.apis.software_version_api import router as SoftwareVersionApiRouter
from openapi_server.apis.source_code_api import router as SourceCodeApiRouter
from openapi_server.apis.spatial_resolution_api import router as SpatialResolutionApiRouter
from openapi_server.apis.spatially_distributed_grid_api import router as SpatiallyDistributedGridApiRouter
from openapi_server.apis.standard_variable_api import router as StandardVariableApiRouter
from openapi_server.apis.theory_guided_model_api import router as TheoryGuidedModelApiRouter
from openapi_server.apis.time_interval_api import router as TimeIntervalApiRouter
from openapi_server.apis.unit_api import router as UnitApiRouter
from openapi_server.apis.variable_api import router as VariableApiRouter
from openapi_server.apis.variable_presentation_api import router as VariablePresentationApiRouter
from openapi_server.apis.visualization_api import router as VisualizationApiRouter
from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Model Catalog",
    description="This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)",
    version="v1.8.0",
)

app.include_router(CatalogIdentifierApiRouter)
app.include_router(CausalDiagramApiRouter)
app.include_router(ConfigurationSetupApiRouter)
app.include_router(ConstraintApiRouter)
app.include_router(CoupledModelApiRouter)
app.include_router(DataTransformationApiRouter)
app.include_router(DataTransformationSetupApiRouter)
app.include_router(DatasetSpecificationApiRouter)
app.include_router(EmpiricalModelApiRouter)
app.include_router(EmulatorApiRouter)
app.include_router(EquationApiRouter)
app.include_router(FundingInformationApiRouter)
app.include_router(GeoCoordinatesApiRouter)
app.include_router(GeoShapeApiRouter)
app.include_router(GridApiRouter)
app.include_router(HybridModelApiRouter)
app.include_router(ImageApiRouter)
app.include_router(InterventionApiRouter)
app.include_router(ModelApiRouter)
app.include_router(ModelCategoryApiRouter)
app.include_router(ModelConfigurationApiRouter)
app.include_router(ModelConfigurationSetupApiRouter)
app.include_router(NumericalIndexApiRouter)
app.include_router(OrganizationApiRouter)
app.include_router(ParameterApiRouter)
app.include_router(PersonApiRouter)
app.include_router(PointBasedGridApiRouter)
app.include_router(ProcessApiRouter)
app.include_router(RegionApiRouter)
app.include_router(SampleCollectionApiRouter)
app.include_router(SampleExecutionApiRouter)
app.include_router(SampleResourceApiRouter)
app.include_router(SoftwareApiRouter)
app.include_router(SoftwareConfigurationApiRouter)
app.include_router(SoftwareImageApiRouter)
app.include_router(SoftwareVersionApiRouter)
app.include_router(SourceCodeApiRouter)
app.include_router(SpatialResolutionApiRouter)
app.include_router(SpatiallyDistributedGridApiRouter)
app.include_router(StandardVariableApiRouter)
app.include_router(TheoryGuidedModelApiRouter)
app.include_router(TimeIntervalApiRouter)
app.include_router(UnitApiRouter)
app.include_router(VariableApiRouter)
app.include_router(VariablePresentationApiRouter)
app.include_router(VisualizationApiRouter)
app.include_router(DefaultApiRouter)
