from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Rating(Base):
    __tablename__ = 'rating'
    id = Column(String, primary_key=True)
    grade = Column(Float, nullable=False)
    evaluator_id = Column(String, ForeignKey('user.id'))
    evaluated_id = Column(String, ForeignKey('route.id'))

    evaluator = relationship('User', back_populates='ratings')
    evaluated = relationship('Route', back_populates='ratings')
