from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from schema import UserSchemaRequest, UserSchemaResponse
from repository import UserRepository
from database import get_db
from loguru import logger
from utils import AWS

router = APIRouter(
    prefix="/users"
)


@router.post("", response_model=UserSchemaResponse, status_code=201)
async def create_user(user: UserSchemaRequest, db: Session = Depends(get_db)):
    try:
        logger.debug(f"creating user: {user}")
        user_id = UserRepository.save(db, user)
        if user_id is None:
            raise HTTPException(status_code=500, detail=f"error: something went wrong")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"User response: {create_user}")
    return UserSchemaResponse(
        id=user_id,
        email=user.email,
        name=user.name,
        username=user.username,
        type=user.type,
        cellphone_number=user.cellphone_number,
        birthday=user.birthday,
        description=user.description,
        cpf=user.cpf,
        avatar_url=user.avatar_url,
        state=user.state,
        city=user.city,
    )


@router.get("/profile/{user_id}", response_model=UserSchemaResponse, status_code=200)
async def fetch_user_profile_by_id(user_id: str, db: Session = Depends(get_db)):
    try:
        user = UserRepository.get_user(db=db, user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f"Erro: o usuário não foi encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"User response: {create_user}")
    return UserSchemaResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        username=user.username,
        type=user.type,
        cellphone_number=user.cellphone_number,
        birthday=user.birthday,
        cpf=user.cpf,
        avatar_url=user.avatar_url,
        state=user.state,
        city=user.city,

    )


@router.get("/{email}", response_model=UserSchemaResponse, status_code=200)
async def fetch_user_profile_by_email(email: str, db: Session = Depends(get_db)):
    try:
        user = UserRepository.get_user(db=db, email=email)
        if user is None:
            raise HTTPException(status_code=404, detail=f"Erro: o usuário não foi encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

    logger.info(f"User response: {create_user}")
    return UserSchemaResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        username=user.username,
        type=user.type,
        cellphone_number=user.cellphone_number,
        birthday=user.birthday,
        cpf=user.cpf,
        avatar_url=user.avatar_url,
        state=user.state,
        city=user.city,
    )


@router.post("/upload-avatar-image/{email}", response_model_include={"avatar_url"}, status_code=201)
async def upload_avatar_image(email: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        logger.debug(f"receveid request upload_avatar_image")
        s3_image_url = AWS.send_image_s3_bucket(file=file, email=email)
        avatar_url = UserRepository.upload_avatar_url(db=db, email=email, avatar_url=s3_image_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")
    
    logger.info(f"User avatar_url: {avatar_url}")
    return {"avatar_url": avatar_url}