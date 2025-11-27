from fastapi import APIRouter, Depends, HTTPException, Request
from mysql.connector import Error, IntegrityError, errorcode
from ..schemas import signUpIn, loginIn, renameIn
from ..deps import get_conn, get_cur, get_current_user

# HTTPException
# 用途：當發生業務錯誤或權限不足等情況，需要回 400/401/403/404/409/... 這類錯誤碼時使用。
# 會發生什麼：丟出後，FastAPI 不再執行後續程式碼或路由處理器，直接組出錯誤 JSON。
# 回傳格式（預設）：{"detail": <你給的 detail>}

router = APIRouter(prefix="/api")

# signup
@router.post("/signup")
def signup(payload: signUpIn, conn = Depends(get_conn)):
    # check input data
    email = payload.email.strip().lower()
    name = payload.name.strip()
    pw = payload.pw
    if not email or not name or not pw:
        raise HTTPException(status_code=400, detail="請輸入完整資訊")
    # sql 
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO member(email, name, password) VALUES (%s, %s, %s)",(email, name, pw))
        conn.commit()
        return {"msg": "註冊成功，請重新登入"}
    
    except IntegrityError as e:                       # 只攔「資料完整性」錯誤（例如 UNIQUE/FK）
        conn.rollback()                               # 這次交易全部撤回，避免半套資料/鎖卡住
        if e.errno == errorcode.ER_DUP_ENTRY:         # 判斷是否為「重複鍵」(MySQL 1062)
            raise HTTPException(status_code=409, detail="已存在email")  # 回給前端 400＋友善訊息

    except Error:
        conn.rollback()
        raise HTTPException(status_code=500, detail="資料庫錯誤，稍後再試")
    
    finally:
        cur.close()

# login
@router.post("/login")
def login(request: Request, payload: loginIn, cur = Depends(get_cur)):
    email = payload.email.strip()
    pw = payload.pw
    if not email or not pw:
        raise HTTPException(status_code=400, detail="請輸入完整資訊")
    
    cur.execute("SELECT id, name, email, password FROM member WHERE email = %s", (email,))
    data = cur.fetchone()
    if not data:
        raise HTTPException(status_code=401, detail="帳號或密碼輸入錯誤")
    if data["password"] != pw:
        raise HTTPException(status_code=401, detail="帳號或密碼輸入錯誤")

    request.session["user_id"] = data["id"]
    return {"id": data["id"], "name": data["name"], "id": data["email"]}

# get member inform
@router.get("/member")
def member(current_user = Depends(get_current_user)):
    return {"id": current_user["id"], "name": current_user["name"], "id": current_user["email"]}

# search member id API
@router.get("/member/{search_id}")
def member_search_id(
    search_id: int,
    conn = Depends(get_conn), 
    current_user = Depends(get_current_user)
    ):    
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, email FROM member WHERE id = %s", (search_id,))
    data = cur.fetchone()
    if not data:
        cur.close()
        return {"data": "null"}
    
    searcher_id = current_user["id"]
    target_id = search_id
    cur.execute("INSERT INTO member_search_log(searcher_id, target_id)" \
    "VALUES(%s, %s)", (searcher_id, target_id))
    conn.commit()
    cur.close()
    return {"data":{"id": data["id"], "name": data["name"], "email": data["email"]}}

# rename API
@router.patch("/member")
def rename(
    payload: renameIn,
    conn = Depends(get_conn),
    current_user = Depends(get_current_user)
    ):
    user_id = current_user["id"]
    new_name = payload.new_name.strip()
    if not new_name:
        return {"error": True}
    cur = conn.cursor(dictionary=True)
    cur.execute("UPDATE member SET name = %s WHERE id = %s", (new_name, user_id))
    conn.commit()
    cur.close()
    return {"ok": True}

# who search me API
@router.get("/member/extra/who_search")
def who_search(cur = Depends(get_cur), current_user = Depends(get_current_user)):
    user_id = current_user["id"]
    print(user_id)
    cur.execute("""
        SELECT s.searcher_id, s.created_at, m.name
        FROM member_search_log s JOIN member m ON s.searcher_id = m.id
        WHERE s.target_id = %s 
        AND s.searcher_id <> %s
        ORDER BY s.created_at DESC
        LIMIT 10
        """, (user_id, user_id))
    result = cur.fetchall()
    return {"data": result}

    
        
        


