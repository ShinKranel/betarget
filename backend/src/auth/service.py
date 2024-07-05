from sqlalchemy import select
from typing import Optional

from auth.models import User
from db import async_session_maker


async def get_user_by_username(username: str) -> Optional[User]:
    async with async_session_maker() as session:
        query = select(User).where(username == User.username)
        user = (await session.execute(query)).scalar_one_or_none()
        return user 