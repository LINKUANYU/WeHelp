from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates = Jinja2Templates(directory="demo")

app.mount("/demo", StaticFiles(directory="demo"))

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("demo.html", {"request": request})
    

@app.get("/api/data1")
def data1():
    return {"ok":True}

@app.get("/api/data2")
def data2(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    return {"ok":True}