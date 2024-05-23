from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema import UserSchemaRequest, UserSchemaResponse
from repository import UserRepository
from database import get_db
from loguru import logger
from uuid import UUID

router = APIRouter()

@router.post("/users", response_model=UserSchemaResponse, status_code=201)
async def create_user(user: UserSchemaRequest, db: Session = Depends(get_db)):
    try:
        logger.debug(f"creating user: {user}")
        user_id = UserRepository.save(db, user)
        if user_id is None:
            raise HTTPException(
                status_code=500,
                detail=f"error: something went wrong"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"error: {e}"
        )
    
    logger.info(f"User response: {create_user}")
    return UserSchemaResponse(
        id=user_id,
        email=user.email,
        name=user.name,
        username=user.username,
        type=user.type,
        cellphone_number=user.cellphone_number,
        birthday=user.birthday,
        cpf=user.cpf,
        avatar_url=user.avatar_url,
        state=user.state,
        city=user.city
    )

@router.get("/users/:id", response_model=UserSchemaResponse, status_code=201)
async def create_user(id: UUID, db: Session = Depends(get_db)):
    try:
        logger.debug(f"getting user by id: {id}")
        user = UserRepository.get_user(db=db, id=id)
        if user is None:
            raise HTTPException(
                status_code=500,
                detail=f"error: something went wrong"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"error: {e}"
        )
    
    logger.info(f"User response: {create_user}")
    return UserSchemaResponse(
        id=id,
        email=user.email,
        name=user.name,
        username=user.username,
        type=user.type,
        cellphone_number=user.cellphone_number,
        birthday=user.birthday,
        cpf=user.cpf,
        avatar_url=user.avatar_url,
        state=user.state,
        city=user.city
    )