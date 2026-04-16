from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class InteractionRecord:
    """
    互动记录：标准化捕获单次评论或私信。
    """
    id: str
    platform: str
    account_id: str
    post_id: str
    source_type: str  # comment, dm, mention
    raw_text: str
    normalized_text: str = ""
    language: str = "zh-CN"
    external_user_id: str = "unknown"
    
    # Brain Analysis
    intent_primary: Optional[str] = None
    intent_confidence: float = 0.0
    risk_level: str = "low"  # low, medium, high, critical
    requires_human: bool = False
    
    # Suggestions
    suggested_reply: str = ""
    reply_style: str = "persona_default"
    
    # Lifecycle
    status: str = "new"  # new, reviewed, replied, escalated, blocked
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    processed_at: Optional[str] = None

@dataclass
class LeadMark:
    """
    线索标记：高意向用户画像。
    """
    id: str
    external_user_id: str
    persona_id: str
    brand_id: str
    channel_id: str
    lead_type: str = "general"  # tour_inquiry, pricing, booking_intent, collab, etc.
    intent_score: float = 0.0
    urgency_score: float = 0.0
    notes: str = ""
    last_interaction_id: str = ""
    owner: str = "ai_persona"
    status: str = "new"  # new, contacted, qualified, closed

@dataclass
class HandoffDecision:
    """
    人工接管决策记录。
    """
    id: str
    interaction_id: str
    decision: str  # auto_suggest, human_review, block
    reason: str
    risk_tags: List[str] = field(default_factory=list)
    suggested_action: str = ""
    review_status: str = "pending"
    decided_at: str = field(default_factory=lambda: datetime.now().isoformat())
