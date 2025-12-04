from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory=".")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("reflected_xss.html", {"request": request})

@app.get("/search")
def search(request: Request, q: str = ""):
    return templates.TemplateResponse("reflected_xss.html", {"request": request, "q": q})

app.mount("/", StaticFiles(directory="."))
