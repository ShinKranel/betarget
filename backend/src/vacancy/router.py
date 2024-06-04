from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.vacancy.models import Vacancy, WorkFormat
from backend.src.vacancy.schemas import CreateVacancy

router = APIRouter()


@router.get("/")
async def get_vacancies(session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def add_vacancy(new_vacancy: CreateVacancy, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
