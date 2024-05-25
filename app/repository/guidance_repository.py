from sqlalchemy.orm import Session
from loguru import logger
from models import User, Guidance
from typing import List
from schema import UserSchemaRequest
from uuid import uuid4, UUID


class GuidanceRepository:
    @staticmethod
    def get_guidances(db: Session) -> List[Guidance]:
        logger.debug(f"Getting guidances.")
        return db.query(Guidance).all()

    @staticmethod
    def get_ser(db: Session, id: UUID = None, email: str = None):
        arguments = {}
        if id is not None:
            arguments['id'] = id
        if email is not None:
            arguments['email'] = email
        return db.query(User).filter_by(**arguments).first()
