from uuid import uuid4
from sqlalchemy import Column, String, Float, ForeignKey, UUID
from database import Base


class Guidance(Base):
    __tablename__ = "guidance"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    approximately_value = Column(Float, nullable=True)
    rating = Column(Float, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=uuid4)
