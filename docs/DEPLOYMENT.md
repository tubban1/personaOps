# PersonaOps 部署手册 (Deployment)

## 🐳 1. 环境准备
确保您的物理机满足以下基础需求：
- **操作系统**：Linux / MacOS (推荐)
- **Python**：3.10+
- **网络**：可稳定访问 VectorEngine API 与 社交媒体平台

## 📦 2. 部署步骤

### 第一步：克隆项目并安装依赖
```bash
git clone https://path/to/personaOps.git
cd personaOps
pip install -r requirements.txt
```

### 第二步：安装渲染环境 (Playwright)
```bash
playwright install chromium
```

### 第三步：配置环境变量
在项目根目录运行或手动创建 `data/.env`：
```bash
cp data/.env.example data/.env # (若有样例文件)
```

### 第四步：初始化目录结构
首次运行时项目会自动创建必要的数据子目录：
- `data/entities/`
- `data/assets/`
- `data/audit/`
- `data/auth/`
- `data/memory/`

### 第五步：运行冒烟测试
```bash
python3 main.py --mode plan
```

## 🛡️ 3. 安全与权限 (Security)

1.  **凭证保护**：不要将 `data/.env` 或 `data/auth/` 提交至版本管理。
2.  **API 指导**：确保 `VECTORENGINE_API_KEY` 具备 `image:generation` 与 `text:completion` 权限。
3.  **浏览器权限**：在服务器环境运行，请确保具备运行 `headless` 浏览器的系统库依赖。

---
*Owl Lab Infrastructure Team*
