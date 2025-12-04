import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv
import time
# 從.env讀取環境變數
load_dotenv()
# DB連線參數設定
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE")
}
# 建立連線池
cnxpool = pooling.MySQLConnectionPool(
    pool_name = "mypool",
    pool_size = 5,
    **DB_CONFIG
)
# Demo1：使用連線池操作DB
def demo1():
    # 從連線池拿連線來使用
    cnx1 = cnxpool.get_connection()
    cnx2 = cnxpool.get_connection()
    cnx3 = cnxpool.get_connection()
    # 建立cursor
    cur1 = cnx1.cursor()
    cur2 = cnx2.cursor()
    cur3 = cnx3.cursor()
    # 嘗試插入資料
    try:
        cur1.execute("INSERT INTO member(name, email, password) VALUES(%s, %s, %s)", ("Alice", "Alice@mail", "123"))
        cur2.execute("INSERT INTO member(name, email, password) VALUES(%s, %s, %s)", ("Bob", "Bob@mail", "456"))
        cnx1.commit()
        cnx2.commit()
        print("會員資料插入成功")
    # 印出錯誤訊息
    except mysql.connector.Error as e:
        print("插入失敗", e)
    # 搜尋
    cur3.execute("SELECT * FROM member")
    data = cur3.fetchall()
    print("查詢所有會員資料：", data)
    # 關閉cur然後歸還連線池的連線
    cur1.close()
    cur2.close()
    cur3.close()
    cnx1.close()
    cnx2.close()
    cnx3.close()
    return 

# Demo2：比較有無使用連線池的時間差別
def demo2():
    # 未使用連線池，每次都與DB重新建立連線和關閉連線
    start1 = time.perf_counter()
    for _ in range(300):
        cnx = mysql.connector.connect(**DB_CONFIG)
        cur = cnx.cursor()
        cur.execute("SELECT password FROM member WHERE name = %s", ("Alice",))
        cur.fetchone()
        cur.close()
        cnx.close()
    end1 = time.perf_counter()
    print("「未」使用連線池的狀況下時間花費", end1 - start1, "秒")

    # 使用連線池，每次都跟連線池借用連線
    start2 = time.perf_counter()
    for _ in range(300):
        cnx = cnxpool.get_connection()
        cur = cnx.cursor()
        cur.execute("SELECT password FROM member WHERE name = %s", ("Alice",))
        cur.fetchone()
        cur.close()
        cnx.close()
    end2 = time.perf_counter()
    print("「有」使用連線池的狀況下時間花費", end2 - start2, "秒")
    return

demo1()
demo2()
