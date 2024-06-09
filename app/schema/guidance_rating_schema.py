from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from schema import UserSchemaResponse


class GuidanceRatingSchemaBase(BaseModel):
    rating: float
    evaluator_id: UUID
    guidance_id: UUID
    description: Optional[str] = None

class GuidanceRatingSchemaRequest(GuidanceRatingSchemaBase):
    pass

class GuidanceRatingSchemaResponse(GuidanceRatingSchemaBase):
    id: UUID
    ratingHolder: UserSchemaResponse
    class Config:
        orm_mode = True
