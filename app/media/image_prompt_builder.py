import logging
from typing import Dict, Any
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile
from app.media.portrait_consistency import PortraitConsistency, VisualAnchors

logger = logging.getLogger("ImagePromptBuilder")

class ImagePromptBuilder:
    """
    (V5.2) 图像提示词构建器。
    综合人设、品牌、计划和叙事上下文，生成结构化的 AI 提示词。
    """
    def __init__(self):
        self.consistency = PortraitConsistency()

    def build_prompt(self, plan: PostPlan, persona: Persona, brand: BrandProfile) -> Dict[str, str]:
        # 1. 获取人物视觉锚点
        anchors = self.consistency.get_anchors_for_persona(persona.id)
        anchor_text = self.consistency.build_anchor_prompt(anchors)
        
        # 2. 解析场景与动作 (从 Plan 提取)
        scene = plan.topic_seed
        context = plan.story_context
        
        # 3. 组装最终 Prompt (who + where + doing what + style)
        full_prompt = (
            f"{anchor_text}. "
            f"Scene: {scene}. "
            f"Context: {context}. "
            f"Visual Style: high-quality photography, cinematic lighting, 8k resolution, realistic textures, "
            f"warm natural colors, shallow depth of field. "
            f"Brand Vibe: {brand.business_goal} oriented but {persona.tone_of_voice} style."
        )
        
        negative_prompt = "cartoon, anime, 3d render, distorted face, extra limbs, low quality, blurry, text, watermark, bad anatomy"
        
        return {
            "prompt": full_prompt,
            "negative_prompt": negative_prompt,
            "anchors_used": str(anchors)
        }
