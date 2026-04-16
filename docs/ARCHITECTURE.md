# personaOps System Architecture (V4.2)

## 1. 核心战略：单项目闭环 (Unified System Strategy)
本项目（personaOps）正处于从“决策引擎”向“全栈 AI 人员系统”的演进过程中。目前的战略是**逐步吞并 `socialMedia` 项目的成熟执行能力**，最终实现从角色建模、内容规划到物理发布的单项目闭环。

## 2. 逻辑架构层 (Logical Layers)

### A. 认知域 (Cognition Domain)
*   **Persona Manager**: 角色性格、生命史、人设红线。
*   **Brand Binding**: 品牌调性约束、业务目标注入。

### B. 策略域 (Planning Domain)
*   **Content Brain**: 周计划编排、支柱分配。
*   **Story Engine**: 叙事弧线控制、剧情节奏点感知。

### C. 互动域 (Perception & Interaction)
*   **Interaction Brain**: 意图识别（咨询/夸赞/投诉）、风险判定、回复建议建议、线索标记 (LeadMark)。

### D. 执行域 (Execution Domain - Migrated)
*   **Media Pipeline**: 模板资产调度、AI 生成图像、资产自审计。
*   **Publish Layer**: 平台发布驱动（XHS, Instagram）、文案契约解析。

## 3. 演进状态 (Migration Status)
系统目前处于 **Phase 4: 执行层迁移**。
*   `personaOps` 已具备直接驱动平台发布（XHSDriver）的能力。
*   `socialMedia` 仓库目前仅作为“代码供体”和“临时渲染服务”存在，后续将被完全淘汰。

---
*Updated: 2026-04-16*
