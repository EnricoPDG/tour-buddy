from pydantic import BaseModel
from typing import List
from uuid import UUID
from typing import Optional
import schema.guidance_destination_schema as g


class HolderSchema(BaseModel):
    id: UUID
    name: str
    username: str
    image: Optional[str] = None


class GuidanceSchemaBase(BaseModel):
    title: str
    description: str
    state: str
    city: Optional[str] = None
    approximately_value: float
    destinations: List[g.GuidanceDestinationSchemaBase]


class GuidanceSchemaRequest(GuidanceSchemaBase):
    owner_id: UUID


class GuidanceSchemaResponse(GuidanceSchemaBase):
    id: UUID
    holder: HolderSchema
    rating: float
    destinations: List[g.GuidanceDestinationSchemaResponse]

    class Config:
        orm_mode = True
