"""Pydantic models for the Met Museum departments endpoint."""

from typing import List

from pydantic import BaseModel, ConfigDict, Field


class Department(BaseModel):
    model_config = ConfigDict(extra="allow")

    departmentId: int
    displayName: str


class DepartmentsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    departments: List[Department] = Field(default_factory=list)
