from pydantic import BaseModel
from enums import UserTypeEnum
from datetime import date
from uuid import UUID


class UserSchemaBase(BaseModel):
    email: str
    username: str
    type: UserTypeEnum
    name: str
    description: str | None
    cellphone_number: str
    birthday: date
    cpf: str
    avatar_url: str
    state: str
    city: str


class UserSchemaRequest(UserSchemaBase): ...


class UserSchemaResponse(UserSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
