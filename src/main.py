import uvicorn
from fastapi import FastAPI

from src.auth.router import router as user_router
from src.resume.router import router as resume_router
from src.vacancy.router import router as vacancy_router


app = FastAPI()

app.include_router(user_router, tags=["auth"])
app.include_router(resume_router, prefix="/resume", tags=["auth"])
app.include_router(vacancy_router, prefix="/vacancy", tags=["auth"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )



