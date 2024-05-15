from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.vacancy.models import Vacancy
from src.vacancy.schemas import CreateVacancy

router = APIRouter()


@router.get("/")
async def say_hello():
    return 'Эта вкладка для ВАКАНСИЙ'


@router.post("/")
async def add_vacancy(new_vacancy: CreateVacancy, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
