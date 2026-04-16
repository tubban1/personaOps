from typing import Dict, Any
from app.interaction.models import InteractionRecord
import uuid

class InteractionNormalizer:
    """
    负责将各平台的原始数据格式化为系统的统一 InteractionRecord。
    """
    def normalize_request(self, raw_data: Dict[str, Any]) -> InteractionRecord:
        # 这里模拟解析不同平台的结构
        platform = raw_data.get("platform", "unknown")
        
        normalized = InteractionRecord(
            id=f"int_{uuid.uuid4().hex[:8]}",
            platform=platform,
            account_id=raw_data.get("account_id", ""),
            post_id=raw_data.get("post_id", ""),
            source_type=raw_data.get("source_type", "comment"),
            raw_text=raw_data.get("raw_text", ""),
            normalized_text=raw_data.get("raw_text", "").strip(),
            external_user_id=raw_data.get("external_user_id", "anonymous"),
            language=raw_data.get("language", "zh-CN")
        )
        
        return normalized
