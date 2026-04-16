# PersonaOps: The Unified AI Persona Operating System

`personaOps` 是一个工业级、全闭环的 AI 人设运营系统。它将人设规划、品牌对齐、互动感知、媒体生产与多平台分发整合为一个统一的自治逻辑单元。

> **核心现状**：目前系统已完成从 `socialMedia` 仓库的功能全量迁入。`personaOps` 已成为具备独立执行主权的主控系统，原有的双项目协作模式已升级为单项目内核架构。

## 🪐 系统架构 (The Unified Loop)

系统运行在六大核心域之上：

1.  **Persona & Brand Domain**：人设与品牌资产建模，定义“我是谁”与“为谁服务”。
2.  **Planning Domain**：`ContentBrain` 负责叙事线规划，生成连续的 `PostPlan`。
3.  **Interaction Domain**：`InteractionBrain` 实时感知社交媒体反馈，进行意图识别与风险管控。
4.  **Media Domain**：`MediaCoordinator` 驱动双引擎（Template + AI Image）生产高保真视觉资产。
5.  **Publish Domain**：统一驱动层，承载多平台（XHS, Instagram）的物理执行。
6.  **Audit Domain**：全链路审计，追踪从“一个念头”到“一次发布”的每一分钱支出与每一次行为结果。

## 🚀 快速启动

### 1. 安装依赖
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 配置环境
在 `data/.env` 中配置您的 VectorEngine API 凭证：
```env
VECTORENGINE_API_KEY=your_key
VECTORENGINE_URL=https://api.example.com/v1
VECTORENGINE_IMAGE_MODEL=dall-e-3
```

### 3. 运行执行引擎
您可以直接运行默认演示，或者通过命令行灵活配置运行参数：

```bash
# 运行默认演示 (林小棠 @ 小红书)
python3 main.py

# 指定其他人设与品牌
python3 main.py --persona data/entities/personas/custom_p.json --brand data/entities/brands/custom_b.json

# 一键切换发布平台与账号 (Override)
python3 main.py --platform instagram --account my_insta_01
```

#### CLI 参数列表
- `--persona`: 指定人设配置文件 (.json)
- `--brand`: 指定品牌配置文件 (.json)
- `--channel`: 指定渠道配置文件 (.json)
- `--platform`: 强制覆盖发布平台 (xhs, instagram)
- `--account`: 强制覆盖账号 ID
- `--real`: 开启真实发布模式（默认 mock 模式）

## 🏗️ 核心契约 (Key Contracts)

*   **`PostPlan`**：规划层与生产层的核心契约。
*   **`MediaPackage`**：媒体层与执行层的资产交付契约。
*   **`CaptionSchema`**：全系统通用的结构化文案契约。
*   **`AuditRecord`**：统一的执行回执与财务审计契约。

## 🛡️ 边界声明 (Boundary Decisions)

*   **主权归属**：所有业务逻辑、渲染引擎、发布驱动均驻留在 `personaOps`。
*   **Legacy 说明**：`socialMedia` 项目目前仅作为历史代码贡献源，不再参与生产环境的任务分发与执行。

---
*Created by Owl Lab*
