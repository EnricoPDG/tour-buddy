from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, UUID
from database import Base


class GuidanceImage(Base):
    __tablename__ = 'guidance_image'
    id = Column(String, primary_key=True)
    url = Column(String, nullable=False)
    idGuidanceDestination = Column(UUID(as_uuid=True), ForeignKey('guidance_destination.id'), default=uuid4)
