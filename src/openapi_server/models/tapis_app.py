from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID




class TapisApp(BaseModel):
    tenant: Optional[str] = None
    id: Optional[str] = Field(None, min_length=1, max_length=80)
    version: Optional[str] = Field(None, min_length=1, max_length=64)
    description: Optional[str] = Field(None, max_length=2048)
    owner: Optional[str] = Field(None, min_length=1, max_length=60)
    enabled: bool = True
    versionEnabled: bool = True
    locked: bool = False
    isPublic: Optional[bool] = None
    sharedWithUsers: Optional[List[str]] = None
    runtime: Optional[str] = None  # RuntimeEnum
    runtimeVersion: Optional[str] = None
    runtimeOptions: Optional[List[str]] = None  # RuntimeOptions
    containerImage: Optional[str] = None
    jobType: Optional[str] = None  # JobTypeEnum
    maxJobs: int = -1
    maxJobsPerUser: int = -1
    strictFileInputs: bool = False
    jobAttributes: Optional[dict] = None  # JobAttributes
    tags: Optional[List[str]] = None
    notes: Optional[dict] = None
    sharedAppCtx: Optional[str] = Field(None, min_length=1, max_length=60)
    uuid: Optional[UUID] = None
    deleted: Optional[bool] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
