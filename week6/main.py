from fastapi import FastAPI, Request, Depends, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import mysql.connector, os
from dotenv import load_dotenv
from mysql.connector import Error
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware




app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="dfnfneiwcheoq")
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"))
app.mount("/frontend", StaticFiles(directory="frontend"))

# put the PW into .env then use dotenv to get imformation
load_dotenv()
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}


# Cehck DB connecting
def open_conn():
    return mysql.connector.connect(**DB_CONFIG)

# This is a decorator not a route, means when the server start running do this function once
@app.on_event("startup")
def test_db_connection():
    try:
        conn = open_conn()
        cur = conn.cursor()
        cur.execute("SELECT DATABASE(), NOW();")
        row = cur.fetchone()
        print("✅ DB 連線成功")
        print("目前使用的資料庫：", row[0])
        print("資料庫伺服器時間：", row[1])
    # Error is the error type provide by mysql
    except Error as e:
        print("❌ DB 連線失敗：", e)
    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()
        # if cur/conn have not been define as var will cause NameError, just pass it.
        except NameError:
            pass


#  Use Depends to connect and sending instruction to DB for API
def get_conn():
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

def get_cursor(conn = Depends(get_conn)):
    cur = conn.cursor(dictionary=True)
    try:
        yield cur
    finally:
        cur.close()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/member")
def member(
    request: Request,
    cur = Depends(get_cursor)
    ):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/ohoh?msg=請先登錄", status_code=303)
    
    find_user_sql = """
    SELECT name FROM member WHERE id = %s
    """
    cur.execute(find_user_sql, (user_id,))
    user = cur.fetchone()
    user_name = user["name"]

    find_msg_sql = """
    SELECT 
        member.name AS name, 
        member.id AS member_id,
        message.id AS message_id,
        message.content AS content
    FROM message JOIN member ON message.member_id = member.id
    ORDER BY message.created_at ASC
    """
    cur.execute(find_msg_sql)
    msg = cur.fetchall()

    return templates.TemplateResponse("member.html", {"request": request, "name": user_name, "user_id": user_id, "msg": msg})

@app.get("/logout")
def logout(
    request: Request
    ):
    request.session["user_id"] = None
    return RedirectResponse("/", status_code=303)
    


@app.get("/ohoh")
def ohoh(
    request: Request,
    msg: Annotated[str | None, Query()] = None
    ):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})

@app.post("/api/signup")
def signup(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    pw: Annotated[str, Form()],
    conn = Depends(get_conn)
    ):
    name = name.strip()
    email = email.strip()
    pw = pw.strip()
    if not name or not email or not pw:
        return RedirectResponse("/ohoh?msg=請輸入信箱或密碼", status_code=303)
    
    try:
        cur = conn.cursor(dictionary=True)
        find_sql = """
            SELECT email FROM member WHERE email = %s
        """
        
        insert_sql = """
            INSERT INTO member (name, email, password) VALUES (%s, %s, %s)
        """
        
        cur.execute(find_sql, (email,))
        result = cur.fetchone()
        if result is None:
            cur.execute(insert_sql, (name, email, pw))
            conn.commit()
            return RedirectResponse("/", status_code=303)
        else:
            return RedirectResponse("/ohoh?msg=重複的電子郵件", status_code=303)
    finally:
        cur.close()

@app.post("/api/login")
def login(
    request: Request,
    email: Annotated[str, Form()],
    pw: Annotated[str, Form()],
    cur = Depends(get_cursor)
    ):
    email = email.strip()
    pw = pw.strip()
    if not email or not pw:
        return RedirectResponse("/ohoh?msg=請輸入信箱或密碼", status_code=303)
    
    find_sql = """
    SELECT id, password FROM member WHERE email = %s
    """
    cur.execute(find_sql, (email,))
    db_data = cur.fetchone()
    if db_data is None:
        return RedirectResponse("/ohoh?msg=電子郵件或密碼錯誤", status_code=303)    
    else:
        if db_data["password"] == pw:
            request.session["user_id"] = db_data["id"]
            return RedirectResponse("/member", status_code=303)        
        else:
            return RedirectResponse("/ohoh?msg=電子郵件或密碼錯誤", status_code=303)

@app.post("/api/createMessage")
def create_message(
    request: Request,
    context: Annotated[str, Form()],
    conn = Depends(get_conn)
    ):
    context = context.strip()
    if not context:
        return RedirectResponse("/ohoh?msg=請輸入留言內容", status_code=303)

    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/ohoh?msg=請先登錄", status_code=303)
    
    cur = conn.cursor(dictionary=True)
    try:
        insert_msg_sql = """
            INSERT INTO message (member_id, content) VALUES (%s, %s)
        """
        cur.execute(insert_msg_sql,(user_id, context))
        conn.commit()
    finally:
        cur.close()
    return RedirectResponse("/member", status_code=303)
    
@app.post("/api/deleteMessage")
def delete_message(
    request: Request,
    message_id: Annotated[int, Form()],
    conn = Depends(get_conn)
    ):
    
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/ohoh?msg=請先登錄", status_code=303)
    
    cur = conn.cursor()
    try:
        delete_sql = """
        DELETE FROM message WHERE id = %s AND member_id = %s
        """
        cur.execute(delete_sql,(message_id, user_id))
        conn.commit()
    finally:
        cur.close()
    return RedirectResponse("/member", status_code=303)
