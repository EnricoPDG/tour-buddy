from pydantic import BaseModel
from typing import List, Dict
from enums import UserTypeEnum
from uuid import UUID
from typing import Optional
import schema.guidance_destination_schema as g
import schema.user_schema as u


class GuidanceSchemaBase(BaseModel):
    title: str
    description: str
    rating: float
    state: str
    city: Optional[str] = None 
    approximatelyValue: float
    holder: u.UserSchemaResponse
    destinations: List[g.GuidanceDestinationSchemaResponse]


class GuidanceSchemaRequest(GuidanceSchemaBase): ...


class GuidanceSchemaResponse(GuidanceSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
