from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许所有跨域请求，方便前端开发
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 示例接口，返回模拟数据
@app.get("/api/data")
def get_data():
    return {
        "x": ["一月", "二月", "三月", "四月"],
        "y": [120, 200, 150, 80]
    } 