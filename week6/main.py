from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector, os
from dotenv import load_dotenv
from mysql.connector import Error




app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"))

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
# This is a decorator not a route, means when the server start running do this function once
@app.on_event("startup")
def test_db_connection():
    try:
        conn = get_conn()
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

#  Use Depends to connect and sending instruction to DB
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
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ohoh")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
