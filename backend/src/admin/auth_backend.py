import secrets

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from auth.manager import verify_password
from auth.service import get_user_by_username
from logger import logger
from config import settings


admin_settings = settings.admin


class AdminAuth(AuthenticationBackend):
    async def __login(self, request: Request, username: str, log_msg: str | None = None) -> bool:
        session_token = secrets.token_hex(16)
        request.session.update({
                "admin_session_token": session_token,
                "admin_username": username
            })
        logger.info(log_msg)
        return True
    
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if username == admin_settings.ADMIN_USERNAME and password == admin_settings.ADMIN_PASSWORD:
            return await self.__login(request, username, "Base Admin logged in admin panel")

        user = await get_user_by_username(username)

        if user and await verify_password(user.hashed_password, password) and user.is_superuser:
            return await self.__login(request, username, f"Admin {user} logged in admin panel")

        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        logger.warning("Logged out admin panel")
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("admin_session_token")
        username = request.session.get("admin_username")

        if not token or not username:
            return False

        if username == admin_settings.ADMIN_USERNAME:
            return True

        user = await get_user_by_username(username)

        if not user or not user.is_superuser:
            return False

        return True
