# 边界决策文档 (Boundary Decision)

## 1. 核心共识
从 2026-04-16 起，`personaOps` 已完成从“管理端”向“执行端”的一体化升级。系统边界不再划分“策略 vs 执行”，而是划分为“内部原子本领”。

## 2. 物理边界清单

| 组件/本领 | 现有所属项目 | 状态 | 说明 |
| :--- | :--- | :--- | :--- |
| **人设与品牌策略** | `personaOps` | 已立项 | 系统的逻辑起点 |
| **内容规划大脑** | `personaOps` | 已迁入 | 原 `socialMedia` 逻辑已重构 |
| **互动感知大脑** | `personaOps` | 已建立 | 核心安全护城河 |
| **Canvas 渲染引擎** | `personaOps` | 已迁入 | 物理渲染在 `personaOps` 完成 |
| **AI 生图引擎** | `personaOps` | 已建立 | 视觉一致性管理在此闭环 |
| **平台执行驱动** | `personaOps` | 已迁入 | 浏览器自动化与 API 提交在此执行 |
| **执行审计日志** | `personaOps` | 已建立 | 统一存储于 `personaOps/data/audit/` |

## 3. 弃用说明 (Deprecation)
*   **`socialMedia` 仓库**：现仅作为受保护的历史资产库（Legacy Donor）。不再向其下发任务。
*   **`SocialMediaAdapter`**：已废弃。系统通过 `app/runtime/manager.py` 直接调用具体的 Platform Drivers。

## 4. 数据流动方向
所有产生的数据（资产、文案、审计报告）均驻留在 `personaOps/data/` 目录下，该目录是系统的唯一持久化事实来源。
