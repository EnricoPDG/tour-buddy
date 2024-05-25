from uuid import uuid4
from sqlalchemy import Column, Float, ForeignKey, UUID
from database import Base


class GuidanceRating(Base):
    __tablename__ = "guidance_rating"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rating = Column(Float, nullable=False)
    evaluator_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=uuid4)
    guidance_id = Column(UUID(as_uuid=True), ForeignKey("guidance.id"), default=uuid4)
