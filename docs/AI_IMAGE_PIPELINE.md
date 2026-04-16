# Phase 5B: AI Image Pipeline Architecture

## 1. 核心链路 (Dual-Path Orchestration)
`personaOps` 现在支持两种并行的视觉生产路径，由 `RenderStrategy` 自动调度：

*   **路径 A: Template (Canvas Engine)**
    *   适用场景：数据报告、结构化知识、强文字信息图。
    *   技术栈：HTML5 + CSS3 + Playwright。
*   **路径 B: AI Image (Generative Engine)**
    *   适用场景：生活随拍、封面氛围图、人物叙事背景、具象场景呈现。
    *   技术栈：VectorEngine API (DALL-E 3 / Flux) + Prompt Engineering。

## 2. 人物视觉一致性 (Visual Consistency)
我们通过 `PortraitConsistency` 管理人设的“视觉锚点”（Visual Anchors）：
*   **特征固定**：发型、五官特征、常驻穿搭风格、气质描述。
*   **Prompt 注入**：每一个 AI 生图请求都会强制注入这些锚点，确保生成结果不偏离林小棠（p_001）的基础形象。

## 3. 提示词工程 (Prompt Engineering)
`ImagePromptBuilder` 负责将多维信息压缩为高质量 Prompt：
*   **Input**: `Persona` + `Brand` + `PostPlan` + `Storyline Context`。
*   **Structure**: [人设锚点] + [动作/场景描述] + [镜头与光影] + [风格约束] + [负向提示词]。

## 4. 环境变量与安全 (Secret Management)
所有配置严格通过 `app/core/settings.py` 处理：
*   `VECTORENGINE_API_KEY`: 核心凭证。
*   `VECTORENGINE_URL`: API 端点。
*   `VECTORENGINE_IMAGE_MODEL`: 指定模型（如 `dall-e-3`）。

## 5. 审计与回溯 (Auditability)
渲染结果包含 `prompt.json` 与 `render_log.json`：
*   记录完整的生成的 Prompt。
*   记录使用的模型与渲染引擎。
*   保存 Mock/Real 状态标识。

---
*Last Updated: 2026-04-16*
