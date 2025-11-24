from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..path import TEMPLATES_DIR

router = APIRouter()

templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})


@router.get("/member")
def member(request: Request):
    return templates.TemplateResponse("member.html",{"request": request})


    