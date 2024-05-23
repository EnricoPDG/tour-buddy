from fastapi import FastAPI
import uvicorn
from routers import user_route
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.router, tags=["User Route"])


@app.get("/")
def teste():
    return {"olá": "mundo"}

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)