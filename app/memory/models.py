from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime

@dataclass
class MemorySnapshot:
    """
    记忆快照：角色在特定任务或周期后的认知沉淀。
    """
    id: str
    persona_id: str
    snapshot_type: str  # episodic (event), semantic (knowledge)
    summary: str
    raw_data_ref: str  # reference to task_id or interaction_id
    importance: int = 3 # 1-5
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class Storyline:
    """
    剧情线：指导跨时间周期的内容叙事。
    """
    id: str
    persona_id: str
    brand_id: str
    title: str
    current_stage: str
    goals: List[str] = field(default_factory=list)
    active: bool = True

@dataclass
class StoryBeat:
    """
    剧情节奏点：Storyline 中的原子事件或里程碑。
    """
    id: str
    storyline_id: str
    beat_type: str  # intro, tension, climax, resolution, casual
    summary: str
    emotion: str = "neutral"
    business_relevance: float = 0.1  # 0.0 - 1.0
    completed: bool = False
