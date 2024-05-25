from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class GuidanceRatingSchemaBase(BaseModel):
    rating: float
    evaluator_id: UUID
    guidance_id: UUID

class GuidanceRatingSchemaRequest(GuidanceRatingSchemaBase):
    pass

class GuidanceRatingSchemaResponse(GuidanceRatingSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
