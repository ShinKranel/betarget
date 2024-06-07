import asyncio

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.vacancy.models import Vacancy
from backend.src.vacancy.schemas import VacancyCreate, VacanciesRead

router = APIRouter()


@router.get("/")
async def get_vacancies(session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy)
    result = await session.execute(query)
    vacancies = result.scalars().all()
    return vacancies


@router.get("/{vacancy_id}")
async def get_vacancy_by_id(vacancy_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Vacancy).where(Vacancy.id == vacancy_id)
    result = await session.execute(query)
    vacancies = result.scalars().all()
    return vacancies


@router.post("/")
async def add_vacancy(new_vacancy: VacancyCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/")
async def delete_vacancy(vacancy_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Vacancy).where(Vacancy.id == vacancy_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "vacancy was deleted"}
