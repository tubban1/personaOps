# PersonaOps 运行手册 (Runbook)

## 📍 1. 运行流程概述
系统支持从内容规划、媒体渲染到物理发布的全量生命周期管理。

## ⚙️ 2. 环境说明
在 `data/.env` 中配置您的核心凭证：
```env
VECTORENGINE_API_KEY=xxx
VECTORENGINE_URL=https://api.example.com/v1
VECTORENGINE_IMAGE_MODEL=dall-e-3
```

## 🛠️ 3. 运行模式 (Modes)

### A. 全链路运行 (Planning -> Media -> Publishing)
```bash
python3 main.py --mode full
```
*   **适用场景**：日常自动化运营。
*   **默认行为**：加载林小棠人设与四川品牌，模拟发布在小红书测试账号。

### B. 仅规划模式 (Planning Only)
```bash
python3 main.py --mode plan
```
*   **适用场景**：审查内容计划，暂不产生图片资产。

### C. 仅媒体模式 (Media Only)
```bash
python3 main.py --mode media
```
*   **适用场景**：单独为已有的计划生成图片或进行渲染基准测试。

### D. 环境与覆盖 (Overrides)
您可以通过 CLI 指定具体的运营渠道：
```bash
python3 main.py --platform instagram --account your_insta_user
```

## 📊 4. 查看运行审计 (Auditing)
所有运行输出统一存于 `data/` 目录：
*   **任务快照**：`data/audit/run_run_p_{timestamp}.json` (聚合回执)
*   **渲染记录**：`data/assets/{plan_id}/{timestamp}/render_log.json`
*   **发布详情**：`data/audit/aud_{publish_id}.json`

---
*Owl Lab Operation Engineering*
