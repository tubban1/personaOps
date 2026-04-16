import json
from dataclasses import dataclass
from typing import Optional, List, Any, Dict, Tuple
from abc import ABC, abstractmethod
from pathlib import Path

from app.publish.caption import CaptionSchema

@dataclass(frozen=True)
class PlatformPolicy:
    """
    (Migrated) 平台政策：定义发布限制与文案裁剪规则。
    """
    key: str
    display_name: str
    title_max_chars: Optional[int] = None
    body_max_chars: Optional[int] = None
    caption_max_chars: Optional[int] = None
    max_images: int = 9
    hashtag_count: int = 5

    @classmethod
    def from_dict(cls, key: str, payload: dict) -> "PlatformPolicy":
        return cls(
            key=key,
            display_name=payload.get("display_name", key),
            title_max_chars=payload.get("title_max_chars"),
            body_max_chars=payload.get("body_max_chars"),
            caption_max_chars=payload.get("caption_max_chars"),
            max_images=payload.get("max_images", 9),
            hashtag_count=payload.get("hashtag_count", 5),
        )

    def clip_text(self, text: str, max_chars: Optional[int]) -> str:
        if not text: return ""
        text = text.strip()
        if max_chars:
            return text[:max_chars].strip()
        return text

class BaseDriver(ABC):
    """
    (Migrated & Refactored) 发布驱动基类。
    不再持有 Task 对象，而是由具体的发布参数驱动。
    """
    
    @abstractmethod
    def login(self, auth_data: Dict[str, Any]) -> bool:
        """验证或执行登录"""
        pass

    @abstractmethod
    def publish(self, images: List[str], caption: CaptionSchema, **kwargs) -> Dict[str, Any]:
        """
        执行发布。
        :return: {"success": bool, "post_id": str, "receipt": dict}
        """
        pass

    def get_policy(self, platform_key: str) -> PlatformPolicy:
        """获取平台规则"""
        # (V4.0) 基于模块文件位置的绝对路径解析
        base_dir = Path(__file__).resolve().parent
        config_path = base_dir / "platforms" / platform_key / "constraints.json"
        
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                return PlatformPolicy.from_dict(platform_key, json.load(f))
        return PlatformPolicy(key=platform_key, display_name=platform_key)
