from fastapi import APIRouter, Depends

from starlette import status

from backend.src.auth.base_config import current_user
from backend.src.auth.models import User
from backend.src.vacancy.service import get_vacancy_by_id

from .models import ResumeStage
from .schemas import ResumeCreate, ResumeRead, ResumeUpdate
from .service import (
    get_resume_by_id, get_resumes_by_user_id, 
    get_vacancy_resumes_by_stage, create_resume,
    delete_resume_by_id, update_resume
)

router = APIRouter()


@router.get("/", response_model=list[ResumeRead])
async def get_user_resumes(
        vacancy_id: int | None = None,
        resume_stage: ResumeStage = "in_work",
        user: User = Depends(current_user)
):
    """
    Return user resumes.

    If vacancy_id is None - get ALL user resumes.
    If vacancy_id is NOT None - get vacancy_id resumes by resume_stage filter
    """
    if not vacancy_id:
        return await get_resumes_by_user_id(user.id)

    return await get_vacancy_resumes_by_stage(vacancy_id, resume_stage, user.id)


@router.get("/{resume_id}", response_model=ResumeRead)
async def get_user_resume(resume_id: int, user: User = Depends(current_user)):
    """Get user resume by id"""
    return await get_resume_by_id(resume_id, user.id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResumeRead)
async def create_user_resume(
        new_resume: ResumeCreate,
        vacancy_id: int,
        user: User = Depends(current_user)
):
    """Creates a new resume."""
    await get_vacancy_by_id(vacancy_id, user.id)
    return await create_resume(new_resume, vacancy_id, user.id)


@router.delete("/{resume_id}")
async def delete_resume(resume_id: int, user: User = Depends(current_user)):
    """Delete user resume by id."""
    return await delete_resume_by_id(resume_id, user.id)


@router.put("/", response_model=ResumeRead)
async def update_user_resume(updated_resume: ResumeUpdate, user: User = Depends(current_user)):
    """Update resume"""
    return await update_resume(updated_resume, user.id)