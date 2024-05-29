from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from Backend.src.db import get_async_session
from Backend.src.vacancy.models import Vacancy, WorkFormat
from Backend.src.vacancy.schemas import CreateVacancy

router = APIRouter()


@router.get("/")
async def get_vacancy_by_work_format(work_format: WorkFormat, session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy).where(Vacancy.work_format == work_format)
    result = await session.execute(query)
    return {
            "status": "ok",
            "data": result.scalars().all()
    }


@router.post("/")
async def add_vacancy(new_vacancy: CreateVacancy, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
