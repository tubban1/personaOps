# Phase 7 Step 1: Dashboard Service 与只读 API 契约设计

## 目标
为 `Ops Console / Run Dashboard` 定义一个稳定的数据服务层，让前端不直接扫描 `data/` 和 JSON 文件，而是通过统一的只读 API 获取运行事实、资产预览和审计信息。  
这一层是后续 FastAPI MVP 的基础，不承担业务执行，只负责“读取、归一化、暴露”。

## 为什么前端不能直接扫 `data/` 和 JSON
1. 文件结构是物理存储细节，不是稳定的产品契约。前端一旦依赖目录布局，后续重构会直接破坏页面。
2. 当前系统存在部分成功、历史脏数据、缺失文件等真实情况，前端不应自己猜文件是否完整。
3. 直接扫盘会把解析逻辑散落到多个页面，导致状态解释不一致。
4. `mock_mode`、`real`、审计状态、运行状态需要统一归一，否则页面会出现“文件存在但业务上无效”的误判。
5. 后续如果迁移到数据库或对象存储，扫描文件的前端实现无法平滑升级。

## 建议的数据服务层
建议新增一个轻量数据服务层，名称可以是 `DashboardService`，内部可以拆成两个概念：

1. `RunRegistry`
   - 负责枚举、索引和定位 run。
   - 输入是 `data/audit`、`data/assets`、`data/entities` 下的现有文件。
   - 输出是经过归一化的 run 索引和 run 详情。
2. `DashboardService`
   - 负责聚合 `PipelineRunRecord`、`PostPlan`、`MediaPackage`、`RenderAudit`、`AuditRecord`。
   - 负责把分散文件转换成前端可消费的稳定对象。
   - 负责错误语义归一，例如缺失、部分可读、脏数据、解析失败。

## 建议输出的数据对象

### 1. Run Summary
用于列表页和首页卡片。

建议字段：
```json
{
  "run_id": "run_p_20260417_120000",
  "status": "success",
  "mode": "full",
  "mock_mode": true,
  "persona_id": "persona_xxx",
  "brand_id": "brand_xxx",
  "channel_id": "channel_xxx",
  "platform": "xhs",
  "account_id": "acct_001",
  "started_at": "2026-04-17T12:00:00",
  "finished_at": "2026-04-17T12:03:10",
  "counts": {
    "post_plans": 1,
    "media_packages": 1,
    "publish_audits": 1
  },
  "health": "complete"
}
```

### 2. Run Detail
用于运行详情页。

建议字段：
```json
{
  "summary": { "...": "same as run summary" },
  "post_plans": ["post_plan_id_1"],
  "media_packages": ["media_pkg_id_1"],
  "publish_audits": ["aud_12345678"],
  "timeline": [
    { "stage": "planning", "status": "success" },
    { "stage": "media", "status": "success" },
    { "stage": "publish", "status": "success" }
  ],
  "warnings": [],
  "errors": []
}
```

### 3. Asset Preview
用于媒体资产详情和缩略图区域。

建议字段：
```json
{
  "media_package_id": "pkg_xxx",
  "post_plan_id": "plan_xxx",
  "platform": "xhs",
  "asset_dir": "data/assets/...",
  "images": [
    { "name": "img_01.png", "url": "/assets/plan_xxx/...", "exists": true }
  ],
  "caption": {
    "path": "data/assets/.../caption.json",
    "exists": true,
    "content": { "...": "CaptionSchema" }
  },
  "render_log": {
    "path": "data/assets/.../render_log.json",
    "exists": true,
    "content": { "...": "RenderAudit" }
  },
  "status": "ready",
  "coverage_score": 1.0,
  "mock_mode": true
}
```

### 4. Audit Detail
用于发布结果和执行回执页。

建议字段：
```json
{
  "audit_id": "aud_12345678",
  "plan_id": "plan_xxx",
  "platform": "xhs",
  "account_id": "acct_001",
  "status": "success",
  "mode": "mock",
  "driver_name": "XHS",
  "error": null,
  "receipt": { "...": "platform response" },
  "created_at": "2026-04-17T12:03:10"
}
```

## 建议的只读 API 列表
以下 API 目标是服务 `Run Dashboard`，不做写操作。

### 1. `GET /api/dashboard/runs`
用途：运行列表。

输入：
1. `status` 可选。
2. `mode` 可选。
3. `platform` 可选。
4. `mock_mode` 可选。
5. `page`、`page_size` 可选。

输出：
1. `items: RunSummary[]`
2. `total`
3. `page`
4. `page_size`

错误语义：
1. 目录不可读时返回 `503 DASHBOARD_STORAGE_UNAVAILABLE`。
2. 单个 run 文件损坏不应导致列表失败，应该跳过并记录 `partial_data`.

### 2. `GET /api/dashboard/runs/{run_id}`
用途：运行详情。

输入：
1. `run_id`

输出：
1. `RunDetail`

错误语义：
1. run 不存在返回 `404 RUN_NOT_FOUND`。
2. run 存在但部分依赖文件缺失时返回 `200`，同时在 `warnings` 中标记 `missing_media_package`、`missing_audit` 等问题。

### 3. `GET /api/dashboard/runs/{run_id}/assets/{media_package_id}`
用途：资产预览。

输入：
1. `run_id`
2. `media_package_id`

输出：
1. `AssetPreview`

错误语义：
1. 对应包不存在返回 `404 ASSET_PACKAGE_NOT_FOUND`。
2. 图片或 `caption.json` 缺失时不直接报整体错误，应返回 `partial=true` 并标注缺失项。

### 4. `GET /api/dashboard/audits/{audit_id}`
用途：审计详情。

输入：
1. `audit_id`

输出：
1. `AuditDetail`

错误语义：
1. 审计文件不存在返回 `404 AUDIT_NOT_FOUND`。
2. 审计 JSON 解析失败返回 `422 AUDIT_PARSE_ERROR`。

### 5. `GET /api/dashboard/health`
用途：数据服务健康检查。

输出：
1. `status`
2. `storage_root`
3. `counts`
4. `last_scan_at`

## `mock_mode` / `real` 的显式暴露方案
`mock_mode` 不应只在执行层存在，而应该贯穿 Dashboard 数据层。

建议做法：
1. `RunSummary` 和 `RunDetail` 必须显式暴露 `mock_mode`。
2. `AuditDetail` 必须暴露 `mode`，与 `mock_mode` 形成双重确认。
3. UI 层应使用清晰标识区分 mock 与 real，避免误把模拟结果当成真实发布结果。
4. 对真实发布数据，服务层可以额外返回 `risk_level=high` 或 `execution_scope=real` 这类只读标签。

## `ProjectPaths.ASSETS` 的静态资源映射建议
当前资产目录已经由 `ProjectPaths.ASSETS = DATA / "assets"` 统一管理。  
建议 Dashboard Service 不直接暴露物理路径，而是把静态文件映射为统一的只读 URL 前缀。

建议映射：
1. 物理目录：`data/assets/{plan_id}/{timestamp}/...`
2. HTTP 前缀：`/assets/{plan_id}/{timestamp}/...`
3. 服务职责：把 `ProjectPaths.ASSETS` 下的文件安全地映射到静态资源服务。

注意：
1. 只读映射必须限制在 `ProjectPaths.ASSETS` 范围内。
2. 不允许通过 URL 穿透到 `data/auth`、`data/entities` 等敏感目录。
3. 如果文件不存在，应该返回标准 404，而不是把物理路径暴露给前端。

## 缺失文件、历史脏数据、部分成功 run 的处理
这是 Dashboard Service 必须优先解决的问题。

建议规则：
1. run 文件存在，但某些 `media_package_id` 缺失时，run 仍可展示，状态标记为 `partial`.
2. run 成功，但某个 asset 目录中的 `caption.json` 缺失时，资产页返回部分数据并附带 warning.
3. 历史脏数据如果 JSON 无法解析，列表仍应返回，只是该条记录标记为 `corrupt`.
4. 部分成功 run 要允许同时存在 success stage 和 failed stage，不强行压成单一状态。
5. 对于 `publish` 成功但 `media` 不完整的历史数据，优先展示已知事实，不做臆断补全。

建议状态枚举：
1. `complete`
2. `partial`
3. `missing`
4. `corrupt`
5. `orphaned`

## 与现有模型和目录结构的映射
1. `app/runtime/models.py`
   - `PipelineRunRecord` 对应 `RunSummary` 和 `RunDetail` 的主来源。
2. `app/media/models.py`
   - `MediaPackage` 对应 `AssetPreview` 的主来源。
   - `RenderAudit` 对应资产页中的渲染审计内容。
3. `app/audit/models.py`
   - `AuditRecord` 对应 `AuditDetail`。
4. `app/planning/models.py`
   - `PostPlan`、`WeeklyPlan`、`ChannelProfile` 用于 run detail 的上下文补充。
5. `app/runtime/pipeline_runner.py`
   - 定义了实际执行阶段边界，是 Dashboard timeline 的事实来源。
6. `app/core/paths.py`
   - `ProjectPaths.DATA`、`ProjectPaths.ASSETS`、`ProjectPaths.AUDIT` 是数据扫描入口。

## 推荐实现顺序
1. 先做 `DashboardService`，把本地文件归一化成稳定对象。
2. 再做 FastAPI 只读路由，把 service 输出暴露成 API。
3. 最后再接 UI，避免前端先行绑定不稳定的数据形状。

## 实施原则
1. 前端只消费契约，不消费目录结构。
2. 服务层只做读取和归一化，不做业务改写。
3. 所有异常都要保留“部分可用”的可能性，不要让单点损坏拖垮整页。
4. 对真实发布和模拟发布，必须在数据层显式区分。

