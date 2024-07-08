from fastapi import APIRouter, Depends
from starlette import status

from user.models import User
from vacancy.schemas import VacancyCreate, VacancyRead, VacancyUpdate
from logger import logger

from auth.base_config import current_user
from vacancy.service import (
    get_vacancies_by_user_id, get_vacancy_by_id, 
    create_vacancy, delete_vacancy_by_id, update_vacancy
)

router = APIRouter()


@router.get("/", response_model=list[VacancyRead])
async def read_user_vacancies(user: User = Depends(current_user)):
    """Get all user vacancies"""
    logger.info(f"Get all user vacancies for user {user}")
    return await get_vacancies_by_user_id(user.id)


@router.get("/{vacancy_id}", response_model=VacancyRead)
async def read_user_vacancy_by_id(vacancy_id: int, user: User = Depends(current_user)):
    """Get vacancy by id"""
    logger.info(f"Get user vacancy with id {vacancy_id} for user {user}")
    return await get_vacancy_by_id(vacancy_id, user.id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VacancyRead)
async def create_user_vacancy(new_vacancy: VacancyCreate, user: User = Depends(current_user)):
    """Create a new vacancy for current user"""
    logger.info(f"Create new user vacancy for user {user}")
    return await create_vacancy(new_vacancy, user.id)


@router.delete("/{vacancy_id}")
async def delete_user_vacancy(vacancy_id: int, user: User = Depends(current_user)) -> dict[str, str]:
    """Delete vacancy."""
    logger.info(f"Delete user vacancy with id {vacancy_id} for user {user}") 
    return await delete_vacancy_by_id(vacancy_id, user.id)


@router.put("/", response_model=VacancyRead)
async def update_user_vacancy(updated_vacancy: VacancyUpdate, user: User = Depends(current_user)):
    """Update vacancy."""
    logger.info(f"Update user vacancy with id {updated_vacancy.id} for user {user}")
    return await update_vacancy(updated_vacancy, user.id)