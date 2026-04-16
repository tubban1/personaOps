import logging
from app.planning.models import PostPlan

logger = logging.getLogger("RenderStrategy")

class RenderStrategy:
    """
    (V5.2) 渲染策略器。
    决定对给定的 PostPlan 使用何种渲染路径（模板 vs AI生图）。
    """
    def decide_engine(self, plan: PostPlan) -> str:
        # 简单启发式规则：
        # lifestyle 倾向于 AI 生图 (真实感)
        # business / conversion 倾向于 Template (信息密度)
        
        if plan.intent == "lifestyle":
            return "ai_image"
        
        # 默认使用模板渲染
        return "template"
