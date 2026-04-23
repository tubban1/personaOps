# Phase 5A: Media & Render Pipeline Migration Plan

## 1. 目标 (Objectives)
将 `socialMedia` 仓库中成熟的视觉资产生成能力全量迁入 `personaOps`。重点在于实现从 `PostPlan` 到物理图文资产（MediaPackage）的自动化转换。

## 2. 迁入路径 (Migration Source & Target)

| 功能 (Feature) | 源文件 (socialMedia) | 目标位置 (personaOps) | 改造重点 |
| :--- | :--- | :--- | :--- |
| **Orchestrator** | `app/content/orchestrator.py` | `app/media/orchestrator.py` | 适配 PostPlan 语义，去掉 Task 依赖 |
| **Blueprint** | `app/content/blueprint.py` | `app/media/blueprint.py` | 整合 Persona & Brand 视觉约束 |
| **Canvas Engine** | `app/render/engine_canvas.py` | `app/media/engine_canvas.py` | 统一输出目录到 data/assets |
| **Archetypes** | `app/content/archetypes/*` | `app/media/archetypes/*` | 保持 HTML/CSS 结构一致 |
| **Registry** | `app/content/template_registry.py` | `app/media/template_registry.py` | 简化为单项目注册表 |

## 3. 核心契约：MediaPackage
`media` 域的最终产物不再是散乱的文件，而是封装好的 `MediaPackage` 对象。
该对象将包含：
*   所有生成的图片路径。
*   符合平台政策的 `caption.json`。
*   渲染过程审计 `render_log.json`。

## 4. 关键改造点
1.  **输入升级**：Orchestrator 不再接收 `topic` 字符串，而是接收 `PostPlan` 对象。
2.  **视觉语义**：从 Blueprint 层就开始注入 `Persona.visual_profile` 约束，确保“人设感”在画面层面的落地。
3.  **审计闭环**：在 `app/audit/models.py` 中增加渲染级审计记录。

## 5. 本阶段非目标 (Non-Goals for 5A)
*   高性能多卡 AI 生图调度。
*   视频剪辑与语音合成。
*   动态画布 (Dynamic Canvas) 交互。

---
*Generated: 2026-04-16*
