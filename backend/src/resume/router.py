from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.resume.models import Resume
from backend.src.resume.schemas import ResumeCreate, ResumeRead

router = APIRouter()


@router.get("/")
async def get_resumes(session: AsyncSession = Depends(get_async_session)):
    query = select(Resume)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{resume_id}")
async def get_resume_by_id(resume_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Resume).where(Resume.id == resume_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def add_resume(new_resume: ResumeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Resume).values(**new_resume.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/")
async def delete_resume(resume_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Resume).where(Resume.id == resume_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": f"resume with id {resume_id} was deleted"}
