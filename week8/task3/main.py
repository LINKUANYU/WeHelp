from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# FastAPI 會自動在所有回應加上對應的 CORS header
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],         # 允許哪些 origin
#     allow_credentials=False,         # 要不要允許 cookie / 認證資訊
#     allow_methods=["*"],            # 允許哪些 HTTP 方法（GET, POST...）
#     allow_headers=["*"],            # 允許哪些自訂 header
# )
    

@app.get("/api/demo1")
def demo1():
    return {"msg": "成功獲取資料！！！"}

@app.get("/api/demo2")
def demo2(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    return {"msg": "成功獲取資料！！！"}