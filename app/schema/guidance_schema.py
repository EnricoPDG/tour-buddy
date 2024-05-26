from pydantic import BaseModel
from typing import List
from uuid import UUID
from typing import Optional
from schema import HolderSchema, GuidanceDestinationSchemaResponse


class GuidanceSchemaBase(BaseModel):
    title: str
    description: str
    rating: float
    state: str
    city: Optional[str] = None
    approximately_value: float
    holder: HolderSchema
    destinations: List[GuidanceDestinationSchemaResponse]


class GuidanceSchemaRequest(GuidanceSchemaBase): ...


class GuidanceSchemaResponse(GuidanceSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
