from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status

from backend.src.auth.base_config import current_user
from backend.src.auth.models import User
from backend.src.db import get_async_session
from backend.src.resume.models import Resume
from backend.src.resume.schemas import ResumeCreate, ResumeRead
from backend.src.vacancy.models import Vacancy

router = APIRouter()


@router.get(
    "/",
    name="resume:read_user_resumes"
)
async def get_user_resumes(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    query = select(Resume).where(user.id == Resume.user_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{resume_id}", response_model=ResumeRead)
async def get_resume_by_id(
        resume_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    resume = await session.get(Resume, resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    if resume.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return resume


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    name="create_resume"
)
async def create_resume(
        new_resume: ResumeCreate,
        vacancy_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Create a new resume.
    """
    vacancy = await session.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    if vacancy.user_id != user.id:
        raise HTTPException(status_code=403, detail="This is not user vacancy")
    new_resume = new_resume.dict()
    new_resume.update({"user_id": user.id, "vacancy_id": vacancy_id})
    stmt = insert(Resume).values(**new_resume)
    await session.execute(stmt)
    await session.commit()
    return {"status": "Resume created"}


@router.delete(
    "/{resume_id}",
    name="delete_resume"
)
async def delete_resume(
        resume_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Delete resume.
    """
    resume = await session.get(Resume, resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    if resume.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    await session.delete(resume)
    await session.commit()
    return {"status": "Resume deleted"}
