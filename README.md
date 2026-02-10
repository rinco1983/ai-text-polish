# AI Text Polish

一个基于智谱 AI API 的文本润色工具，将普通文本改写得更清晰、更专业、更通顺。

## 功能特性

- 使用智谱 GLM-4 模型进行文本润色
- FastAPI 后端 + 静态前端
- 支持跨域请求
- 自动错误处理

## 部署方式

### 方式一：部署到 Netlify（推荐）

#### 前置条件
- 注册 Netlify 账户：https://www.netlify.com
- 安装 Netlify CLI：`npm install -g netlify-cli`

#### 快速开始

1. **使用 Netlify CLI 部署**
   ```bash
   npm install -g netlify-cli
   netlify login
   netlify init
   netlify deploy --prod
   ```

2. **设置环境变量**
   - 在 Netlify 控制台的 "Site settings" → "Environment variables" 中
   - 添加环境变量：`ZHIPU_API_KEY` = 你的真实 API Key

3. **重新部署**
   - 设置环境变量后，在 Netlify 控制台手动触发部署

#### 详细部署指南

详细的 Netlify 部署指南请查看 [NETLIFY_DEPLOY.md](NETLIFY_DEPLOY.md)

---

### 方式二：部署到 Vercel

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
│   └── polish.py           # FastAPI 后端代码
├── netlify/
│   └── functions/
│       └── polish.py       # Netlify Functions 代码
├── public/
│   └── index.html          # 前端页面（儿童风格）
├── netlify.toml            # Netlify 配置
├── vercel.json             # Vercel 配置
├── requirements.txt        # Python 依赖
├── NETLIFY_DEPLOY.md       # Netlify 部署指南
├── .env                    # 环境变量模板
├── .vercelignore           # Vercel 忽略文件
└── README.md               # 项目说明
```

### 本地开发

#### 使用 FastAPI 服务器（推荐）
```bash
# 安装依赖
pip install -r requirements.txt

# 启动 FastAPI 服务器
uvicorn api.polish:app --reload --host 0.0.0.0 --port 8002

# 访问 http://127.0.0.1:8002 查看 API 文档
```

#### 使用 Netlify CLI
```bash
# 安装 Netlify CLI
npm install -g netlify-cli

# 启动本地开发服务器
netlify dev

# 访问 http://localhost:3000 查看页面
```

## 注意事项

1. **API Key 安全**：不要将 API Key 提交到版本控制系统
2. **CORS 配置**：生产环境建议限制访问域名
3. **错误处理**：生产环境不会返回详细的错误信息

## 许可证

MIT License