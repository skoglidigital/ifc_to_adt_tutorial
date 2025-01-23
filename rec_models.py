import uuid
from typing import Optional, Annotated
from enum import Enum
from pydantic import BaseModel, Field, AwareDatetime, AfterValidator, UUID4

class Empty(BaseModel):

    class Config:
        extra = "forbid"


class LastUpdateTime(BaseModel):
    lastUpdateTime: AwareDatetime


class Metadata(BaseModel):
    model: Optional[str] = Field(alias="$model", default=None)
    name: Optional[LastUpdateTime] = None
    identifiers: Optional[LastUpdateTime] = None
    customProperties: Optional[LastUpdateTime] = None
    lastUpdateTime: Optional[AwareDatetime] = Field(
        alias="$lastUpdateTime",default=None)


class CollectionMetadata(Metadata):
    model: str = Field(
        alias="$model", 
        default="dtmi:org:w3id:rec:Collection;1")


class RealEstateMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:RealEstate;1"
        )


class SpaceMetadata(Metadata):
    model: str = Field(
        alias="$model", 
        default="dtmi:org:w3id:rec:Space;1")


class ArchitectureMetadata(Metadata):
    model: str = Field(
        alias="$model", 
        default="dtmi:org:w3id:rec:Architecture;1")
    

class BuildingMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:Building;1"
        )
    

class LevelMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:Level;1"
        )
    

class RoomMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:Room;1"
        )
    

class InformationMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:Information;1"
        )


class ArchitectureCapacityMetadata(Metadata):
    # model: str = Field(
    #     alias="$model",
    #     default="dtmi:org:w3id:rec:ArchitectureCapacity;1"
    #     )
    maxOccupancy: Optional[LastUpdateTime] = None
    seatingCapacity: Optional[LastUpdateTime] = None

    

class ArchitectureAreaMetadata(Metadata):
    # model: Optional[str] = Field(
    #     alias="$model",
    #     default="dtmi:org:w3id:rec:ArchitectureArea;1"
    #     )
    area: Optional[LastUpdateTime] = None
    grossArea: Optional[LastUpdateTime] = None
    rentableArea: Optional[LastUpdateTime] = None
    

class PostalAdressMetadata(Metadata):
    model: str = Field(
        alias="$model",
        default="dtmi:org:w3id:rec:PostalAddress;1"
        )


class Information(BaseModel):
    dtid: Optional[UUID4] = Field(alias="$dtid", default = None)
    name: Optional[str] = ""
    identifiers: Optional[dict] = None
    customProperties: Optional[dict] = {}
    customTags: Optional[dict] = {}
    metadata: InformationMetadata = Field(alias="$metadata")


class ArchitectureArea(Information):
    grossArea: Optional[float] = None
    netArea: Optional[float] = None
    rentableArea: Optional[float] = None
    metadata: ArchitectureAreaMetadata = Field(alias="$metadata",default= ArchitectureAreaMetadata())


class ArchitectureCapacity(Information):
    maxOccupancy: Optional[int] = None
    seatingCapacity: Optional[int] = None
    metadata: ArchitectureCapacityMetadata = Field(alias="$metadata",default=ArchitectureCapacityMetadata())


class PostalAddress(Information):
    addressLine1: Optional[str]
    addressLine2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postalCode: Optional[str]
    region: Optional[str]
    metadata: PostalAdressMetadata = PostalAdressMetadata()


class Collection(BaseModel):
    dtid: Optional[UUID4] = Field(alias="$dtid")
    name: Optional[str] = ""
    identifiers: Optional[dict] = None
    customProperties: Optional[dict] = None
    customTags: Optional[dict] = None
    metadata: CollectionMetadata = Field(alias="$metadata")


class Space(BaseModel):
    dtid: Optional[UUID4] = Field(alias="$dtid")
    name: Optional[str] = ""
    identifiers: Optional[dict] = {}
    customProperties: Optional[dict] = {}
    metadata: SpaceMetadata = Field(alias="$metadata")


class Architecture(Space):
    area: ArchitectureArea = ArchitectureArea()
    capacity: ArchitectureCapacity = ArchitectureCapacity()
    metadata: ArchitectureMetadata = Field(alias="$metadata")
    

class Building(Architecture):
    dtid: Annotated[str, AfterValidator(
        lambda x: "Building-"+str(uuid.UUID(x.replace("Building-", ""),
                                version=4)))] = Field(
                                alias="$dtId",
                                default_factory=lambda: "Building-"+str(uuid.uuid4()))
    name: str
    metadata: BuildingMetadata = Field(
        alias="$metadata",
        default=BuildingMetadata())
    

class Level(Architecture):
    dtid: Annotated[str, AfterValidator(
        lambda x: "Level-"+str(uuid.UUID(x.replace("Level-", ""),
                                version=4)))] = Field(
                                alias="$dtId",
                                default_factory=lambda: "Level-"+str(uuid.uuid4()))
    levelNumber: Optional[int] = None
    name: str
    customProperties: Optional[dict] = {}
    metadata: Optional[LevelMetadata] = Field(
        alias="$metadata",
        default=LevelMetadata())
    

class Room(Architecture):
    dtid: Annotated[str, AfterValidator(
        lambda x: "Room-"+str(uuid.UUID(x.replace("Room-", ""),
                                version=4)))] = Field(
                                alias="$dtId",
                                default_factory=lambda: "Room-"+str(uuid.uuid4()))
    name: str
    customProperties: Optional[dict] = {}
    metadata: Optional[RoomMetadata] = Field(
        alias="$metadata",
        default=RoomMetadata())
    
class Relationship(BaseModel):
    relationshipId: str = Field(alias="$relationshipId")
    sourceId: str = Field(alias="$sourceId")
    targetId: str = Field(alias="$targetId")
    relationshipName: str = Field(alias="$relationshipName")
    etag: str = Field(alias="$etag")



    

    
    





    

