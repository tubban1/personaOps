from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile

@dataclass
class RenderBlueprint:
    """
    渲染蓝图：定义具体一次渲染的输入、模板与主题环境。
    """
    archetype: str
    theme: str
    data: Dict[str, Any]
    selector: str = ".visual-engine"
    viewport: Optional[Dict[str, int]] = None

class BlueprintAssembler:
    """
    负责将业务层的 PostPlan 组装为底层的渲染蓝图。
    """
    def assemble(self, plan: PostPlan, persona: Persona, brand: BrandProfile) -> RenderBlueprint:
        # 默认根据 intent 选择 archetype
        archetype = "card"
        if plan.intent == "lifestyle":
            archetype = "rough_note"
        elif plan.intent == "business":
            archetype = "structured_card"
            
        # 组装数据上下文
        render_data = {
            "title": plan.topic_seed,
            "content": plan.story_context,
            "author": persona.name,
            "brand": brand.name,
            "vibe": persona.tone_of_voice
        }
        
        return RenderBlueprint(
            archetype=archetype,
            theme="default",
            data=render_data
        )
