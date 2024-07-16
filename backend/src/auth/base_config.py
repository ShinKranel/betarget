from typing import Optional, Type, TypeVar, Generic

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi import APIRouter
from fastapi_users import models

from auth.manager import get_user_manager
from user.models import User
from config import settings

try:
    from httpx_oauth.oauth2 import BaseOAuth2
    from src.auth.socials.router import get_oauth_router
except ModuleNotFoundError:
    BaseOAuth2 = Type


auth_settings = settings.auth
SECRET = auth_settings.SECRET_JWT


cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=604800)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

UP = TypeVar("UP", bound=User)
ID = TypeVar("ID")

class CustomFastapiUsers(FastAPIUsers[models.UP, models.ID], Generic[models.UP, models.ID]):
    def get_oauth_router(
        self,
        oauth_client: BaseOAuth2,
        backend: AuthenticationBackend,
        state_secret: str,
        redirect_url: Optional[str] = None,
        associate_by_email: bool = False,
        is_verified_by_default: bool = False,
    ) -> APIRouter:
        return get_oauth_router(
            oauth_client,
            backend,
            self.get_user_manager,
            state_secret,
            redirect_url,
            associate_by_email,
            is_verified_by_default,
        )

fastapi_users = CustomFastapiUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()