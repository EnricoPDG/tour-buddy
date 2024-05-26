from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from loguru import logger
from repository import RatingRepository
from schema import GuidanceRatingSchemaResponse

router = APIRouter(
    prefix="/ratings"
)


@router.get("/profile/{user_id}", response_model=List[GuidanceRatingSchemaResponse], status_code=200)
async def get_ratings_from_user_id(user_id: UUID, db: Session = Depends(get_db)):
    try:
        ratings = RatingRepository.get_ratings(db=db, user_id=user_id)
        if ratings is None:
            raise HTTPException(status_code=500, detail=f"error: something went wrong")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"get_ratings_from_user_id response: {ratings}")

    return ratings
