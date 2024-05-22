from sqlalchemy.orm import Session
from loguru import logger
from model import UserModel
from schema import UserSchemaRequest
from uuid import uuid4, UUID

class UserRepository:
    @staticmethod
    def save(db: Session, user_schema: UserSchemaRequest) -> id:
        logger.debug(f"Setting UserModel.")
        id = uuid4()
        user_model = UserModel(
            id=id,
            email=user_schema.email,
            name=user_schema.name,
            username=user_schema.username,
            type=user_schema.type,
            cellphone_number=user_schema.cellphone_number,
            birthday=user_schema.birthday,
            cpf=user_schema.cpf,
            avatar_url=user_schema.avatar_url,
            state=user_schema.state,
            city=user_schema.city
        )

        logger.debug(f"UserModel created: {user_model.__dict__}")

        if user_model.id:
            db.merge(user_model)
        else:
            db.add(user_model)
        db.commit()

        logger.debug(f"User created in database: {user_model}")
        return id
    

    @staticmethod
    def get_user(db: Session, id: UUID):
        return db.query(UserModel).filter_by(id=id).first()