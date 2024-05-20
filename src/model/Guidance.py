from src.model.BaseModel import EntityMeta
from sqlalchemy import Column, Integer, String, ForeignKey


class Guidance(EntityMeta):
    __tablename__ = 'guidances'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    approximate_value = Column(String(255), nullable=True)
    owner_user = Column(Integer, ForeignKey("users.id"), nullable=False)
