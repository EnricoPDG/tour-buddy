from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(String, primary_key=True)
    startDateTime = Column(DateTime, nullable=False)
    finishDateTime = Column(DateTime, nullable=False)
    confirmed = Column(Boolean, default=False)

    route_id = Column(String, ForeignKey('route.id'))
    guide_id = Column(String, ForeignKey('user.id'))
    tourist_id = Column(String, ForeignKey('user.id'))

    route = relationship('Route')
    guide = relationship('User', foreign_keys=[guide_id])
    tourist = relationship('User', foreign_keys=[tourist_id], back_populates='schedules')
