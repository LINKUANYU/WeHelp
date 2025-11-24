from fastapi import APIRouter, Request
from ..schemas import signUp


router = APIRouter(prefix="/api")

# signup
@router.post("/signup")
def signup(payload: signUp):
    email = payload.email.strip()
    name = payload.name.strip()
    pw = payload.pw.strip()
    if not email or not name or not pw:
        return {"msg": "請輸入完整資訊"}
    # sql 


    print(email)
    return {"ok": "註冊成功"}

# login

