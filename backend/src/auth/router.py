from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def say_hello():
    return 'Эта вкладка для ЛОГИНА'
