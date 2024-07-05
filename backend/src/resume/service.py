from fastapi import HTTPException
from sqlalchemy import select

from db import async_session_maker
from resume.models import Resume, ResumeStage
from resume.schemas import ResumeRead, ResumeCreate, ResumeUpdate
from vacancy.schemas import VacancyRead
from logger import logger


async def get_resume_by_id(resume_id: int, user_id: int) -> ResumeRead:
    """Get user resume by resume_id"""
    async with async_session_maker() as session:
        resume = await session.get(Resume, resume_id)

        if not resume:
            logger.warning(f"Resume with id {resume_id} not found for user {user_id}")
            raise HTTPException(status_code=404, detail="Resume not found")
        if resume.user_id != user_id:
            logger.warning(f"Resume with id {resume_id} not found for user {user_id}")
            raise HTTPException(status_code=403, detail="Not enough permissions to read this resume")

        return resume


async def get_resumes_by_user_id(user_id: int) -> list[VacancyRead]:
    """Get user resumes by user_id"""
    async with async_session_maker() as session:
        query = select(Resume.__table__.columns).where(user_id == Resume.user_id)
        resumes = await session.execute(query)
        return resumes.mappings().all()


async def get_vacancy_resumes_by_stage(vacancy_id: int, resume_stage: ResumeStage, user_id: int):
    """Get vacancy resumes by resume_stage"""
    async with async_session_maker() as session:
        query = (
            select(Resume.__table__.columns)
            .where(
                (vacancy_id == Resume.vacancy_id) &
                (user_id == Resume.user_id) &
                (resume_stage == Resume.resume_stage)
            )
        )
        resumes = await session.execute(query)
        return resumes.mappings().all()


async def create_resume(new_resume: ResumeCreate, vacancy_id: int, user_id: int):
    """Create a new resume for current user"""
    async with async_session_maker() as session:
        new_resume = new_resume.model_dump()
        new_resume.update({"user_id": user_id, "vacancy_id": vacancy_id})
        resume = Resume(**new_resume)
        session.add(resume)
        await session.commit()
        return resume


async def delete_resume_by_id(resume_id: int, user_id: int):
    """Delete user resume"""
    async with async_session_maker() as session:
        resume = await get_resume_by_id(resume_id, user_id)
        await session.delete(resume)
        await session.commit()
        return {"success": f"Resume with id {resume.id} deleted."}


async def update_resume(updated_resume: ResumeUpdate, user_id: int) -> ResumeUpdate:
    """Update resume with updated_resume and user_id"""
    async with async_session_maker() as session:
        resume = await get_resume_by_id(updated_resume.id, user_id)
        updated_data = updated_resume.model_dump(exclude_unset=True)
        
        for key, value in updated_data.items():
            setattr(resume, key, value)
        
        session.add(resume)
        await session.commit()
        await session.refresh(resume)
        return resume
