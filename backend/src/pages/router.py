from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="frontend/src/templates")


@router.get("/crm")
def get_base_template(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
