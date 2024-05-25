from pydantic import BaseModel
from typing import List
from uuid import UUID
from typing import Optional
import schema.guidance_image_schema

class GuidanceDestinationSchemaBase(BaseModel):
    description: str
    cep: str
    state: str
    city: str
    street: str
    number: str
    neighborhood: str
    complement: Optional[str] = None
    images: List[schema.guidance_image_schema.GuidanceImageSchemaResponse]
    guidance_id: UUID

class GuidanceDestinationSchemaRequest(GuidanceDestinationSchemaBase): ...


class GuidanceDestinationSchemaResponse(GuidanceDestinationSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
