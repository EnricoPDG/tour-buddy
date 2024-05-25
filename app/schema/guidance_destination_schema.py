from pydantic import BaseModel
from typing import List
from uuid import UUID
from typing import Optional
from schema import GuidanceImageSchemaRequest


class GuidanceDestinationSchemaBase(BaseModel):
    description: str
    cep: str
    state: str
    city: str
    street: str
    number: str
    neighborhood: str
    complement: Optional[str] = None
    images: List[GuidanceImageSchemaRequest]
    guidance_id: UUID

class GuidanceDestinationSchemaRequest(GuidanceDestinationSchemaBase): ...


class GuidanceDestinationSchemaResponse(GuidanceDestinationSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
