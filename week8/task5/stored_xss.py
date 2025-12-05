from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse

# 把留言暫時存進記憶體，server關掉後消失
comment = []

app = FastAPI()

# # Stored_XSS 概念：資料庫設計漏洞，攻擊者存入惡意腳本
# @app.get("/")
# def home():
#     comment_html = comment_html = "<br>".join(comment) or "目前沒有留言"

#     html = f"""
#     <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <link rel="stylesheet" href="/base.css">
#             <title>Storted XSS Demo</title>
#         </head>
#         <body>
#             <header class="l-header flex">week8任務：Stored XSS Demo</header>
#             <!-- Demo -->
#             <div class="card">
#                 <p class="text-center">留言板(設計有漏洞)</p>
#                 <form class="flex" action="/comment" method="post">
#                     <input name="content" autocomplete="off">
#                     <button type="submit">留言</button>
#                 </form>
#                 <div class="text-center">留言列表：</div>
#                 <div class="flex">
#                     {comment_html}
#                 </div>
#             </div>
#         </body>
#     </html>
#     """
#     return HTMLResponse(html)
# # 攻擊者直接輸入惡意程式存進資料庫，每當有人查看資料就會跑出來
# # <script>alert("XSS ATTACK")</script> 

# 防禦概念：

# 資料庫裡的東西一律當「不可信」 就算是很久以前存的、自己系統產生的，也可能被利用。
# 輸出到 HTML 時，一樣要用模板引擎 + auto escape。
# jinja engine
templates = Jinja2Templates(directory=".")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("stored_xss.html", {"request": request, "comment": comment})

# add comment
@app.post("/comment")
def add_comment(content: str = Form(...)):
    comment.append(content)
    return RedirectResponse("/", status_code=303)

app.mount("/", StaticFiles(directory="."))
