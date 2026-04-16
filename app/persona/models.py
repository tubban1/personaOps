from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Persona:
    id: str
    name: str
    display_name: str = ""
    identity_summary: str = ""
    tone_of_voice: str = "Neutral"
    personality_traits: List[str] = field(default_factory=list)
    taboos: List[str] = field(default_factory=list)
    age_range: str = "20-25"
    gender_presentation: str = "neutral"
    occupation: str = "Independent Creator"
    visual_profile_id: Optional[str] = None
    status: str = "active"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    @classmethod
    def from_dict(cls, data: dict) -> 'Persona':
        # 过滤掉不在 dataclass 字段中的 key
        import inspect
        fields = inspect.signature(cls).parameters
        filtered_data = {k: v for k, v in data.items() if k in fields}
        return cls(**filtered_data)

    @classmethod
    def load_from_file(cls, path: str) -> 'Persona':
        import json
        with open(path, "r", encoding="utf-8") as f:
            return cls.from_dict(json.load(f))

@dataclass
class PortraitPack:
    id: str
    persona_id: str
    avatar_images: List[str]
    reference_images: List[str] = field(default_factory=list)
    style_keywords: List[str] = field(default_factory=list)
    face_consistency_notes: str = ""
    body_notes: str = ""
    outfit_rules: List[str] = field(default_factory=list)
    scene_preferences: List[str] = field(default_factory=list)
