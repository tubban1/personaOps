from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RunHealth(str, Enum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    MISSING = "missing"
    CORRUPT = "corrupt"
    ORPHANED = "orphaned"

class RunStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    RUNNING = "running"
    PARTIAL = "partial"

class RunSummary(BaseModel):
    run_id: str
    status: RunStatus
    mode: str
    mock_mode: bool
    persona_id: Optional[str] = None
    brand_id: Optional[str] = None
    channel_id: Optional[str] = None
    platform: Optional[str] = None
    account_id: Optional[str] = None
    started_at: datetime
    finished_at: Optional[datetime] = None
    counts: Dict[str, int] = Field(default_factory=lambda: {"post_plans": 0, "media_packages": 0, "publish_audits": 0})
    health: RunHealth = RunHealth.COMPLETE

class RunTimelineItem(BaseModel):
    stage: str
    status: str
    timestamp: Optional[datetime] = None

class RunDetail(BaseModel):
    summary: RunSummary
    post_plans: List[str] = []
    media_packages: List[str] = []
    publish_audits: List[str] = []
    timeline: List[RunTimelineItem] = []
    warnings: List[str] = []
    errors: List[str] = []

class ImageAssetPreview(BaseModel):
    name: str
    url: str
    exists: bool

class AssetPreview(BaseModel):
    media_package_id: str
    post_plan_id: str
    platform: str
    asset_dir: str
    images: List[ImageAssetPreview] = []
    caption_exists: bool = False
    caption_content: Optional[Dict[str, Any]] = None
    render_log_exists: bool = False
    render_log_content: Optional[Dict[str, Any]] = None
    status: str = "ready"
    mock_mode: bool = True
    partial: bool = False

class AuditDetail(BaseModel):
    audit_id: str
    plan_id: Optional[str] = None
    platform: str
    account_id: str
    status: str
    mode: str
    driver_name: Optional[str] = None
    error: Optional[str] = None
    receipt: Optional[Dict[str, Any]] = None
    created_at: datetime

class DashboardHealth(BaseModel):
    status: str = "ok"
    storage_root: str
    counts: Dict[str, int]
    last_scan_at: datetime
