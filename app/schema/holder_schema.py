from pydantic import BaseModel
from uuid import UUID


class HolderSchema(BaseModel):
    id: UUID
    name: str
    username: str
    image: str
