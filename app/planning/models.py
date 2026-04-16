from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime

@dataclass
class ChannelProfile:
    id: str
    binding_id: str
    platform: str  # xhs, instagram
    account_id: str
    content_style: str = "default"
    posting_frequency: str = "daily"
    format_preferences: List[str] = field(default_factory=lambda: ["image_text"])

    @classmethod
    def from_dict(cls, data: dict) -> 'ChannelProfile':
        import inspect
        params = inspect.signature(cls).parameters
        return cls(**{k: v for k, v in data.items() if k in params})

    @classmethod
    def load_from_file(cls, path: str) -> 'ChannelProfile':
        import json
        with open(path, "r", encoding="utf-8") as f:
            return cls.from_dict(json.load(f))

@dataclass
class ContentPillar:
    """
    内容支柱：定义 persona 在特定账号下的内容分布策略。
    """
    id: str
    binding_id: str
    name: str  # lifestyle, professional, business, conversion
    description: str
    weight: float  # 0.0 - 1.0
    allowed_formats: List[str] = field(default_factory=lambda: ["image_text"])

@dataclass
class WeeklyPlan:
    """
    周计划：为一个频道规划的 7 天内容序列。
    """
    id: str
    channel_profile_id: str
    week_start: str  # ISO date
    goals: List[str] = field(default_factory=list)
    post_ids: List[str] = field(default_factory=list)
    status: str = "proposed"  # proposed, approved, executing, completed
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class PostPlan:
    id: str
    channel_profile_id: str
    persona_id: str
    brand_id: str
    intent: str  # lifestyle, business, conversion
    story_context: str
    content_goal: str
    topic_seed: str
    pillar_id: Optional[str] = None # 关联的内容支柱
    status: str = "draft"  # draft, pending_delivery, delivered, published, failed
    delivery_payload: Optional[Dict] = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    scheduled_at: Optional[str] = None
