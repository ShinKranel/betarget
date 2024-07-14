from fastapi import HTTPException, UploadFile
from sqlalchemy import select
from typing import Optional

from user.models import User
from user.schemas import UserRead, UserUpdate
from s3_storage import s3_client, s3_settings
from logger import db_query_logger as logger
from db import async_session_maker


async def get_user_by_username(username: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(username == User.username)
        user = (await session.execute(query)).scalar_one_or_none()
        return user
    

async def get_user_by_email(email: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(email == User.email)
        user = (await session.execute(query)).scalar_one_or_none()
        return user
    

async def delete_user(user: User):
    async with async_session_maker() as session:
        stmt = select(User).where(User.id == user.id)
        result = await session.execute(stmt)
        db_user = result.scalar_one_or_none()
        await session.refresh(db_user)
        await session.delete(db_user)
        await session.commit()
        logger.info(f"User {db_user} deleted")
    

async def update_user(user: User, updated_user: UserUpdate) -> UserRead:
    async with async_session_maker() as session:
        query = select(User).where(User.id == user.id)
        db_user = (await session.execute(query)).scalar_one_or_none()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in updated_user.model_dump().items():
            setattr(db_user, key, value)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user


async def update_user_profile_picture(user: User, profile_picture: UploadFile | None) -> str | None:
    async with async_session_maker() as session:
        stmt = select(User).where(User.id == user.id)
        result = await session.execute(stmt)
        db_user = result.scalar_one_or_none()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        if profile_picture:
            if db_user.profile_picture and s3_settings.S3_PUBLIC_DOMAIN in db_user.profile_picture:
                delete_path = '/'.join(db_user.profile_picture.split('/')[3:])
                await s3_client.delete_file(delete_path)
            s3_key = f"profile-pictures/{user.username}/{profile_picture.filename}"
            profile_url = await s3_client.upload_file(
                object_name=s3_key,
                file_data=profile_picture.file,
            )
            db_user.profile_picture = profile_url
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user.profile_picture