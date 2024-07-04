from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import mimetypes

from backend.src.logger import logger

mimetypes.init()

router = APIRouter()

templates = Jinja2Templates(directory="frontend/src/templates")


@router.get("/crm", response_class=HTMLResponse)  # todo: make route protected
def get_base_template(request: Request):
    logger.info("Get CRM template")
    mimetypes.add_type('application/javascript', '.js')
    mimetypes.add_type('text/css', '.css')
    context = {
        "request": request
    }
    return templates.TemplateResponse("index.html", context)
