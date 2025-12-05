from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Reflected_XSS 概念：正常的網站搜尋頁因設計漏洞，被攻擊者利用
@app.get("/search")
def search(q: str = ""):
    html = f"""
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/base.css">
            <title>Reflected XSS Demo</title>
        </head>
        <body>
            <header class="l-header flex">week8任務：Reflected XSS Demo</header>
            <div class="card">
                <h3 class="text-center">正常的網站搜尋頁(網站設計有漏洞)</h3>
                <form class="flex" action="/search">
                    <input name="q" autocomplete="off">
                    <button type="submit">搜尋</button>
                </form>
                <div class="text-center">你搜尋了：{q}</div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(html)

# 最後將有問題的網址散播在任何地方給受害者點
# http://127.0.0.1:8000/search?q=%3Cscript%3Ealert(%27XSS%20ATTACK%27)%3C/script%3E



# # 防禦概念：不要自己用字串拼 HTML，改用模板引擎有預設 HTML escape 功能
# # jinja engine

# templates = Jinja2Templates(directory=".")

# @app.get("/search")
# def search(request: Request, q: str = ""):
#     return templates.TemplateResponse("reflected_xss.html", {"request": request, "q": q})

app.mount("/", StaticFiles(directory="."))

# HTML escape：在 HTML 裡，把這些符號有「語法上的意義」變成「安全的文字」來顯示
# 把 < 變成 &lt;          <：開始一個標籤
# 把 > 變成 &gt;          >：結束一個標籤
# 把 & 變成 &amp;         &：開始一個實體（例如 &nbsp;）
# 把 " 變成 &quot;        " / '：用在屬性的引號裡
# 把 ' 變成 &#x27;（或 &#39;）