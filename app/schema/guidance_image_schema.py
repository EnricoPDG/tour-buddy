from pydantic import BaseModel
from uuid import UUID

class GuidanceImageSchemaBase(BaseModel):
    url: str

class GuidanceImageSchemaRequest(GuidanceImageSchemaBase): ...


class GuidanceImageSchemaResponse(GuidanceImageSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
