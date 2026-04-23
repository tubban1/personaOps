from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime

from app.dashboard.service import DashboardService
from app.dashboard.models import RunSummary, RunDetail, AssetPreview, AuditDetail, DashboardHealth
from app.core.paths import ProjectPaths
import os

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])
service = DashboardService()

@router.get("/runs", response_model=List[RunSummary])
async def get_runs(limit: int = Query(50, ge=1, le=100)):
    """获取运行记录列表"""
    return service.list_runs(limit=limit)

@router.get("/runs/{run_id}", response_model=RunDetail)
async def get_run_detail(run_id: str):
    """获取单次运行详情"""
    detail = service.get_run_detail(run_id)
    if not detail:
        raise HTTPException(status_code=404, detail=f"Run {run_id} not found")
    return detail

@router.get("/assets/{plan_id}/{media_package_id}", response_model=AssetPreview)
async def get_asset_preview(plan_id: str, media_package_id: str):
    """查看资产包详情（预览图、文案、渲染日志）"""
    preview = service.get_asset_preview(media_package_id=media_package_id, plan_id=plan_id)
    if not preview:
        raise HTTPException(status_code=404, detail="Asset package not found")
    return preview

@router.get("/audits/{audit_id}", response_model=AuditDetail)
async def get_audit_detail(audit_id: str):
    """查看发布审计详情"""
    detail = service.get_audit_detail(audit_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Audit record not found")
    return detail

@router.get("/health", response_model=DashboardHealth)
async def get_health():
    """仪表盘服务端健康检查"""
    # 基础统计逻辑
    runs_count = len([f for f in os.listdir(ProjectPaths.AUDIT) if f.startswith("run_")])
    audits_count = len([f for f in os.listdir(ProjectPaths.AUDIT) if f.startswith("aud_")])
    
    return DashboardHealth(
        storage_root=ProjectPaths.DATA,
        counts={
            "runs": runs_count,
            "audits": audits_count
        },
        last_scan_at=datetime.now()
    )
