from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema import GuidanceSchemaResponse, UserSchemaResponse
from typing import List
from repository import GuidanceRepository
from database import get_db
from loguru import logger
from uuid import UUID

router = APIRouter(
    prefix="/guidances"
)


@router.get("", response_model=List[GuidanceSchemaResponse], status_code=201)
async def get_guidances(db: Session = Depends(get_db)):
    try:
        guidances = GuidanceRepository.get_guidances(db=db)
        if guidances is None:
            raise HTTPException(status_code=500, detail=f"error: something went wrong")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"Guidance response: {guidances}")

    return guidances


@router.get("/profile/{user_id}", response_model=List[GuidanceSchemaResponse], status_code=201)
async def get_guidances(user_id: UUID, db: Session = Depends(get_db)):
    try:
        guidances = GuidanceRepository.get_guidances(db=db, user_id=user_id)
        if guidances is None:
            raise HTTPException(status_code=500, detail=f"error: something went wrong")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"Guidance response: {guidances}")

    return guidances
