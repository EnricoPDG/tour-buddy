from sqlalchemy.orm import Session
from models import Guidance, User, GuidanceDestination, GuidanceImage
from schema.guidance_schema import GuidanceSchemaResponse, HolderSchema, GuidanceSchemaRequest
from schema.guidance_destination_schema import GuidanceDestinationSchemaResponse
from schema.guidance_image_schema import GuidanceImageSchemaResponse
import uuid
from typing import List


class GuidanceRepository:
    @staticmethod
    def get_guidances(db: Session, user_id: uuid.UUID = None, guidance_id: uuid.UUID = None) -> list[GuidanceSchemaResponse]:
        arguments = {}
        if guidance_id is not None:
            arguments['id'] = guidance_id
        if user_id is not None:
            arguments['owner_id'] = user_id
        guidances = db.query(Guidance).filter_by(**arguments).all()
        response = []

        for guidance in guidances:
            holder = db.query(User).filter(User.id == guidance.owner_id).first()
            destinations = db.query(GuidanceDestination).filter(GuidanceDestination.guidance_id == guidance.id).all()
            
            destination_responses = []

            for destination in destinations:
                images = db.query(GuidanceImage).filter(GuidanceImage.id_guidance_destination == destination.id).all()
                image_responses = [GuidanceImageSchemaResponse(url=image.url, id=image.id) for image in images]
                destination_responses.append(
                    GuidanceDestinationSchemaResponse(
                        id=destination.id,
                        description=destination.description,
                        cep=destination.cep,
                        state=destination.state,
                        city=destination.city,
                        street=destination.street,
                        neighborhood=destination.neighborhood,
                        number=destination.number,
                        complement=destination.complement,
                        images=image_responses,
                        guidance_id=destination.guidance_id
                    )
                )

            holder_response = HolderSchema(
                id=holder.id,
                name=holder.name,
                username=holder.username,
                image=holder.avatar_url
            )

            guidance_response = GuidanceSchemaResponse(
                id=guidance.id,
                title=guidance.title,
                description=guidance.description,
                # TODO: fazer requisição para buscar o rating
                rating=3.5,
                state=guidance.state,
                city=guidance.city,
                approximately_value=guidance.approximately_value,
                holder=holder_response,
                destinations=destination_responses

            )
            response.append(guidance_response)

        return response

    @staticmethod
    def update_destination_images(db: Session, destination_id: uuid.UUID, image_urls: List[str]):
        for url in image_urls:
            new_image = GuidanceImage(id=str(uuid.uuid4()), url=url, id_guidance_destination=destination_id)
            db.add(new_image)
        
        db.commit()
    
    @staticmethod
    def get_destination_images(db: Session, destination_id: uuid.UUID):
        return db.query(GuidanceImage).filter(GuidanceImage.id_guidance_destination == destination_id).all()
    
    @staticmethod
    def create_guidance(db: Session, guidance_data: GuidanceSchemaRequest) -> GuidanceSchemaResponse:
        new_guidance = Guidance(
            id=uuid.uuid4(),
            title=guidance_data.title,
            description=guidance_data.description,
            state=guidance_data.state,
            city=guidance_data.city,
            approximately_value=guidance_data.approximately_value,
            owner_id=guidance_data.owner_id,
        )
        db.add(new_guidance)

        for destination in guidance_data.destinations:
            new_destination = GuidanceDestination(
                description=destination.description,
                cep=destination.cep,
                state=destination.state,
                city=destination.city,
                street=destination.street,
                neighborhood=destination.neighborhood,
                number=destination.number,
                complement=destination.complement,
                guidance_id=new_guidance.id
            )
            db.add(new_destination)
        db.commit()
        
        return GuidanceRepository.get_guidances(db=db, guidance_id=new_guidance.id)[0]
