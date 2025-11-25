import os
from dotenv import load_dotenv
import mysql.connector
from fastapi import Depends
from typing import Generator

# 讀環境變數
load_dotenv()
# DB環境變數
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "website")
}

# 連線到資料庫用Depends來管理，連線結束後自動關閉，-> 代表方程式回傳的物件類型是Generator
def get_conn() -> Generator:
    conn = mysql.connector.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

def get_cur(conn = Depends(get_conn)) -> Generator:
    cur = conn.cursor(dictionary=True)
    try:
        yield cur
    finally:
        cur.close()