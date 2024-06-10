from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.src.auth.models import User
from backend.src.db import get_async_session
from backend.src.vacancy.models import Vacancy
from backend.src.vacancy.schemas import VacancyCreate

from backend.src.auth.base_config import current_user

router = APIRouter()


@router.get(
    "/",
    name="vacancy:read_user_vacancies"
)
async def read_user_vacancies(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = select(Vacancy).where(user.id == Vacancy.user_id)
    result = await session.execute(query)
    vacancies = result.scalars().all()
    return vacancies


@router.get(
    "/{vacancy_id}",
    name="vacancy:read_user_vacancy"
)
async def read_user_vacancy(vacancy_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy).where(vacancy_id == Vacancy.id)
    result = await session.execute(query)
    vacancies = result.scalars().all()
    return vacancies


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    name="vacancy:create-vacancy"
)
async def create_vacancy(
        new_vacancy: VacancyCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    new_vacancy = new_vacancy.dict()
    new_vacancy.update({"user_id": user.id})
    stmt = insert(Vacancy).values(**new_vacancy)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete(
    "/",
    name="vacancy:delete_vacancy"
)
async def delete_vacancy(vacancy_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Vacancy).where(vacancy_id == Vacancy.id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "vacancy was deleted"}
