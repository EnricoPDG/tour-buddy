from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Route(Base):
    __tablename__ = 'route'
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    state = Column(String)
    city = Column(String)
    aproxPrice = Column(Float)
    averageRating = Column(Float)

    owner_id = Column(String, ForeignKey('user.id'))
    owner = relationship('User', back_populates='routes')
    ratings = relationship('Rating', back_populates='evaluated')
    destinations = relationship('DestinyRoute', back_populates='route')

class DestinyRoute(Base):
    __tablename__ = 'destiny_route'
    id = Column(String, primary_key=True)
    desc = Column(String)
    cep = Column(String)
    state = Column(String)
    city = Column(String)
    street = Column(String)
    number = Column(String)
    complement = Column(String)
    imageUrl = relationship('RouteImage', back_populates='destiny_route')

    route_id = Column(String, ForeignKey('route.id'))
    route = relationship('Route', back_populates='destinations')

class RouteImage(Base):
    __tablename__ = 'route_iamge'
    id = Column(String, primary_key=True)
    url = Column(String, nullable=False)

    destiny_route_id = Column(String, ForeignKey('destiny_route.id'))
    destiny_route = relationship('DestinyRoute', back_populates='imageUrl')

class InterestedDestiny(Base):
    __tablename__ = 'interested_destiny'
    id = Column(String, primary_key=True)
    state = Column(String)
    city = Column(String)
    street = Column(String)    