from sqlalchemy.orm import Session
from models import Guidance, User, GuidanceDestination, GuidanceImage
from schema.guidance_schema import GuidanceSchemaResponse, HolderSchema
from schema.guidance_destination_schema import GuidanceDestinationSchemaResponse
from schema.guidance_image_schema import GuidanceImageSchemaResponse


class GuidanceRepository:
    @staticmethod
    def get_guidances(db: Session) -> list[GuidanceSchemaResponse]:
        guidances = db.query(Guidance).all()
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
                rating=guidance.rating,
                state=guidance.state,
                city=guidance.city,
                approximately_value=guidance.approximately_value,
                holder=holder_response,
                destinations=destination_responses
            )
            response.append(guidance_response)

        return response
