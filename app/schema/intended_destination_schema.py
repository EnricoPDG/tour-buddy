from pydantic import BaseModel
from typing import Optional

class IntendedDestinationSchemaBase(BaseModel):
    state: str
    city: Optional[str] = None
    street: Optional[str] = None

class IntendedDestinationSchemaRequest(IntendedDestinationSchemaBase):
    pass

class IntendedDestinationSchemaResponse(IntendedDestinationSchemaBase):
    id: str

    class Config:
        orm_mode = True
