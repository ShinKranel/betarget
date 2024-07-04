import secrets

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from backend.src.auth.manager import verify_password
from backend.src.auth.service import get_user_by_username
from backend.src.logger import logger


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        user = await get_user_by_username(username)

        if user and await verify_password(user.hashed_password, password) \
            and user.is_superuser and user.is_verified and user.is_active:
            session_token = secrets.token_hex(16)
            request.session.update({
                "admin_session_token": session_token,
                "admin_username": username
            })
            logger.info(f"User {user} logged in admin panel")
            return True

        logger.warning(f"User {user} failed to login in admin panel")
        return False

    async def logout(self, request: Request) -> bool:
        logger.warning(f"User {request.user} logged out admin panel")
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("admin_session_token")
        username = request.session.get("admin_username")

        if not token or not username:
            return False

        user = await get_user_by_username(username)

        if not user or not user.is_superuser:
            return False

        return True
