import enum
from src.model.BaseModel import EntityMeta
from sqlalchemy import Column, Integer, String, Enum, Date, Text


class UserTypeEnum(enum.Enum):
    tourist = 'turista'
    guide = 'guia'


class User(EntityMeta):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(60), nullable=False)
    type = Column(Enum(UserTypeEnum))
    name = Column(String(255), nullable=False)
    cellphone_number = Column(String(14), nullable=False)
    birthday = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=True)
    avatar_url = Column(Text, nullable=True)
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
