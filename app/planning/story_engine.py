from typing import List, Optional
from app.memory.models import Storyline, StoryBeat

class StoryEngine:
    """
    负责维护角色的叙事连续性。
    """
    def get_current_context(self, storyline: Storyline, beats: List[StoryBeat]) -> str:
        """
        获取当前剧情的上下文描述，用于下发给 LLM 规划内容。
        """
        active_beats = [b for b in beats if b.storyline_id == storyline.id and not b.completed]
        if not active_beats:
            return f"当前处于剧情线 [{storyline.title}] 的 {storyline.current_stage} 阶段。"
        
        current_beat = active_beats[0]
        return (
            f"剧情线: {storyline.title}. "
            f"当前阶段: {storyline.current_stage}. "
            f"当前关键点: {current_beat.summary} (调性: {current_beat.emotion})."
        )

    def progress_story(self, storyline: Storyline, beats: List[StoryBeat]):
        """标记当前节奏点已完成"""
        for b in beats:
            if b.storyline_id == storyline.id and not b.completed:
                b.completed = True
                break
