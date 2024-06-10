from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from backend.src.auth.manager import get_user_manager
from backend.src.auth.models import User
from backend.src.config import SECRET_JWT

cookie_transport = CookieTransport(
    cookie_name="bonds",
    cookie_max_age=3600
)

SECRET = SECRET_JWT


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
