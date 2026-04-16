from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class PipelineRunRecord:
    """
    (V6.0) 管道运行全量记录。
    追踪一次完整任务周期的所有输出与中间产物。
    """
    id: str
    persona_id: str
    brand_id: str
    channel_id: str
    mode: str # plan, media, publish, full
    status: str = "pending" # pending, running, success, failed
    mock_mode: bool = True
    
    post_plan_ids: List[str] = field(default_factory=list)
    media_package_ids: List[str] = field(default_factory=list)
    publish_audit_ids: List[str] = field(default_factory=list)
    
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())
    finished_at: Optional[str] = None
    error: Optional[str] = None
    
    metadata: Dict[str, Any] = field(default_factory=dict)

    def complete(self, success: bool = True, error: str = None):
        self.status = "success" if success else "failed"
        self.error = error
        self.finished_at = datetime.now().isoformat()
