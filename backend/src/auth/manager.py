from typing import Optional
from uuid import UUID
import secrets
from uuid import uuid4

from fastapi import Depends, Request, Response
from fastapi_users import exceptions, models
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.password import PasswordHelper
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from config import settings
from db import get_user_db, async_session_maker
from logger import logger
from user.models import User
from auth.tasks import delete_user_reset_password_token_task, delete_user_verification_token_task
from auth.service import update_user_verification_token, update_user_reset_password_token
from mail.utils import (
    send_sucessful_login_msg,
    send_sucessful_register_msg,
    send_sucessful_reset_password_msg,
    send_sucessful_forgot_password_msg,
    send_email_verification_msg,
)

auth_settings = settings.auth
SECRET = auth_settings.SECRET_MANAGER

password_hash = PasswordHash((Argon2Hasher(),))
password_helper = PasswordHelper(password_hash)


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def oauth_callback(
        self: "BaseUserManager[models.UOAP, models.ID]",
        oauth_name: str,
        access_token: str,
        account_id: str,
        account_email: str,
        expires_at: Optional[int] = None,
        refresh_token: Optional[str] = None,
        request: Optional[Request] = None,
        *,
        associate_by_email: bool = False,
        is_verified_by_default: bool = False,
    ) -> models.UOAP:
        oauth_account_dict = {
            "oauth_name": oauth_name,
            "access_token": access_token,
            "account_id": account_id,
            "account_email": account_email,
            "expires_at": expires_at,
            "refresh_token": refresh_token,
        }
        try:
            user = await self.get_by_oauth_account(oauth_name, account_id)
        except exceptions.UserNotExists:
            try:
                # Associate account
                user = await self.get_by_email(account_email)
                if not associate_by_email:
                    raise exceptions.UserAlreadyExists()
                user = await self.user_db.add_oauth_account(user, oauth_account_dict)
            except exceptions.UserNotExists:
                # Create account
                username_postfix = str(uuid4()).replace("-", "")[:7]
                username = account_email.split("@")[0] + "_" + username_postfix
                password = self.password_helper.generate()
                user_dict = {
                    "email": account_email,
                    "username": username,
                    "hashed_password": self.password_helper.hash(password),
                    "is_verified": is_verified_by_default,
                }
                user = await self.user_db.create(user_dict)
                user = await self.user_db.add_oauth_account(user, oauth_account_dict)
                await self.on_after_register(user, request)
        else:
            # Update oauth
            for existing_oauth_account in user.oauth_accounts:
                if (
                    existing_oauth_account.account_id == account_id
                    and existing_oauth_account.oauth_name == oauth_name
                ):
                    user = await self.user_db.update_oauth_account(
                        user, existing_oauth_account, oauth_account_dict
                    )
        
        return user
    
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        logger.debug(f"User {user.id} has registered.")
        await self.on_after_request_verify(user=user, token='', request=request)
        await send_sucessful_register_msg(user=user)

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ): 
        logger.debug(f"User {user.id} logged in.")
        logger.debug(f"Request: {str(request.json)}")
        logger.debug(f"Response: {response.body}")
        await send_sucessful_login_msg(user=user)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        logger.debug(f"User {user.id} has forgot their password. Reset token: {token}")
        await update_user_reset_password_token(user_id=user.id, token=token)
        await send_sucessful_forgot_password_msg(user=user, reset_token=token)
        delete_user_reset_password_token_task.apply_async(
            (user.id,), countdown=auth_settings.RESET_PASSWORD__TOKEN_EXPIRATION
        )

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        await send_sucessful_reset_password_msg(user=user)

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        token = await send_verification(user=user)
        logger.debug(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


async def verify_password(stored_hashed_password: str, given_password: str) -> bool:
    is_verified, updated_hash = password_helper.verify_and_update(given_password, stored_hashed_password)
    if is_verified and updated_hash:
        async with async_session_maker() as session:
            await session.execute(
                f"UPDATE {User.__tablename__} SET hashed_password = :new_hash WHERE hashed_password = :old_hash",
                {"new_hash": updated_hash, "old_hash": stored_hashed_password}
            )
            await session.commit()
    return is_verified


async def send_verification(user: User) -> str:
    token = secrets.token_hex(16)
    await update_user_verification_token(user_id=user.id, token=token)
    await send_email_verification_msg(user=user, verification_token=token)
    delete_user_verification_token_task.apply_async(
        (user.id,), countdown=auth_settings.VERIFY_TOKEN_EXPIRATION
    )
    return token