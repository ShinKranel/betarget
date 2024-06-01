from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.auth.base_config import current_user
from backend.src.auth.models import User
from backend.src.db import get_async_session
from backend.src.vacancy.models import Vacancy
from backend.src.vacancy.schemas import CreateVacancy

router = APIRouter()


@router.get("/")
async def get_user_vacancies(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy).where(Vacancy.user_id == user.id)
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
