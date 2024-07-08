from fastapi import HTTPException
from sqlalchemy import select
from typing import Optional

from auth.models import User
from logger import logger
from db import async_session_maker


async def get_user_by_username(username: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(username == User.username)
        user = (await session.execute(query)).scalar_one_or_none()
        return user 
    

async def update_user_verification_token(user_id: int, token: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(user_id == User.id)
        user = (await session.execute(query)).scalar_one_or_none()
        user.verification_token = token
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def verify_verification_token(token: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(token == User.verification_token)
        user = (await session.execute(query)).scalar_one_or_none()
        if not user:
            logger.warning(f"User with verification token {token} not found")
            raise HTTPException(status_code=404, detail=f"User with this verification token {token} not found")

        logger.debug(f"User with verification token {token} verified")
        user.is_verified = True
        user.verification_token = None
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user
