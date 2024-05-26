from pydantic import BaseModel
from uuid import UUID
from schema import HolderSchema


class GuidanceRatingSchemaBase(BaseModel):
    rating: float
    evaluator_id: UUID
    guidance_id: UUID
    holder: HolderSchema


class GuidanceRatingSchemaRequest(GuidanceRatingSchemaBase):
    pass


class GuidanceRatingSchemaResponse(GuidanceRatingSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
