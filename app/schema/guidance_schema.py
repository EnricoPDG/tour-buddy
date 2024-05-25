from pydantic import BaseModel
from typing import List 
from enums import UserTypeEnum
from uuid import UUID
from typing import Optional
from schema import GuidanceDestinationSchemaResponse

class Holder(BaseModel):
    id: UUID
    name: str
    username: str
    image: str

class GuidanceSchemaBase(BaseModel):
    title: str
    description: str
    rating: UserTypeEnum
    state: str
    city: Optional[str] = None 
    approximatelyValue: float
    holder: Holder
    destinations: List[GuidanceDestinationSchemaResponse]


class GuidanceSchemaRequest(GuidanceSchemaBase): ...


class GuidanceSchemaResponse(GuidanceSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
