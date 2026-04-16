# 交付契约 (Delivery Contract)

## 1. 概述
本系统不再依赖跨项目 API 调用。所有“交付”均发生在 `personaOps` 内部不同领域的 Service 之间。

## 2. 三大核心内部交付件

### A. 规划交付件 (`PostPlan`)
*   **生产者**：`ContentBrain`
*   **消费者**：`MediaCoordinator`
*   **内容**：包含 `topic_seed`, `story_context`, `intent`, `references`。
*   **意义**：决定了生产什么的“念头”。

### B. 资产交付件 (`MediaPackage`)
*   **生产者**：`MediaCoordinator`
*   **消费者**：`RuntimeManager`
*   **内容**：
    *   `images[]`: 物理生成的图片路径。
    *   `caption.json`: 根据 `CaptionSchema` 生成的结构化文案。
    *   `render_log.json`: 渲染审计记录。
*   **意义**：具备分发条件的成品包裹。

### C. 执行执行回执 (`AuditRecord`)
*   **生产者**：`RuntimeManager` (Driver)
*   **消费者**：`Audit Domain` / `Business Logic`
*   **内容**：`status`, `audit_id`, `cost_metrics`, `platform_response`。
*   **意义**：代表该任务在物理世界已发生。

## 3. 标准目录结构
交付资产必须符合以下持久化约定：
*   **资产存储**：`data/assets/{plan_id}/{timestamp}/`
*   **审计存储**：`data/audit/aud_{id}.json`
*   **凭证存储**：`data/auth/`
