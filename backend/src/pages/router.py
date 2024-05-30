from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from backend.src.resume.router import get_resume_by_sex

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@router.get("/crm")
def get_base_template(request: Request):
    return templates.TemplateResponse("crm.html", {"request": request})


@router.get("/base")
def get_base_template(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search/{sex}")
def get_base_template(request: Request, resume=Depends(get_resume_by_sex)):
    return templates.TemplateResponse("search.html", {"request": request, "resume": resume["data"]})
