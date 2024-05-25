from sqlalchemy.orm import Session
from loguru import logger
from models import User
from schema import UserSchemaRequest
from uuid import uuid4, UUID


class UserRepository:
    @staticmethod
    def save(db: Session, user_schema: UserSchemaRequest) -> id:
        logger.debug(f"Setting User.")
        id = uuid4()
        user_model = User(
            id=id,
            email=user_schema.email,
            name=user_schema.name,
            description=user_schema.description,
            username=user_schema.username,
            type=user_schema.type,
            cellphone_number=user_schema.cellphone_number,
            birthday=user_schema.birthday,
            cpf=user_schema.cpf,
            avatar_url=user_schema.avatar_url,
            state=user_schema.state,
            city=user_schema.city,
        )

        logger.debug(f"User created: {user_model.__dict__}")

        if user_model.id:
            db.merge(user_model)
        else:
            db.add(user_model)
        db.commit()

        logger.debug(f"User created in database: {user_model}")
        return id

    @staticmethod
    def get_user(db: Session, id: UUID = None, email: str = None):
        arguments = {}
        if id is not None:
            arguments['id'] = id
        if email is not None:
            arguments['email'] = email
        return db.query(User).filter_by(**arguments).first()
