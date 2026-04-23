import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path

from app.core.paths import ProjectPaths
from app.dashboard.models import (
    RunSummary, RunDetail, RunStatus, RunHealth, 
    RunTimelineItem, AssetPreview, ImageAssetPreview, AuditDetail
)
# 注意：我们复用现有模型进行解析
from app.runtime.models import PipelineRunRecord
from app.media.models import MediaPackage, RenderAudit

logger = logging.getLogger("DashboardService")

class DashboardService:
    """
    负责从物理存储 (data/*) 读取事实并归一化为 Dashboard API 对象。
    实现“只读、健壮、脱耦”的数据层。
    """

    @staticmethod
    def _parse_datetime(dt_str: Any) -> datetime:
        if isinstance(dt_str, datetime):
            return dt_str
        try:
            return datetime.fromisoformat(str(dt_str))
        except:
            return datetime.min

    def list_runs(self, limit: int = 50) -> List[RunSummary]:
        """枚举所有运行记录并生成概览"""
        runs = []
        audit_dir = ProjectPaths.AUDIT
        
        if not os.path.exists(audit_dir):
            return []

        # 找出所有可能的运行记录文件，排除 publish 审计收据 (aud_*)
        all_files = os.listdir(audit_dir)
        run_files = sorted(
            [f for f in all_files if f.endswith(".json") and not f.startswith("aud_")],
            reverse=True
        )

        for filename in run_files[:limit]:
            file_path = os.path.join(audit_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    
                # 1. ID 归一化
                actual_id = data.get("id") or data.get("run_id") or filename.replace(".json", "").replace("run_", "")
                
                # 2. 获取元数据
                mode = data.get("mode", "full")
                media_ids = data.get("media_package_ids", [])
                audit_ids = data.get("publish_audit_ids", [])
                post_plans = data.get("post_plan_ids", [])

                # 3. 语义健康度实测
                health = RunHealth.COMPLETE
                missing_count = 0
                
                # 预期检查：基于模式判断是否应该有产物
                expect_media = mode in ["full", "media"]
                expect_publish = mode in ["full", "publish"]
                
                # A. 检查已声明的依赖是否物理存在
                total_declared = len(media_ids) + len(audit_ids)
                
                for i, m_id in enumerate(media_ids):
                    p_id = post_plans[i] if i < len(post_plans) else (post_plans[0] if post_plans else "unknown")
                    if not os.path.exists(os.path.join(ProjectPaths.ASSETS, p_id, m_id)):
                        missing_count += 1
                
                for a_id in audit_ids:
                    if not os.path.exists(os.path.join(audit_dir, f"{a_id}.json")):
                        missing_count += 1
                
                # B. 检查 模式/预期 是否脱节 (例如 full 模式但无 audit ID)
                semantic_gap = False
                if expect_media and not media_ids: semantic_gap = True
                if expect_publish and not audit_ids: semantic_gap = True

                if missing_count > 0 or semantic_gap:
                    # 如果有东西丢了，或者根本没生成预期的产物，根据丢失比例判定
                    if total_declared == 0 and semantic_gap:
                        health = RunHealth.PARTIAL # 流程中断或失败
                    else:
                        health = RunHealth.PARTIAL if missing_count < total_declared else RunHealth.MISSING
                
                # 4. 基础字段提取
                started_at = self._parse_datetime(data.get("started_at", data.get("created_at")))
                finished_at = self._parse_datetime(data.get("finished_at")) if data.get("finished_at") else None

                summary = RunSummary(
                    run_id=actual_id,
                    status=RunStatus(data.get("status", "success")),
                    mode=mode,
                    mock_mode=data.get("mock_mode", True),
                    persona_id=data.get("persona_id"),
                    brand_id=data.get("brand_id"),
                    channel_id=data.get("channel_id"),
                    platform=data.get("platform"),
                    account_id=data.get("account_id"),
                    started_at=started_at,
                    finished_at=finished_at,
                    counts={
                        "post_plans": len(post_plans),
                        "media_packages": len(media_ids),
                        "publish_audits": len(audit_ids)
                    },
                    health=health
                )
                runs.append(summary)
            except Exception as e:
                logger.warning(f"Failed to parse run file {filename}: {e}")
                runs.append(RunSummary(
                    run_id=filename.replace(".json", "").replace("run_", ""),
                    status=RunStatus.FAILED,
                    mode="unknown",
                    mock_mode=True,
                    started_at=datetime.fromtimestamp(os.path.getctime(file_path)),
                    health=RunHealth.CORRUPT
                ))

        return runs

    def get_run_detail(self, run_id: str) -> Optional[RunDetail]:
        """获取单个运行的详细数据及依赖项列表"""
        # 尝试两种可能的物理文件名：1. 直接 ID, 2. 带 run_ 前缀
        possible_paths = [
            os.path.join(ProjectPaths.AUDIT, f"{run_id}.json"),
            os.path.join(ProjectPaths.AUDIT, f"run_{run_id}.json")
        ]
        
        data = None
        for p in possible_paths:
            if os.path.exists(p):
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        break
                except: continue
        
        if data is None:
            return None

        try:
            # 使用 list_runs 获取归一化后的 Summary
            summaries = self.list_runs(limit=1000)
            match_summary = next((s for s in summaries if s.run_id == run_id), None)
            
            if not match_summary:
                return None

            detail = RunDetail(summary=match_summary)
            detail.post_plans = data.get("post_plan_ids", [])
            detail.media_packages = data.get("media_package_ids", [])
            detail.publish_audits = data.get("publish_audit_ids", [])
            
            # 生成时间轴事实
            if match_summary.started_at:
                detail.timeline.append(RunTimelineItem(stage="start", status="ok", timestamp=match_summary.started_at))
            
            if detail.post_plans:
                detail.timeline.append(RunTimelineItem(stage="planning", status="success"))
            if detail.media_packages:
                detail.timeline.append(RunTimelineItem(stage="media", status="success"))
            if detail.publish_audits:
                detail.timeline.append(RunTimelineItem(stage="publish", status="success"))
                
            if match_summary.finished_at:
                detail.timeline.append(RunTimelineItem(stage="finish", status="ok", timestamp=match_summary.finished_at))

            return detail
        except Exception as e:
            logger.error(f"Error reading run detail {run_id}: {e}")
            return None

    def get_asset_preview(self, media_package_id: str, plan_id: str) -> Optional[AssetPreview]:
        """
        预览媒体资产包。
        注意：media_package_id 通常是 timestamp，路径在 data/assets/{plan_id}/{timestamp}
        """
        pkg_dir = os.path.join(ProjectPaths.ASSETS, plan_id, media_package_id)
        if not os.path.exists(pkg_dir):
            return None

        preview = AssetPreview(
            media_package_id=media_package_id,
            post_plan_id=plan_id,
            platform="unknown", # 尝试从 render_log 提取
            asset_dir=pkg_dir
        )

        # 扫描图片
        images = sorted([f for f in os.listdir(pkg_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        for img in images:
            # URL 在 API 层映射，此处先保留相对路径
            preview.images.append(ImageAssetPreview(
                name=img,
                url=f"/assets/{plan_id}/{media_package_id}/{img}",
                exists=True
            ))

        # 加载 Caption
        caption_path = os.path.join(pkg_dir, "caption.json")
        if os.path.exists(caption_path):
            preview.caption_exists = True
            try:
                with open(caption_path, "r", encoding="utf-8") as f:
                    preview.caption_content = json.load(f)
                    preview.platform = preview.caption_content.get("platform", "unknown")
            except: pass

        # 加载渲染日志
        render_log_path = os.path.join(pkg_dir, "render_log.json")
        if os.path.exists(render_log_path):
            preview.render_log_exists = True
            try:
                with open(render_log_path, "r", encoding="utf-8") as f:
                    preview.render_log_content = json.load(f)
                    preview.mock_mode = preview.render_log_content.get("mock_mode", True)
            except: pass

        return preview

    def get_audit_detail(self, audit_id: str) -> Optional[AuditDetail]:
        """获取具体的发布审计记录"""
        file_path = os.path.join(ProjectPaths.AUDIT, f"{audit_id}.json")
        if not os.path.exists(file_path):
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            return AuditDetail(
                audit_id=audit_id,
                plan_id=data.get("plan_id"),
                platform=data.get("platform", "unknown"),
                account_id=data.get("account_id", "unknown"),
                status=data.get("status", "success"),
                mode=data.get("mode", "mock"),
                driver_name=data.get("driver_name"),
                error=data.get("error"),
                receipt=data.get("receipt"),
                created_at=self._parse_datetime(data.get("timestamp", data.get("created_at")))
            )
        except Exception as e:
            logger.error(f"Error reading audit {audit_id}: {e}")
            return None
