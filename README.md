# AI Text Polish

一个基于智谱 AI API 的文本润色工具，将普通文本改写得更清晰、更专业、更通顺。

## 功能特性

- 使用智谱 GLM-4 模型进行文本润色
- FastAPI 后端 + 静态前端
- 支持跨域请求
- 自动错误处理

## 部署到 Vercel

### 前置条件
- 注册 Vercel 账户：https://vercel.com
- 安装 Vercel CLI：`npm install -g vercel`

### 部署步骤

1. **克隆项目到本地**
   ```bash
   git clone <your-repo-url>
   cd ai-text-polish
   ```

2. **安装 Python 依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **设置环境变量**
   - 在 Vercel 控制台中设置环境变量：
     - 进入项目设置 → Environment Variables
     - 添加新的环境变量：
       - Name: `ZHIPU_API_KEY`
       - Value: `your_actual_api_key_here`

4. **部署到 Vercel**
   ```bash
   vercel
   ```

   或者直接在 Vercel 控制台导入 Git 仓库。

### 环境变量配置

在 Vercel 部署时，必须设置以下环境变量：

| 变量名 | 描述 | 必需 |
|--------|------|------|
| `ZHIPU_API_KEY` | 智谱 AI API Key | 是 |

### 项目结构

```
ai-text-polish/
├── api/
│   └── polish.py      # FastAPI 后端代码
├── public/
│   └── index.html     # 前端页面
├── vercel.json        # Vercel 部署配置
├── requirements.txt   # Python 依赖
├── .env              # 环境变量模板
├── .vercelignore     # Vercel 忽略文件
└── README.md         # 项目说明
```

### 本地开发

```bash
# 启动 FastAPI 服务器
uvicorn api.polish:app --reload --host 0.0.0.0 --port 8000

# 访问 http://localhost:8000/docs 查看 API 文档
```

## 注意事项

1. **API Key 安全**：不要将 API Key 提交到版本控制系统
2. **CORS 配置**：生产环境建议限制访问域名
3. **错误处理**：生产环境不会返回详细的错误信息

## 许可证

MIT License