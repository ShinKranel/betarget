import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.router import router as user_router
from src.auth.schemas import UserRead, UserCreate
from src.resume.router import router as resume_router
from src.vacancy.router import router as vacancy_router


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(user_router, tags=["auth"])
app.include_router(resume_router, prefix="/resume", tags=["auth"])
app.include_router(vacancy_router, prefix="/vacancy", tags=["auth"])

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )



