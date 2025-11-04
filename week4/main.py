from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import urllib.request as req
import json


app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="kfnejnfwndnskdlakmd")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@app.post("/login")
def login(
    request: Request,
    # email would be sent in thur html form(default None), type could be str or None
    email: Annotated[str | None, Form()] = None, 
    password: Annotated[str| None, Form()] = None
    ):
    # (A or B) means if A != (None, empty string, 0) return A, else return B
    # if email == (None, empty string, 0) then can't use .strip(), So turn email into "" (empty str)
    email = (email or "").strip()
    password = (password or "").strip()
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
    request.session["user_id"] = email
    return RedirectResponse(url="/member", status_code=303)
@app.get("/member")
def member(request: Request):
    # cuz session is dict form, in {} if key is not exsist use .get() will return None instead of Keyerror
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/logout")
def logout(request: Request):
    request.session["user_id"] = None
    return RedirectResponse(url="/", status_code=303)

@app.get("/ohoh")
def ohoh(
     request: Request,
     msg: str = None
     ):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg":msg})

@app.get("/hotel/{id}")
def hotel(
    request:Request,
    id: int
    ):
    ch_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
    en_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
    with req.urlopen(ch_url) as response_ch:
        ch_rowdata = json.load(response_ch)
    with req.urlopen(en_url) as response_en:
        en_rowdata = json.load(response_en)
    ch_datas = ch_rowdata["list"]
    en_datas = en_rowdata["list"]
    result1 = None
    for ch_data in ch_datas:
        if id == int(ch_data["_id"]):
            result1 = ch_data["旅宿名稱"]
            break
    if result1 == None:
        return templates.TemplateResponse("hotel.html", {"request": request, "msg": "查詢不到相關資料"})
    result2 = result3 = None
    for en_data in en_datas:
        if id == int(en_data["_id"]):
            result2 = en_data["hotel name"]
            result3 = en_data["tel"]
            break
    if result2 == None or result3 == None:
        return templates.TemplateResponse("hotel.html", {"request": request, "msg": "查詢不到相關資料"})
    msg = f"{result1}、{result2}、{result3}"
    return templates.TemplateResponse("hotel.html", {"request": request, "msg":msg})