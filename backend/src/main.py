import sys
sys.path.append('g:\\OSPanel\\domains\\betarget\\betarget')

from backend.src.config import BACKEND_CORS_ORIGINS
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from starlette.staticfiles import StaticFiles

from auth.base_config import auth_backend
from auth.manager import get_user_manager
from backend.src.auth.models import User
from auth.schemas import UserRead, UserCreate

from auth.router import router as router_user
from resume.router import router as router_resume
from vacancy.router import router as router_vacancy
from pages.router import router as router_pages

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.mount(
    "/static",
    StaticFiles(directory='frontend/src/static'),
    name="static",
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(router_user, prefix="/auth", tags=["auth"])
app.include_router(router_vacancy, prefix="/vacancy", tags=["vacancy"])
app.include_router(router_resume, prefix="/resume", tags=["resume"])
app.include_router(router_pages, prefix="/pages", tags=["pages"])
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


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
