from sqlalchemy.orm import Session
from sqlalchemy.future import select
from loguru import logger
from models import User, GuidanceSubscription
from schema import UserSchemaRequest, UserSchemaResponse
from uuid import uuid4, UUID
from typing import List, Optional
from sqlalchemy import or_


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
    def get_user(db: Session, user_id: UUID = None, email: str = None):
        arguments = {}
        if user_id is not None:
            arguments['id'] = user_id
        if email is not None:
            arguments['email'] = email
        return db.query(User).filter_by(**arguments).first()

    @staticmethod
    def upload_avatar_url(db: Session, email: str, avatar_url: str):

        user = db.query(User).filter(User.email == email).first()

        if user:
            user.avatar_url = avatar_url
            db.commit()
            db.refresh(user)
            return avatar_url
        else:
            return None
        
    @staticmethod
    def search_users(db: Session, search_text: Optional[str] = None) -> List[UserSchemaResponse]:
        query = db.query(User)

        if search_text:
            search_text = f"%{search_text}%"
            query = query.filter(
                or_(
                    User.name.ilike(search_text),
                    User.username.ilike(search_text)
                )
            )

        users = query.all()
        response = []

        for user in users:
            user_response = UserSchemaResponse(
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
                city=user.city
            )
            response.append(user_response)

        return response

    @staticmethod
    def follow_user(db: Session, follower: str, followed: str) -> None:
        subscription = GuidanceSubscription(
            id=uuid4(),
            id_user_follower=follower,
            id_user_followed=followed
        )

        db.add(subscription)
        db.commit()
        return None
