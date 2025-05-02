from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from enum import Enum

class InputModeEnum(str, Enum):
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    FIXED = "FIXED"

class ArgumentInputModeEnum(str, Enum):
    REQUIRED = "REQUIRED"
    FIXED = "FIXED"
    INCLUDE_ON_DEMAND = "INCLUDE_ON_DEMAND"
    INCLUDE_BY_DEFAULT = "INCLUDE_BY_DEFAULT"

class EnvironmentVariable(BaseModel):
    """Environment variable for job execution."""
    key: str = Field(..., description="Environment variable key")
    value: str = Field(..., description="Environment variable value")

class Argument(BaseModel):
    """Command line argument for job execution."""
    name: str = Field(..., min_length=1, max_length=80, description="Argument name")
    description: Optional[str] = Field(None, max_length=8096, description="Argument description")
    inputMode: ArgumentInputModeEnum = Field(ArgumentInputModeEnum.INCLUDE_ON_DEMAND, description="Input mode for the argument")
    value: Optional[str] = Field(None, description="Argument value")
    order: Optional[int] = Field(None, description="Order of the argument in the command line")

class InputParameter(BaseModel):
    """Input parameter for job execution."""
    name: str = Field(..., min_length=1, max_length=80, description="Parameter name")
    description: Optional[str] = Field(None, max_length=8096, description="Parameter description")
    inputMode: InputModeEnum = Field(InputModeEnum.OPTIONAL, description="Input mode for the parameter")
    value: Optional[str] = Field(None, description="Parameter value")
    required: bool = Field(False, description="Whether the parameter is required")
    order: Optional[int] = Field(None, description="Order of the parameter in the command line")

class FileInput(BaseModel):
    """File input for job execution."""
    name: str = Field(..., min_length=1, max_length=80, description="File input name")
    description: Optional[str] = Field(None, max_length=8096, description="File input description")
    inputMode: InputModeEnum = Field(InputModeEnum.REQUIRED, description="Input mode for the file input")
    autoMountLocal: Optional[bool] = Field(True, description="Whether to automatically mount the file locally")
    envKey: Optional[str] = Field(None, description="Environment variable key for the file input")
    notes: Optional[Dict[str, Any]] = Field(None, description="Additional notes about the file input")
    sourceUrl: Optional[str] = Field(None, description="Source URL for the file input")
    targetPath: Optional[str] = Field(None, description="Target path for the file input")

class ArchiveFilter(BaseModel):
    """Filter for archiving job files."""
    includes: List[str] = Field(default_factory=list, description="Files to include in archive")
    excludes: List[str] = Field(default_factory=list, description="Files to exclude from archive")
    includeLaunchFiles: bool = Field(True, description="Whether to include launch files in archive")

class LogConfig(BaseModel):
    """Configuration for job logging."""
    stdoutFilename: str = Field("", description="Filename for stdout")
    stderrFilename: str = Field("", description="Filename for stderr")

class ParameterSet(BaseModel):
    """Set of parameters for job execution."""
    appArgs: List[Argument] = Field(default_factory=list, description="Application arguments")
    containerArgs: List[Argument] = Field(default_factory=list, description="Container arguments")
    schedulerOptions: List[Argument] = Field(default_factory=list, description="Scheduler options")
    envVariables: List[EnvironmentVariable] = Field(default_factory=list, description="Environment variables")
    archiveFilter: ArchiveFilter = Field(default_factory=ArchiveFilter, description="Archive filter configuration")
    logConfig: LogConfig = Field(default_factory=LogConfig, description="Log configuration")

class JobAttributes(BaseModel):
    """Job attributes for Tapis applications."""
    description: Optional[str] = Field(None, description="Job description")
    dynamicExecSystem: bool = Field(False, description="Whether to use dynamic execution system")
    execSystemConstraints: Optional[Dict[str, Any]] = Field(None, description="Execution system constraints")
    execSystemId: str = Field(..., description="Execution system identifier")
    execSystemExecDir: str = Field(..., description="Execution directory on the system")
    execSystemInputDir: str = Field(..., description="Input directory on the system")
    execSystemOutputDir: str = Field(..., description="Output directory on the system")
    dtnSystemInputDir: Optional[str] = Field(None, description="DTN input directory")
    dtnSystemOutputDir: Optional[str] = Field(None, description="DTN output directory")
    execSystemLogicalQueue: Optional[str] = Field(None, description="Logical queue for execution")
    archiveSystemId: Optional[str] = Field(None, description="Archive system identifier")
    archiveSystemDir: Optional[str] = Field(None, description="Archive directory on the system")
    archiveOnAppError: bool = Field(True, description="Whether to archive on application error")
    isMpi: bool = Field(False, description="Whether the job uses MPI")
    mpiCmd: Optional[str] = Field(None, description="MPI command")
    cmdPrefix: Optional[str] = Field(None, description="Command prefix")
    parameterSet: ParameterSet = Field(default_factory=ParameterSet, description="Parameter set for the job")
    fileInputs: List[FileInput] = Field(default_factory=list, description="File inputs for the job")
    fileInputArrays: List[Any] = Field(default_factory=list, description="File input arrays")
    nodeCount: int = Field(1, description="Number of nodes to use")
    coresPerNode: int = Field(1, description="Cores per node")
    memoryMB: int = Field(1000, description="Memory in MB")
    maxMinutes: int = Field(10, description="Maximum runtime in minutes")
    subscriptions: List[Any] = Field(default_factory=list, description="Job subscriptions")
    tags: List[str] = Field(default_factory=list, description="Job tags")

class TapisApp(BaseModel):
    """Tapis Application model based on OpenAPI v3 spec."""
    sharedAppCtx: Optional[str] = Field(None, min_length=1, max_length=60, description="Shared application context")
    isPublic: bool = Field(False, description="Whether the application is public")
    sharedWithUsers: Optional[List[str]] = Field(None, description="List of users the application is shared with")
    tenant: str = Field(..., description="Tenant identifier")
    id: str = Field(..., min_length=1, max_length=80, description="Application identifier")
    version: str = Field(..., min_length=1, max_length=64, description="Application version")
    description: Optional[str] = Field(None, max_length=2048, description="Application description")
    owner: str = Field(..., min_length=1, max_length=60, description="Application owner")
    enabled: bool = Field(True, description="Whether the application is enabled")
    versionEnabled: bool = Field(True, description="Whether this version is enabled")
    locked: bool = Field(False, description="Whether the application is locked")
    runtime: str = Field(..., description="Runtime environment (SINGULARITY, DOCKER, ZIP)")
    runtimeVersion: Optional[str] = Field(None, description="Runtime version")
    runtimeOptions: Optional[List[str]] = Field(None, description="Runtime options")
    containerImage: str = Field(..., description="Container image for the application")
    jobType: str = Field(..., description="Job type (BATCH, FORK)")
    maxJobs: int = Field(2147483647, description="Maximum number of concurrent jobs")
    maxJobsPerUser: int = Field(2147483647, description="Maximum number of concurrent jobs per user")
    strictFileInputs: bool = Field(False, description="Whether file inputs are strictly enforced")
    jobAttributes: JobAttributes = Field(..., description="Job attributes")
    tags: Optional[List[str]] = Field(None, description="Application tags")
    notes: Optional[Dict[str, Any]] = Field(None, description="Application notes")
    uuid: Optional[UUID] = Field(None, description="Application UUID")
    deleted: bool = Field(False, description="Whether the application is deleted")
    created: Optional[datetime] = Field(None, description="Creation timestamp")
    updated: Optional[datetime] = Field(None, description="Last update timestamp")

    class Config:
        schema_extra = {
            "example": {
                "sharedAppCtx": "mosorio",
                "isPublic": False,
                "sharedWithUsers": ["user1", "user2"],
                "tenant": "portals",
                "id": "modflow-2005",
                "version": "0.0.6",
                "description": "Run an non-interactive script on TACC using docker.",
                "owner": "mosorio",
                "enabled": True,
                "versionEnabled": True,
                "locked": False,
                "runtime": "SINGULARITY",
                "runtimeVersion": None,
                "runtimeOptions": ["SINGULARITY_RUN"],
                "containerImage": "docker://ghcr.io/mosoriob/cookbook-modflow:0.0.4",
                "jobType": "BATCH",
                "maxJobs": 2147483647,
                "maxJobsPerUser": 2147483647,
                "strictFileInputs": False,
                "jobAttributes": {
                    "description": None,
                    "dynamicExecSystem": False,
                    "execSystemId": "ls6",
                    "execSystemExecDir": "${JobWorkingDir}",
                    "execSystemInputDir": "${JobWorkingDir}",
                    "execSystemOutputDir": "${JobWorkingDir}/output",
                    "archiveSystemId": "cloud.data",
                    "archiveSystemDir": "HOST_EVAL($HOME)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}",
                    "archiveOnAppError": True,
                    "isMpi": False,
                    "parameterSet": {
                        "appArgs": [],
                        "containerArgs": [],
                        "schedulerOptions": [
                            {
                                "arg": "--tapis-profile tacc-apptainer",
                                "name": "TACC Scheduler Profile",
                                "description": "Scheduler profile for HPC clusters at TACC",
                                "inputMode": "FIXED",
                                "notes": {"isHidden": True}
                            }
                        ],
                        "envVariables": [],
                        "archiveFilter": {
                            "includes": [],
                            "excludes": [],
                            "includeLaunchFiles": True
                        },
                        "logConfig": {
                            "stdoutFilename": "",
                            "stderrFilename": ""
                        }
                    },
                    "fileInputs": [
                        {
                            "name": "bas6",
                            "description": "Basic Package Input for the Groundwater Flow Process",
                            "inputMode": "REQUIRED",
                            "autoMountLocal": True,
                            "targetPath": "input.ba6"
                        }
                    ],
                    "fileInputArrays": [],
                    "nodeCount": 1,
                    "coresPerNode": 1,
                    "memoryMB": 1000,
                    "maxMinutes": 10,
                    "subscriptions": [],
                    "tags": []
                },
                "tags": ["portalName: ALL"],
                "notes": {
                    "icon": "jupyter",
                    "label": "MODFLOW 2005",
                    "helpUrl": "https://github.com/In-For-Disaster-Analytics/cookbook-conda-template",
                    "category": "Data Processing",
                    "helpText": "Modflow is a popular open-source groundwater flow model distributed by the U.S. Geological survey",
                    "queueFilter": ["development", "normal"],
                    "isInteractive": False,
                    "hideNodeCountAndCoresPerNode": True
                },
                "uuid": "1c6721eb-7f02-412e-a877-906c2e2e3526",
                "deleted": False,
                "created": "2024-06-08T18:56:30.737674Z",
                "updated": "2024-06-08T18:56:30.737674Z"
            }
        }
