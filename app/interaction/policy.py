from typing import List, Tuple
from app.interaction.models import InteractionRecord

class InteractionPolicy:
    """
    负责执行硬性规则检查与风险判定。
    """
    
    # 关键词规则集
    TRIGGERS_HUMAN = ["多少钱", "价格", "报名", "私信我", "骗", "假", "投诉", "退款", "联系方式"]
    TRIGGERS_BLOCK = ["垃圾", "去死", "sb", "傻逼", "营销", "广告"] # 示例敏感词
    
    def evaluate(self, record: InteractionRecord) -> Tuple[bool, str, str]:
        """
        返回: (是否转人工, 风险等级, 理由)
        """
        text = record.normalized_text.lower()
        
        # 1. 阻断检查
        if any(w in text for w in self.TRIGGERS_BLOCK):
            return False, "critical", "blocked_word_detected"
        
        # 2. 人工接管检查
        if any(w in text for w in self.TRIGGERS_HUMAN):
            return True, "high", "business_intent_or_risk_detected"
            
        # 3. 情绪强度检查 (简单示例)
        if "!" in text or "！" in text:
            # 可能是激动或投诉，标记为中风险
            return False, "medium", "intense_punctuation"
            
        return False, "low", "normal_interaction"

    def apply_brand_guardrails(self, suggested_text: str) -> str:
        """
        最后一道防线：确保生成的回复没有越界。
        """
        # TODO: 这里可以加入更复杂的敏感词过滤或正则表达式检查
        return suggested_text
