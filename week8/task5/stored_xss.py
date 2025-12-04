from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory=".")
# 把留言暫時存進記憶體，server關掉後消失
comment = []

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("stored_xss.html", {"request": request, "comment": comment})

@app.post("/comment")
def search(content: str = Form(...)):
    comment.append(content)
    return RedirectResponse("/", status_code=303)

app.mount("/", StaticFiles(directory="."))
