from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.resume.models import Resume, Sex
from src.resume.schemas import CreateResume

router = APIRouter()


# @router.get("/")
# async def get_all_resumes(session: AsyncSession = Depends(get_async_session)):
#     query = select(Resume)
#     result = await session.execute(query)
#     return {
#             "status": "success",
#             "data": result.scalars().all()
#     }


@router.get("/")
async def get_resume_by_sex(sex: Sex, session: AsyncSession = Depends(get_async_session)):
    query = select(Resume).where(Resume.sex == sex)
    result = await session.execute(query)
    return {
            "status": "ok",
            "data": result.scalars().all()
    }


@router.post("/")
async def add_resume(new_resume: CreateResume, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Resume).values(**new_resume.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
