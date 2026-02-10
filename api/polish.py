import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# 创建 FastAPI 应用
app = FastAPI()

# 允许跨域（方便前端调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 从环境变量中读取智谱 API Key
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "22896446ae2042368f83e093ea197965.VJcQGRGpMwvrAdpV")

# 初始化客户端，指向智谱的 API 地址
client = OpenAI(
    api_key=ZHIPU_API_KEY,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

# 请求体结构
class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "AI Text Polish Backend is running"}

@app.post("/api/polish")
def polish_text(request: TextRequest):
    user_text = request.text

    # 1. 验证文本输入
    if not user_text or not user_text.strip():
        raise HTTPException(status_code=400, detail="文本不能为空")

    try:
        print(f"正在处理文本: {user_text[:30]}...") 
        
        # 2. 调用智谱 GLM-4 模型
        response = client.chat.completions.create(
            model="glm-4", 
            messages=[
                {
                    "role": "system", 
                    "content": "你是一名专业的文字编辑，请将用户提供的文本改写得更清晰、更专业、更通顺。"
                },
                {
                    "role": "user", 
                    "content": user_text
                }
            ],
            temperature=0.7
        )
        
        # 3. 提取结果
        if not response.choices:
            raise HTTPException(status_code=500, detail="AI 服务返回了空响应")
        
        polished_text = response.choices[0].message.content

        return {
            "original": user_text,
            "polished": polished_text
        }

    except Exception as e:
        print(f"发生错误: {str(e)}")
        # 抛出详细错误供前端调试
        raise HTTPException(status_code=500, detail=str(e))