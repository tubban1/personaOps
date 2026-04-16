import logging
import uuid
from typing import Optional
from app.interaction.models import InteractionRecord, LeadMark, HandoffDecision
from app.interaction.policy import InteractionPolicy
from app.persona.models import Persona
from app.brand.models import BrandProfile

logger = logging.getLogger("InteractionBrain")

class InteractionBrain:
    """
    (V3.0) 核心大脑：负责分析用户意图、生成回复建议并做出接管决策。
    """
    def __init__(self):
        self.policy = InteractionPolicy()

    def process_interaction(self, record: InteractionRecord, persona: Persona, brand: BrandProfile) -> HandoffDecision:
        logger.info(f"🧠 Interaction Brain analyzing: '{record.normalized_text}'")
        
        # 1. 意图识别 (模拟 LLM)
        self._analyze_intent(record)
        
        # 2. 政策评估
        requires_human, risk_level, reason = self.policy.evaluate(record)
        record.requires_human = requires_human
        record.risk_level = risk_level
        
        # 3. 生成回复建议 (模拟基于 Persona 的 Prompt 生成)
        if risk_level != "critical":
            record.suggested_reply = self._generate_suggested_reply(record, persona, brand)
        
        # 4. 生成线索标记
        lead_mark = self._generate_lead_mark(record, persona, brand) if record.intent_primary in ["tour_inquiry", "pricing"] else None
        
        # 5. 生成最后决策记录
        decision = HandoffDecision(
            id=f"dec_{uuid.uuid4().hex[:8]}",
            interaction_id=record.id,
            decision="human_review" if requires_human else "auto_suggest",
            reason=reason,
            risk_tags=[risk_level] if risk_level != "low" else [],
            suggested_action="transfer_to_sales" if lead_mark else "approve_reply"
        )
        
        logger.info(f"✅ Decision made: {decision.decision} | Intent: {record.intent_primary}")
        return decision, lead_mark

    def _analyze_intent(self, record: InteractionRecord):
        text = record.normalized_text
        if any(w in text for w in ["好看", "棒", "支持", "绝了"]):
            record.intent_primary = "praise"
            record.intent_confidence = 0.95
        elif any(w in text for w in ["多少钱", "价格", "贵吗"]):
            record.intent_primary = "pricing"
            record.intent_confidence = 0.88
        elif any(w in text for w in ["路线", "哪里", "攻略"]):
            record.intent_primary = "tour_inquiry"
            record.intent_confidence = 0.85
        elif any(w in text for w in ["骗", "假", "投诉", "差评"]):
            record.intent_primary = "complaint"
            record.intent_confidence = 0.90
        else:
            record.intent_primary = "general"
            record.intent_confidence = 0.50

    def _generate_suggested_reply(self, record: InteractionRecord, persona: Persona, brand: BrandProfile) -> str:
        intent = record.intent_primary
        if intent == "praise":
            return f"{persona.name}: 嘿嘿，谢谢支持呀！我也觉得今天的成都特别美~"
        elif intent in ["pricing", "tour_inquiry"]:
            # 这种通常需要更专业的回复，或者是引导私信，AI 不敢乱回答具体价格
            return f"{persona.name}: 哎呀，具体的行程安排和价格我怕记混了不敢随便说，你私信我或者我让专业的同事来给你详细讲讲？"
        elif intent == "complaint":
            return f"{persona.name}: 真的很抱歉让你有这种感觉，我马上反馈给客服同事核实，请等我们一下下！"
        return f"{persona.name}: 收到！"

    def _generate_lead_mark(self, record: InteractionRecord, persona: Persona, brand: BrandProfile) -> Optional[LeadMark]:
        return LeadMark(
            id=f"lm_{uuid.uuid4().hex[:8]}",
            external_user_id=record.external_user_id,
            persona_id=persona.id,
            brand_id=brand.id,
            channel_id=record.account_id,
            lead_type=record.intent_primary,
            intent_score=record.intent_confidence,
            urgency_score=0.8 if record.intent_primary == "pricing" else 0.5,
            notes=f"User inquired about: {record.normalized_text}"
        )
