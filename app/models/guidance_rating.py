from uuid import uuid4
from sqlalchemy import Column, Float, ForeignKey, UUID
from app.database import Base


class GuidanceRating(Base):
    __tablename__ = 'guidance_rating'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rating = Column(Float, nullable=False)
    evaluatorId = Column(UUID(as_uuid=True), ForeignKey('user.id'), default=uuid4)
    guidanceId = Column(UUID(as_uuid=True), ForeignKey('guidance.id'), default=uuid4)
