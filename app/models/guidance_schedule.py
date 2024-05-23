from uuid import uuid4
from sqlalchemy import Column, DateTime, Boolean, ForeignKey, UUID
from app.database import Base


class GuidanceSchedule(Base):
    __tablename__ = 'guidance_schedule'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    startDateTime = Column(DateTime, nullable=False)
    finishDateTime = Column(DateTime, nullable=False)
    confirmedByTourist = Column(Boolean, nullable=False, default=False)
    guideId = Column(UUID(as_uuid=True), ForeignKey('user.id'), default=uuid4)
    touristId = Column(UUID(as_uuid=True), ForeignKey('user.id'), default=uuid4)
    guidanceId = Column(UUID(as_uuid=True), ForeignKey('route.id'), default=uuid4)
