import os
import json
from openai import OpenAI

# 从环境变量中读取智谱 API Key
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

# 如果没有设置 API Key，给出警告
if not ZHIPU_API_KEY:
    print("⚠️  警告：未设置 ZHIPU_API_KEY 环境变量")

# 初始化客户端，指向智谱的 API 地址
client = OpenAI(
    api_key=ZHIPU_API_KEY,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

def handler(event, context):
    """
    Netlify Function handler
    """
    try:
        # 处理 OPTIONS 请求（预检请求）
        if event.get('httpMethod') == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
                },
                'body': ''
            }

        # 解析请求
        body = json.loads(event.get('body', '{}'))
        user_text = body.get('text', '')

        # 验证文本输入
        if not user_text or not user_text.strip():
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
                },
                'body': json.dumps({'detail': '文本不能为空'})
            }

        # 调用智谱 GLM-4 模型
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

        # 提取结果
        if not response.choices:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
                },
                'body': json.dumps({'detail': 'AI 服务返回了空响应'})
            }

        polished_text = response.choices[0].message.content

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            },
            'body': json.dumps({
                'original': user_text,
                'polished': polished_text
            })
        }

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
            },
            'body': json.dumps({'detail': '服务内部错误，请稍后重试'})
        }