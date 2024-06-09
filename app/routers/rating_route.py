from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema.guidance_rating_schema import GuidanceRatingSchemaResponse, GuidanceRatingSchemaRequest
from typing import List
from repository import RatingRepository
from database import get_db
from loguru import logger
import uuid

router = APIRouter(
    prefix="/ratings"
)


@router.get("/profile/{user_id}", response_model=List[GuidanceRatingSchemaResponse], status_code=200)
async def get_ratings_by_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Received request to fetch ratings for user ID: {user_id}")
        ratings = RatingRepository.get_ratings_by_user(db=db, user_id=user_id)
        if ratings is None:
            raise HTTPException(status_code=404, detail="No ratings found")
    except Exception as e:
        logger.error(f"Error fetching ratings for user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return ratings


@router.get("/guidances/{guidance_id}", response_model=List[GuidanceRatingSchemaResponse], status_code=200)
async def get_ratings_by_guidance(guidance_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Received request to fetch ratings for guidance ID: {guidance_id}")
        ratings = RatingRepository.get_ratings_by_guidance(db=db, guidance_id=guidance_id)
        if ratings is None:
            raise HTTPException(status_code=404, detail="No ratings found")
    except Exception as e:
        logger.error(f"Error fetching ratings for guidance: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return ratings


@router.post("/{guidance_id}", response_model=GuidanceRatingSchemaResponse, status_code=201)
async def create_rating(guidance_id: uuid.UUID, rating: GuidanceRatingSchemaRequest, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Received request to create rating for guidance ID: {guidance_id}")
        new_rating = RatingRepository.create_rating(db=db, guidance_id=guidance_id, rating_data=rating)
    except Exception as e:
        logger.error(f"Error creating rating: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    return new_rating
