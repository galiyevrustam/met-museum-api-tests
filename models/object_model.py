"""Pydantic models for the Met Museum object endpoint."""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Constituent(BaseModel):
    """A constituent (artist, maker, etc.) associated with an artwork."""

    model_config = ConfigDict(extra="allow")

    constituentID: Optional[int] = None
    role: Optional[str] = None
    name: Optional[str] = None
    constituentULAN_URL: Optional[str] = None
    constituentWikidata_URL: Optional[str] = None
    gender: Optional[str] = None


class Tag(BaseModel):
    """A subject keyword tag."""

    model_config = ConfigDict(extra="allow")

    term: Optional[str] = None
    AAT_URL: Optional[str] = None
    Wikidata_URL: Optional[str] = None


class Measurement(BaseModel):
    """A single measurement entry."""

    model_config = ConfigDict(extra="allow")

    elementName: Optional[str] = None
    elementDescription: Optional[str] = None
    elementMeasurements: Optional[dict] = None


class ArtObject(BaseModel):
    """A record for an object returned by /objects/{objectID}.

    ``extra="allow"`` lets the model accept any future fields without
    breaking validation.
    """

    model_config = ConfigDict(extra="allow")

    objectID: int = Field(..., ge=0)
    isHighlight: Optional[bool] = None
    accessionNumber: Optional[str] = None
    accessionYear: Optional[str] = None
    isPublicDomain: Optional[bool] = None
    primaryImage: Optional[str] = ""
    primaryImageSmall: Optional[str] = ""
    additionalImages: Optional[List[str]] = Field(default_factory=list)
    constituents: Optional[List[Constituent]] = Field(default_factory=list)
    department: Optional[str] = None
    objectName: Optional[str] = None
    title: Optional[str] = None
    culture: Optional[str] = None
    period: Optional[str] = None
    dynasty: Optional[str] = None
    reign: Optional[str] = None
    portfolio: Optional[str] = None
    artistRole: Optional[str] = None
    artistPrefix: Optional[str] = None
    artistDisplayName: Optional[str] = None
    artistDisplayBio: Optional[str] = None
    artistSuffix: Optional[str] = None
    artistAlphaSort: Optional[str] = None
    artistNationality: Optional[str] = None
    artistBeginDate: Optional[str] = None
    artistEndDate: Optional[str] = None
    artistGender: Optional[str] = None
    artistWikidata_URL: Optional[str] = None
    artistULAN_URL: Optional[str] = None
    objectDate: Optional[str] = None
    objectBeginDate: Optional[int] = None
    objectEndDate: Optional[int] = None
    medium: Optional[str] = None
    dimensions: Optional[str] = None
    dimensionsParsed: Optional[list] = None
    measurements: Optional[List[Measurement]] = Field(default_factory=list)
    creditLine: Optional[str] = None
    geographyType: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    subregion: Optional[str] = None
    locale: Optional[str] = None
    locus: Optional[str] = None
    excavation: Optional[str] = None
    river: Optional[str] = None
    classification: Optional[str] = None
    rightsAndReproduction: Optional[str] = None
    linkResource: Optional[str] = None
    metadataDate: Optional[str] = None
    repository: Optional[str] = None
    objectURL: Optional[str] = None
    tags: Optional[List[Tag]] = Field(default_factory=list)
    objectWikidata_URL: Optional[str] = None
    isTimelineWork: Optional[bool] = None
    GalleryNumber: Optional[str] = None
