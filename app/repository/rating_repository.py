from sqlalchemy.orm import Session
from uuid import UUID
from models import GuidanceRating
from schema import GuidanceRatingSchemaResponse


class RatingRepository:
    @staticmethod
    def get_ratings(db: Session, user_id: UUID = None) -> list[GuidanceRatingSchemaResponse]:
        arguments = {}
        if user_id is not None:
            arguments['id'] = user_id
        ratings = db.query(GuidanceRating).filter_by(**arguments).all()
        response = []
