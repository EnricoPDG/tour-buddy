from fastapi import FastAPI
from routers import user_route
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.router, tags=["User Route"])


@app.get("/")
def teste():
    return {"olá": "mundo"}
