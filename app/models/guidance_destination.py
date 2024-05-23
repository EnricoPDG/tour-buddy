from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, UUID
from database import Base


class GuidanceDestination(Base):
    __tablename__ = "guidance_destination"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(String, nullable=False)
    complement = Column(String, nullable=True)
    guidanceId = Column(UUID(as_uuid=True), ForeignKey("guidance.id"), default=uuid4)
