from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from schema import GuidanceSchemaResponse, UserSchemaResponse
from typing import List
from repository import GuidanceRepository
from database import get_db
from loguru import logger
import uuid
from utils import AWS

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
async def get_guidances(user_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        guidances = GuidanceRepository.get_guidances(db=db, user_id=user_id)
        if guidances is None:
            raise HTTPException(status_code=500, detail=f"error: something went wrong")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"Guidance response: {guidances}")

    return guidances


@router.post("/update-destinations-images/{destination_id}", status_code=201)
async def update_destinations_images(destination_id: uuid.UUID, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    try:
        logger.debug(f"Received request to update images for destination ID: {destination_id}")
        s3_image_urls = AWS.send_images_to_s3(files=files, destination_id=destination_id)
        GuidanceRepository.update_destination_images(db=db, destination_id=destination_id, image_urls=s3_image_urls)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    
    logger.info(f"Images for destination ID {destination_id} updated successfully")
    return {"message": "Images updated successfully", "image_urls": s3_image_urls}


@router.get("/destination-images/{destination_id}", response_model=List[str])
async def get_destination_images(destination_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Received request to get images for destination ID: {destination_id}")
        images = GuidanceRepository.get_destination_images(db=db, destination_id=destination_id)
        if not images:
            raise HTTPException(status_code=404, detail="No images found for the given destination ID")

        image_urls = [image.url for image in images]
    except Exception as e:
        logger.error(f"Error retrieving images: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    
    logger.info(f"Successfully retrieved images for destination ID: {destination_id}")
    return image_urls