import random
from typing import List, Dict
from app.planning.models import ContentPillar

class PillarEngine:
    """
    负责基于权重分配内容支柱。
    """
    def pick_next_pillar(self, pillars: List[ContentPillar]) -> ContentPillar:
        if not pillars:
            # 默认保底
            return ContentPillar(id="default", binding_id="", name="daily_life", description="", weight=1.0)
        
        # 加权随机选择
        total_weight = sum(p.weight for p in pillars)
        r = random.uniform(0, total_weight)
        upto = 0
        for p in pillars:
            if upto + p.weight >= r:
                return p
            upto += p.weight
        return pillars[0]
