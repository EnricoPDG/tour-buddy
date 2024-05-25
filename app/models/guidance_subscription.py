from uuid import uuid4
from sqlalchemy import Column, ForeignKey, UUID
from database import Base

class GuidanceSubscription(Base):
    __tablename__ = "guidance_subscription"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_user_follower = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    id_user_followed = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
