from fastapi import FastAPI
from .routers import page, router
from fastapi.staticfiles import StaticFiles
from .path import FRONT_DIR
import mysql.connector
from mysql.connector import Error
from .deps import DB_CONFIG
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(page.router)
app.include_router(router.router)

app.mount("/frontend", StaticFiles(directory=FRONT_DIR))




@app.on_event("startup")
def db_connect_test():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT DATABASE() AS DB")
        row = cur.fetchone()
        print("ok, 已連線到資料庫：", row["DB"])
    except Error as e:
        print("連線失敗：", e)
    finally:
        try:
            if cur:
                cur.close()
            if conn:
                conn.close()
        except NameError:
            pass


