# Netlify 部署指南

## 方法一：通过 Netlify 控制台部署

### 1. 准备工作
- 注册 Netlify 账户：https://www.netlify.com
- 安装 Git CLI（如果还没安装）
- 将代码推送到 GitHub/GitLab/Bitbucket

### 2. 导入项目到 Netlify

1. 登录 Netlify 控制台
2. 点击 "Add new site" → "Import an existing project"
3. 选择你的 Git 提供商（GitHub/GitLab/Bitbucket）
4. 选择 `ai-text-polish` 仓库
5. 点击 "Import site"

### 3. 配置构建设置

在 "Build & deploy" → "Build settings" 中：

- **Build command**: `pip install -r requirements.txt`
- **Publish directory**: `public`
- **Functions directory**: `netlify/functions`

### 4. 设置环境变量

1. 进入 "Site settings" → "Environment variables"
2. 添加新的环境变量：
   - Key: `ZHIPU_API_KEY`
   - Value: `your_real_api_key_here`
3. 保存设置

### 5. 重新部署

设置环境变量后，需要手动触发部署：
- 在 "Deploys" 页面点击 "Trigger deploy" → "Deploy site"

---

## 方法二：使用 Netlify CLI 部署

### 1. 安装 Netlify CLI

```bash
npm install -g netlify-cli
```

### 2. 登录 Netlify

```bash
netlify login
```

### 3. 初始化项目

```bash
cd /Users/loveapple/Desktop/code/ai-text-polish
netlify init
```

按照提示操作：
- 选择 "Create & configure a new site"
- 选择你的团队
- 输入站点名称（例如：`ai-text-polish-cute`）

### 4. 设置环境变量

```bash
netlify env:set ZHIPU_API_KEY your_real_api_key_here
```

### 5. 本地测试（可选）

```bash
# 启动本地开发服务器
netlify dev

# 或者直接启动 FastAPI 服务器
python3 -m uvicorn api.polish:app --reload --host 0.0.0.0 --port 8002
```

### 6. 部署到生产环境

```bash
# 部署到预览环境
netlify deploy

# 部署到生产环境
netlify deploy --prod
```

---

## 方法三：持续集成部署（推荐）

### 1. 推送代码到 Git

```bash
git add .
git commit -m "准备部署到 Netlify"
git push origin main
```

### 2. Netlify 自动部署

Netlify 会自动检测到 Git 推送并开始部署：
- 在 Netlify 控制台查看部署进度
- 部署完成后会获得一个 `.netlify.app` 域名

---

## 验证部署

### 1. 检查 Functions 是否正常部署

访问：`https://your-site-name.netlify.app/.netlify/functions/polish`

应该返回 JSON 响应。

### 2. 测试前端页面

访问：`https://your-site-name.netlify.app`

在文本框中输入文字，点击"✨ 魔法改写 ✨"按钮，查看是否能正常改写。

---

## 常见问题

### Q: 部署后报错 "ZHIPU_API_KEY environment variable not set"

**A:** 在 Netlify 控制台的 "Site settings" → "Environment variables" 中设置 `ZHIPU_API_KEY`，然后重新部署。

### Q: Function 超时

**A:** Netlify Functions 默认超时时间为 10 秒。如果 AI 响应较慢，可以在 `netlify.toml` 中添加：
```toml
[functions]
  timeout = 30  # 超时时间（秒）
```

### Q: 本地开发时 API 调用失败

**A:** 确保本地 FastAPI 服务器正在运行：
```bash
python3 -m uvicorn api.polish:app --reload --host 0.0.0.0 --port 8002
```

### Q: CORS 错误

**A:** Netlify Functions 已配置 CORS 头，如果仍有问题，检查浏览器控制台的错误信息。

---

## 自定义域名（可选）

### 1. 在 Netlify 控制台配置

1. 进入 "Site settings" → "Domain management"
2. 点击 "Add custom domain"
3. 输入你的域名（例如：`textpolish.yourdomain.com`）

### 2. 配置 DNS

按照 Netlify 提供的 DNS 记录配置你的域名解析。

---

## 环境变量管理

### 查看环境变量

```bash
netlify env:list
```

### 添加环境变量

```bash
netlify env:set KEY_NAME value
```

### 删除环境变量

```bash
netlify env:unset KEY_NAME
```

---

## 监控和日志

### 查看函数日志

1. 进入 Netlify 控制台
2. 点击 "Functions" 标签
3. 选择 "polish" 函数
4. 查看 "Function logs"

### 本地日志

```bash
netlify dev
```

---

## 性能优化建议

1. **启用 CDN 缓存**：Netlify 默认已启用 CDN 缓存
2. **使用图片优化**：压缩静态资源
3. **启用 Gzip 压缩**：在 `netlify.toml` 中添加：
```toml
[[headers]]
  for = "/*"
  [headers.values]
    Content-Type = "text/html; charset=utf-8"
    Cache-Control = "public, max-age=0, must-revalidate"
    X-Frame-Options = "SAMEORIGIN"
    X-Content-Type-Options = "nosniff"
```

---

## 下一步

- [ ] 设置自定义域名
- [ ] 配置环境变量（ZHIPU_API_KEY）
- [ ] 测试所有功能
- [ ] 配置监控和告警
- [ ] 设置自动备份

祝部署顺利！🚀
