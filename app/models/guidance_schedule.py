from uuid import uuid4
from sqlalchemy import Column, DateTime, Boolean, ForeignKey, UUID
from database import Base


class GuidanceSchedule(Base):
    __tablename__ = "guidance_schedule"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    start_date_time = Column(DateTime, nullable=False)
    finish_date_time = Column(DateTime, nullable=False)
    confirmed_by_tourist = Column(Boolean, nullable=False, default=False)
    guide_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=uuid4)
    tourist_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), default=uuid4)
    guidance_id = Column(UUID(as_uuid=True), ForeignKey('guidance.id'), default=uuid4)
