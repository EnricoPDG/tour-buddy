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
    email: Optional[str] = None
    username: Optional[str] = None
    type: UserTypeEnum
    name: Optional[str] = None
    description: Optional[str] = None
    cellphone_number: Optional[str] = None
    birthday: Optional[date] = None
    cpf: Optional[str] = None
    avatar_url: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    guideData: Optional[GuideDataSchema] = None


class UserSchemaRequest(UserSchemaBase):
    pass


class UserSchemaResponse(UserSchemaBase):
    id: UUID

    class Config:
        orm_mode = True