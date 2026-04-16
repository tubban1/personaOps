from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.publish.caption import CaptionSchema

@dataclass
class PublishAccount:
    """
    统一发布账号模型。
    """
    id: str
    platform: str
    account_id: str
    display_name: str = ""
    auth_state_path: str = ""
    status: str = "active"  # active, expired, pending_login
    last_verified_at: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)

@dataclass
class PublishRequest:
    """
    统一发布请求对象。
    """
    account_id: str
    platform: str
    images: List[str]
    caption: CaptionSchema
    post_plan_id: Optional[str] = None
    persona_id: Optional[str] = None
    brand_id: Optional[str] = None
    dry_run: bool = False
    mock_mode: bool = False

@dataclass
class PublishResult:
    """
    统一发布结果对象。
    """
    success: bool
    platform: str
    account_id: str
    post_id: Optional[str] = None
    receipt: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    audit_id: Optional[str] = None
    finished_at: str = field(default_factory=lambda: datetime.now().isoformat())
