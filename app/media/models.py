from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class MediaPackage:
    """
    媒体资产包：MediaCoordinator 的最终输出。
    作为 PublishRequest 的输入。
    """
    id: str
    post_plan_id: str
    platform: str
    asset_dir: str
    archetype: str = "none"
    theme: str = "none"
    images: List[str] = field(default_factory=list)
    caption_path: str = ""
    render_log_path: str = ""
    prompt_path: Optional[str] = None # (New in 5B) 生图 Prompt 路径
    media_engine: str = "template" # template, ai_image
    generation_mode: str = "normal" # normal, reference_based
    status: str = "ready" # ready, pending, failed
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class RenderAudit:
    """
    渲染审计：追踪从 Blueprint 到 Canvas 的每一个细节。
    """
    plan_id: str
    render_engine: str = "canvas" # canvas, ai_image
    image_model: Optional[str] = None # (New in 5B)
    archetype: Optional[str] = None
    theme: Optional[str] = None
    asset_paths: List[str] = field(default_factory=list)
    caption_summary: str = ""
    prompt_summary: Optional[str] = None # (New in 5B)
    prompt_path: Optional[str] = None # (New in 5B)
    coverage_score: float = 1.0 # 0.0 - 1.0
    media_status: str = "success"
    mock_mode: bool = False # (New in 5B)
    render_log: Dict[str, Any] = field(default_factory=dict)
    finished_at: str = field(default_factory=lambda: datetime.now().isoformat())
