from sqlalchemy.orm import Session
from loguru import logger
import models
from typing import List


class GuidanceRepository:
    @staticmethod
    def get_guidances(db: Session) -> List[models.Guidance]:
        logger.debug(f"Getting guidances.")
        return db.query(models.Guidance).all()