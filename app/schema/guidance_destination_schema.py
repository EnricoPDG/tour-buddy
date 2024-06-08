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
    guidance_id: Optional[UUID] = None


class GuidanceDestinationSchemaRequest(GuidanceDestinationSchemaBase):
    pass


class GuidanceDestinationSchemaResponse(GuidanceDestinationSchemaBase):
    id: UUID
    images: List[schema.guidance_image_schema.GuidanceImageSchemaResponse]

    class Config:
        orm_mode = True
