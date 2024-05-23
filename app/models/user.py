from uuid import uuid4
from sqlalchemy import Column, String, Enum, Date, Text, UUID
from database import Base
from enums import UserTypeEnum


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(255), nullable=False)
    username = Column(String(60), nullable=False)
    type = Column(Enum(UserTypeEnum))
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    cellphone_number = Column(String(14), nullable=False)
    birthday = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=True)
    avatar_url = Column(Text, nullable=True)
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
