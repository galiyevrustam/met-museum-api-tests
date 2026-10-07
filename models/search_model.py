"""Pydantic models for the Met Museum search endpoint."""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchResult(BaseModel):
    """Response model for /search and /v1.1/search."""

    model_config = ConfigDict(extra="allow")

    total: int = Field(..., ge=0)
    objectIDs: Optional[List[int]] = Field(default=None)
