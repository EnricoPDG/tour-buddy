from fastapi import FastAPI
from app.routers import user_route
from mangum import Mangum

app = FastAPI()

app.include_router(user_route.router)
