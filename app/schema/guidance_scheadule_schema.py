from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class GuidanceScheduleSchemaBase(BaseModel):
    start_datetime: datetime
    finish_datetime: datetime
    confirmed_by_tourist: bool
    guide_id: UUID
    tourist_id: UUID
    guidance_id: UUID

class GuidanceScheduleSchemaRequest(GuidanceScheduleSchemaBase):
    pass

class GuidanceScheduleSchemaResponse(GuidanceScheduleSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
