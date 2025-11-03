from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@app.post("/login")
def login(
    request: Request,
    email: Annotated[str, Form()],
    password: Annotated[str, Form()]
    ):
    if not email or not password:
        return RedirectResponse(
            url="/ohoh?msg=請輸入信箱和密碼",
            status_code=303
        )
        
    elif email != "abc@abc.com" or password != "abc":
        return RedirectResponse(
            url="/ohoh?msg=信箱或密碼輸入錯誤",
            status_code=303
        )
    
    return RedirectResponse(url="/member", status_code=303)
@app.get("/member")
def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/ohoh")
def ohoh(
     request: Request,
     msg: str = None
     ):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg":msg})