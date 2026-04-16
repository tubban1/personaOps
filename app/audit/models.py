from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, List, Optional

@dataclass
class AuditRecord:
    """
    (V4.2) 审计记录模型。
    用于追踪执行层的渲染日志、发布回执。
    """
    id: str
    plan_id: str
    platform: str
    account_id: str
    execution_type: str = "publish" # render, publish, interaction
    status: str = "success"
    driver_name: str = ""
    mode: str = "real" # real, mock
    error: Optional[str] = None
    receipt: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
