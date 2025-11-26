from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from ..path import TEMPLATES_DIR

router = APIRouter()

templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})


@router.get("/member")
def member(request: Request):
    if not request.session.get("user_id"):
        return RedirectResponse("/?msg=請先登入", status_code=303)
    return templates.TemplateResponse("member.html",{"request": request})

@router.get("/logout")
def logout(request: Request):
    request.session["user_id"] = None
    return RedirectResponse("/", status_code=303)
    