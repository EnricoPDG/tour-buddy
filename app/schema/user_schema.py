from pydantic import BaseModel
from enums import UserTypeEnum
from datetime import date
from uuid import UUID
from typing import Optional

class GuideDataSchema(BaseModel):
    guidancesConcludedQuantity: int
    rating: float
    travelPlanQuantity: int
    
class UserSchemaBase(BaseModel):
    email: str
    username: str
    type: UserTypeEnum
    name: str
    description: Optional[str] = None
    cellphone_number: str
    birthday: date
    cpf: Optional[str] = None
    avatar_url: Optional[str] = None
    state: str
    city: str
    guideData: Optional[GuideDataSchema] = None


class UserSchemaRequest(UserSchemaBase): ...


class UserSchemaResponse(UserSchemaBase):
    id: UUID

    class Config:
        orm_mode = True