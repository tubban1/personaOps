# personaOps Execution Layer Migration Plan

## 1. 战略转变 (Strategic Shift)
本项目已从“双项目协作模型”转变为“单项目集成模型”。
`personaOps` 将逐步吞并 `socialMedia` 的成熟执行能力，成为唯一的主系统。`socialMedia` 仓库现在被视为 **Migration Source (代码供体)**。

## 2. 最终项目结构 (Target Architecture)

`personaOps` 最终将包含以下控制域：

*   **Decision Layer**:
    *   `app/persona`, `app/brand`, `app/planning`, `app/interaction`, `app/memory`
*   **Execution Layer (Migrated)**:
    *   `app/media`: 蓝图解析、模板渲染、AI 图像生成流水线。
    *   `app/publish`: 平台驱动（XHS, Instagram, etc.）、帐号 Session 管理。
    *   `app/runtime`: 任务状态机、并发调度、物理目录管理。
    *   `app/audit`: 渲染日志、发布回执、资产对账。

## 3. 迁移阶段计划 (Phased Roadmap)

### Phase 3.5: 架构对齐 (Architecture Freeze)
*   **目标**：停止集成路线，建立执行层目录骨架。
*   **任务**：创建 `media`, `publish`, `runtime`, `audit` 目录；清理 `delivery_adapter` 的依赖。

### Phase 4: 发布与契约层迁移 (Publish & Contract)
*   **目标**：让 `personaOps` 具备直接发布能力。
*   **迁移模块**：
    *   `platforms/xhs/*`, `platforms/instagram/*` (Driver 逻辑)
    *   `content/caption_schema.py` (完全接管)
    *   `core/models.py` 中的执行状态流转思想。

### Phase 5: 渲染引擎迁移 (Media Engine)
*   **目标**：让 `personaOps` 具备直接生成资产的能力。
*   **迁移模块**：
    *   `agents/producer.py` (重构为 MediaCoordinator)
    *   `content/orchestrator.py` & `engine_canvas.py`
    *   `archetypes/` (模板库)

### Phase 6: 清理与弃用 (Legacy Decommission)
*   **目标**：彻底关停 `socialMedia` 独立运行权限。
*   **任务**：移除双系统 Adapter，整合 `main.py` 入口。

## 4. 迁移原则 (Rules of Engagement)

1.  **重构而非无脑复制**：迁入代码必须删除 `socialMedia` 历史遗留的僵尸逻辑。
2.  **对象适配**：底层 Driver 必须由 `personaOps` 的 `Persona` 和 `PostPlan` 驱动，不再引用旧的 `Task` 模型。
3.  **边界清晰**：`app/publish` 只管发布，不产生任何创意决策。

---
*Status: In Evolution (2026-04-16)*
