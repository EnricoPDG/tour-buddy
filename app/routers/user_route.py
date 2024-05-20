from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def teste():
    return "teste"

@router.get("/user")
def teste():
    return "teste"
