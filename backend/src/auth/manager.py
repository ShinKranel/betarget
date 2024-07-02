from typing import Optional

from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, IntegerIDMixin

from backend.src.config import settings
from backend.src.db import get_user_db
from backend.src.auth.models import User
from backend.src.mail.utils import (
    send_sucessful_login_msg,
    send_sucessful_register_msg,
    send_sucessful_reset_password_msg,
    send_sucessful_forgot_password_msg,
    send_email_verification_msg,
)

auth_settings = settings.auth
SECRET = auth_settings.SECRET_MANAGER


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        await send_sucessful_register_msg(user=user)

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ):
        print(f"User {user.id} logged in.")
        await send_sucessful_login_msg(user=user)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")
        await send_sucessful_forgot_password_msg(user=user, reset_token=token)

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        await send_sucessful_reset_password_msg(user=user)

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        await send_email_verification_msg(user=user, verification_token=token)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
