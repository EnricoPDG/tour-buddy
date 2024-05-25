from pydantic import BaseModel
from typing import List
from uuid import UUID
from typing import Optional
import schema.guidance_destination_schema as g

class HolderSchema(BaseModel):
    id: UUID
    name: str
    username: str
    image: str

class GuidanceSchemaBase(BaseModel):
    title: str
    description: str
    rating: float
    state: str
    city: Optional[str] = None 
    approximately_value: float
    holder: HolderSchema
    destinations: List[g.GuidanceDestinationSchemaResponse]


class GuidanceSchemaRequest(GuidanceSchemaBase): ...


class GuidanceSchemaResponse(GuidanceSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
