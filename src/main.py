import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.router import router as router_user
from src.resume.router import router as router_resume
from src.vacancy.router import router as router_vacancy


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(router_user, tags=["auth"])
app.include_router(router_resume, prefix="/resume", tags=["resume"])
app.include_router(router_vacancy, prefix="/vacancy", tags=["vacancy"])

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


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym!"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )



