from sqlalchemy.orm import Session
from models import GuidanceRating, User, Guidance
from schema.guidance_rating_schema import GuidanceRatingSchemaResponse, GuidanceRatingSchemaRequest
import uuid
from sqlalchemy import func


class RatingRepository:

    @staticmethod
    def get_ratings_by_user(db: Session, user_id: uuid.UUID) -> list[GuidanceRatingSchemaResponse]:
        ratings = (db.query(GuidanceRating).
                   join(Guidance, GuidanceRating.guidance_id == Guidance.id)
                   .join(User, User.id == Guidance.owner_id)
                   .filter(User.id == user_id).all()
                   )
        response = []

        for rating in ratings:
            evaluator = db.query(User).filter(User.id == rating.evaluator_id).first()
            evaluator_response = {
                "id": evaluator.id,
                "name": evaluator.name,
                "username": evaluator.username,
                "image": evaluator.avatar_url,
                "type": evaluator.type,
            }
            rating_response = GuidanceRatingSchemaResponse(
                id=rating.id,
                rating=rating.rating,
                description=rating.description,
                evaluator_id=rating.evaluator_id,
                guidance_id=rating.guidance_id,
                ratingHolder=evaluator_response
            )
            response.append(rating_response)

        return response

    @staticmethod
    def get_ratings_by_guidance(db: Session, guidance_id: uuid.UUID) -> list[GuidanceRatingSchemaResponse]:
        ratings = db.query(GuidanceRating).filter(GuidanceRating.guidance_id == guidance_id).all()
        response = []

        for rating in ratings:
            evaluator = db.query(User).filter(User.id == rating.evaluator_id).first()
            evaluator_response = {
                "id": evaluator.id,
                "name": evaluator.name,
                "username": evaluator.username,
                "image": evaluator.avatar_url,
                "type": evaluator.type
            }
            rating_response = GuidanceRatingSchemaResponse(
                id=rating.id,
                rating=rating.rating,
                description=rating.description,
                evaluator_id=rating.evaluator_id,
                guidance_id=rating.guidance_id,
                ratingHolder=evaluator_response
            )
            response.append(rating_response)

        return response

    @staticmethod
    def create_rating(db: Session, guidance_id: uuid.UUID,
                      rating_data: GuidanceRatingSchemaRequest) -> GuidanceRatingSchemaResponse:
        new_rating = GuidanceRating(
            rating=rating_data.rating,
            description=rating_data.description,
            evaluator_id=rating_data.evaluator_id,
            guidance_id=guidance_id
        )
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)

        evaluator = db.query(User).filter(User.id == new_rating.evaluator_id).first()
        evaluator_response = {
            "id": evaluator.id,
            "name": evaluator.name,
            "username": evaluator.username,
            "image": evaluator.avatar_url
        }

        return GuidanceRatingSchemaResponse(
            id=new_rating.id,
            rating=new_rating.rating,
            description=new_rating.description,
            evaluator_id=new_rating.evaluator_id,
            guidance_id=new_rating.guidance_id,
            ratingHolder=evaluator_response
        )

    @staticmethod
    def get_user_rating(db: Session, user_id: str) -> float:
        avg_rating = db.query(func.avg(GuidanceRating.rating)).join(Guidance,
                                                                    Guidance.id == GuidanceRating.guidance_id).filter(
            Guidance.owner_id == user_id).scalar()
        return avg_rating if avg_rating is not None else 3.5
