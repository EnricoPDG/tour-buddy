from fastapi import FastAPI
from routers import user_route
from mangum import Mangum
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.router, tags=["User Route"])

handler = Mangum(app)