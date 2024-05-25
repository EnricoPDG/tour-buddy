from pydantic import BaseModel
from uuid import UUID

class GuidanceSubscriptionSchemaBase(BaseModel):
    id_user_follower: UUID
    id_user_followed: UUID

class GuidanceSubscriptionSchemaRequest(GuidanceSubscriptionSchemaBase):
    pass

class GuidanceSubscriptionSchemaResponse(GuidanceSubscriptionSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
