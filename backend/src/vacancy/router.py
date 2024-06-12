from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.src.auth.models import User
from backend.src.db import get_async_session
from backend.src.vacancy.models import Vacancy
from backend.src.vacancy.schemas import VacancyCreate, VacancyRead

from backend.src.auth.base_config import current_user

router = APIRouter()


@router.get(
    "/",
    name="read_user_vacancies"
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
    name="read_vacancy_by_id",
    response_model=VacancyRead
)
async def read_vacancy_by_id(
        vacancy_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    vacancy = await session.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    if vacancy.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return vacancy


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    name="create_vacancy"
)
async def create_vacancy(
        new_vacancy: VacancyCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Create a new vacancy.
    """
    new_vacancy = new_vacancy.dict()
    new_vacancy.update({"user_id": user.id})
    stmt = insert(Vacancy).values(**new_vacancy)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete(
    "/{vacancy_id}",
    name="delete_vacancy"
)
async def delete_vacancy(
        vacancy_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Delete vacancy.
    """
    vacancy = await session.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    if vacancy.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    await session.delete(vacancy)
    await session.commit()
    return {"status": "Vacancy deleted successfully"}
