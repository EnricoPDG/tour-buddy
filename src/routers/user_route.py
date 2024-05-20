from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
def teste():
    return "teste"
