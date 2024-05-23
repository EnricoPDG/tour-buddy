from sqlalchemy import String, Column

from app.database import Base


class IntendedDestination(Base):
    __tablename__ = 'intended_destination'
    id = Column(String, primary_key=True)
    state = Column(String, nullable=False)
    city = Column(String, nullable=True)
    street = Column(String, nullable=True)
