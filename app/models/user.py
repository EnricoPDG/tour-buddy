from sqlalchemy import Column, String, Enum, Integer, DateTime
from sqlalchemy.orm import relationship
from base import Base
import enum

class UserType(enum.Enum):
    Guide = "guide"
    Traveler = "traveler"

class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    type = Column(Enum(UserType), nullable=False)
    name = Column(String, nullable=False)
    cellphone = Column(String)
    birthDate = Column(DateTime)
    cpf = Column(String)
    urlAvatar = Column(String)
    state = Column(String)
    city = Column(String)
    followers = Column(Integer)
    following = Column(Integer)

    routes = relationship('Route', back_populates='owner')
    ratings = relationship('Rating', back_populates='evaluator')
    schedules = relationship('Schedule', back_populates='tourist')
