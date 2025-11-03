from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name = "static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@app.get("/member")
def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/ohoh")
def member(request: Request):
    return templates.TemplateResponse("ohoh.html", {"request": request})