from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class VisualAnchors:
    who: str
    age: str
    face_features: str
    hair_style: str
    clothing_preference: str
    vibe: str

class PortraitConsistency:
    """
    (V5.2) 人物视觉一致性管理器。
    维护人设的视觉锚点，确保不同场景下的图像特征稳定。
    """
    def get_anchors_for_persona(self, persona_id: str) -> VisualAnchors:
        # 在实际系统中，这应该从 Persona 模型的 PortraitPack 中读取
        # 此处模拟林小棠的视觉特征
        if "p_001" in persona_id: # 林小棠
            return VisualAnchors(
                who="A beautiful young Chinese travel blogger named Lin Xiaotang",
                age="early 20s",
                face_features="gentle eyes, natural smile, refined features",
                hair_style="long black straight hair with light highlights",
                clothing_preference="modern casual chic, outdoor travel outfits",
                vibe="authentic, friendly, energetic, close to nature"
            )
        return VisualAnchors(
            who="A professional person",
            age="30s",
            face_features="sharp look",
            hair_style="neat hair",
            clothing_preference="business suit",
            vibe="minimalist"
        )

    def build_anchor_prompt(self, anchors: VisualAnchors) -> str:
        return (
            f"{anchors.who}, aged {anchors.age}. "
            f"She has {anchors.face_features} and {anchors.hair_style}. "
            f"Wearing {anchors.clothing_preference}. "
            f"Overall vibe is {anchors.vibe}."
        )
