from fastapi import HTTPException
from sqlalchemy import select

from backend.src.db import async_session_maker
from backend.src.vacancy.models import Vacancy
from backend.src.vacancy.schemas import VacancyCreate, VacancyRead


async def get_vacancy_by_id(vacancy_id: int, user_id: int) -> VacancyRead:
    """Get a vacancy by vacancy_id and user_id"""
    async with async_session_maker() as session:
        vacancy = await session.get(Vacancy, vacancy_id)

        if not vacancy:
            raise HTTPException(status_code=404, detail="Vacancy not found")
        if vacancy.user_id != user_id:
            raise HTTPException(status_code=403, detail="Not enough permissions to read this vacancy")

        return vacancy


async def get_vacancies_by_user_id(user_id: int) -> list[VacancyRead]:
    """Get ALL user vacancies by user_id"""
    async with async_session_maker() as session:
        query = select(Vacancy.__table__.columns).where(user_id == Vacancy.user_id)
        sql_response = await session.execute(query)
        vacancies = sql_response.mappings().all()
        return vacancies


async def create_vacancy(new_vacancy: VacancyCreate, user_id: int):
    """Create a new vacancy for current user"""
    async with async_session_maker() as session:
        new_vacancy = new_vacancy.model_dump()
        new_vacancy.update({"user_id": user_id})
        vacancy = Vacancy(**new_vacancy)
        session.add(vacancy)
        await session.commit()
        return vacancy


async def delete_vacancy_by_id(vacancy_id: int, user_id: int):
    """Delete vacancy with vacancy_id and user_id"""
    async with async_session_maker() as session:
        vacancy = await get_vacancy_by_id(vacancy_id, user_id)
        await session.delete(vacancy)
        await session.commit()
        return {"status": f"Vacancy with id {vacancy.id} deleted successfully"}
