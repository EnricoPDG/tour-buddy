from fastapi import FastAPI, Request
import uvicorn
from routers import user_route, guidance_route
from database import Base, engine
from loguru import logger
import sys

logger.remove(0)
logger.add(sys.stderr, level="DEBUG")

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_route.router, tags=["User Route"])
app.include_router(guidance_route.router, tags=["Guidance Route"])


@app.middleware("http")
async def add_utf8_middleware(request: Request, call_next):
    response = await call_next(request)
    if not request.url.path.__contains__("docs"):
        response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.get("/")
def teste():
    return {"olá": "mundo"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
