from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from db import async_session_maker
from resume.models import Resume, ResumeStage, Candidate
from resume.schemas import  (
    ResumeRead, ResumeCreate, ResumeUpdate, 
    CandidateCreate, CandidateRead, CandidateUpdate
)
from vacancy.models import Vacancy
from logger import logger


# Candidate CRUD methods --------------------------------
async def get_candidate_by_id(candidate_id: int) -> CandidateRead:
    """Get candidate by candidate_id"""
    async with async_session_maker() as session:
        candidate = await session.get(Candidate, candidate_id)
        if not candidate:
            logger.warning(f"Candidate with id {candidate_id} not found")
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate


async def create_candidate(new_candidate: CandidateCreate) -> CandidateRead:
    """Create a new candidate"""
    async with async_session_maker() as session:
        candidate = Candidate(**new_candidate.model_dump())
        session.add(candidate)
        await session.commit()
        await session.refresh(candidate)
        return candidate


async def update_candidate(updated_candidate: CandidateUpdate) -> CandidateRead:
    """Update candidate information"""
    async with async_session_maker() as session:
        candidate = await session.get(Candidate, updated_candidate.id)
        if not candidate:
            logger.warning(f"Candidate with id {updated_candidate.id} not found")
            raise HTTPException(status_code=404, detail="Candidate not found")

        updated_data = updated_candidate.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(candidate, key, value)

        session.add(candidate)
        await session.commit()
        await session.refresh(candidate)
        return candidate


async def delete_candidate(candidate_id: int) -> dict:
    """Delete candidate by candidate_id"""
    async with async_session_maker() as session:
        candidate = await session.get(Candidate, candidate_id)
        if not candidate:
            logger.warning(f"Candidate with id {candidate_id} not found")
            raise HTTPException(status_code=404, detail="Candidate not found")

        await session.delete(candidate)
        await session.commit()
        return {"success": f"Candidate with id {candidate.id} deleted."}


# Updated Resume CRUD methods --------------------------------
async def get_resume_by_id(resume_id: int, user_id: int) -> ResumeRead:
    """Get resume by resume_id with candidate info"""
    async with async_session_maker() as session:
        resume = await session.get(
            Resume, resume_id, options=[joinedload(Resume.candidate)]
        )

        if not resume:
            logger.warning(f"Resume with id {resume_id} not found")
            raise HTTPException(status_code=404, detail="Resume not found")
        vacancy = await session.get(Vacancy, resume.vacancy_id)
        if vacancy.user_id != user_id:
            logger.warning(f"Not enough permissions to read resume with id {resume_id} for user {user_id}")
            raise HTTPException(status_code=403, detail="Not enough permissions to read this resume")

        return resume


async def get_resumes_by_user_id(user_id: int) -> list[ResumeRead]:
    """Get resumes by user_id with candidate info"""
    async with async_session_maker() as session:
        query = (
            select(Resume)
            .join(Vacancy)
            .where(Vacancy.user_id == user_id)
            .options(joinedload(Resume.candidate))
        )
        result = await session.execute(query)
        resumes = result.unique().scalars().all()
        return resumes


async def get_vacancy_resumes_by_stage(vacancy_id: int, resume_stage: ResumeStage, user_id: int):
    """Get vacancy resumes by resume_stage with candidate info"""
    async with async_session_maker() as session:
        vacancy = await session.get(Vacancy, vacancy_id)
        if not vacancy or vacancy.user_id != user_id:
            logger.warning(f"Not enough permissions to access vacancy with id {vacancy_id} for user {user_id}")
            raise HTTPException(status_code=403, detail="Not enough permissions to access this vacancy")
        
        query = (
            select(Resume)
            .where(
                (Resume.vacancy_id == vacancy_id) & 
                (Resume.resume_stage == resume_stage)
            )
            .options(joinedload(Resume.candidate))
        )
        result = await session.execute(query)
        resumes = result.unique().scalars().all()
        return resumes


async def create_resume(new_resume: ResumeCreate, vacancy_id: int, user_id: int):
    """Create a new resume for current user with candidate info"""
    async with async_session_maker() as session:
        vacancy = await session.get(Vacancy, vacancy_id)
        if not vacancy or vacancy.user_id != user_id:
            logger.warning(f"Not enough permissions to create resume for vacancy with id {vacancy_id} for user {user_id}")
            raise HTTPException(status_code=403, detail="Not enough permissions to create resume for this vacancy")

        # Create or get candidate
        new_candidate_data = new_resume.candidate
        candidate = await create_candidate(new_candidate_data)
        
        new_resume_data = new_resume.model_dump(exclude={"candidate"})
        new_resume_data.update({"vacancy_id": vacancy_id, "candidate_id": candidate.id})
        resume = Resume(**new_resume_data)
        session.add(resume)
        await session.commit()
        await session.refresh(resume)
        return resume


async def delete_resume_by_id(resume_id: int, user_id: int):
    """Delete resume and potentially the candidate"""
    async with async_session_maker() as session:
        resume = await get_resume_by_id(resume_id, user_id)
        await session.delete(resume)
        await delete_candidate(resume.candidate_id)
        await session.commit()
        return {"success": f"Resume with id {resume.id} deleted."}


async def update_resume(updated_resume: ResumeUpdate, user_id: int) -> ResumeRead:
    """Update resume with updated_resume and user_id with candidate info"""
    async with async_session_maker() as session:
        resume = await get_resume_by_id(updated_resume.id, user_id)
        updated_data = updated_resume.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            if key == 'candidate' and isinstance(value, dict):
                if resume.candidate:
                    for candidate_key, candidate_value in value.items():
                        setattr(resume.candidate, candidate_key, candidate_value)
                else:
                    raise ValueError("Resume has no associated candidate to update.")
            else:
                setattr(resume, key, value)
        session.add(resume)
        await session.commit()
        await session.refresh(resume)
        return resume
