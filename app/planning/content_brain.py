import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from app.persona.models import Persona
from app.brand.models import BrandProfile, BrandBinding
from app.planning.models import PostPlan, WeeklyPlan, ContentPillar, ChannelProfile
from app.memory.models import Storyline, StoryBeat
from app.planning.pillar_engine import PillarEngine
from app.planning.story_engine import StoryEngine

logger = logging.getLogger("ContentBrain")

class ContentBrain:
    """
    (V2.0) 指挥中心：负责为一个角色生成连续发帖计划。
    从单条任务生成升级为“周计划”编排。
    """
    def __init__(self):
        self.pillar_engine = PillarEngine()
        self.story_engine = StoryEngine()

    def generate_weekly_plan(
        self, 
        persona: Persona, 
        brand: BrandProfile, 
        binding: BrandBinding, 
        channel: ChannelProfile,
        pillars: List[ContentPillar],
        storyline: Storyline,
        beats: List[StoryBeat]
    ) -> WeeklyPlan:
        """
        核心能力：生成未来 7 天的连续内容计划。
        """
        logger.info(f"🧠 Content Brain is thinking for Persona: {persona.name}...")
        
        plan_id = f"wp_{datetime.now().strftime('%Y%m%d')}_{persona.id}"
        week_start = datetime.now().strftime("%Y-%m-%d")
        
        weekly_plan = WeeklyPlan(
            id=plan_id,
            channel_profile_id=channel.id,
            week_start=week_start,
            goals=[brand.business_goal, storyline.goals[0] if storyline.goals else "engagement"]
        )
        
        # 模拟生成 7 天的 PostPlan
        generated_plans = []
        current_date = datetime.now()
        
        for i in range(1, 8):
            # 1. 选取内容支柱
            pillar = self.pillar_engine.pick_next_pillar(pillars)
            
            # 2. 注入剧情上下文
            context = self.story_engine.get_current_context(storyline, beats)
            
            # 3. 构造单日计划 (实际场景下这里会调用 LLM)
            post_id = f"plan_{plan_id}_{i:02d}"
            target_time = current_date + timedelta(days=i-1)
            
            # 这里的 topic 种子会根据 pillar 和 context 动态生成
            topic_seed = self._mock_topic_generation(pillar, storyline)
            
            plan = PostPlan(
                id=post_id,
                channel_profile_id=channel.id,
                persona_id=persona.id,
                brand_id=brand.id,
                intent=pillar.name,
                story_context=context,
                content_goal=f"Reach {pillar.name} target",
                topic_seed=topic_seed,
                pillar_id=pillar.id,
                scheduled_at=target_time.isoformat(),
                status="draft"
            )
            
            generated_plans.append(plan)
            weekly_plan.post_ids.append(post_id)
            
        logger.info(f"✅ Generated 7-day plan with {len(generated_plans)} posts.")
        return weekly_plan, generated_plans

    def _mock_topic_generation(self, pillar: ContentPillar, storyline: Storyline) -> str:
        """模拟根据支柱和剧情生成具体主题"""
        if pillar.name == "lifestyle":
            return f"{storyline.title} 期间的感性时刻"
        elif pillar.name == "professional":
            return f"关于 {storyline.title} 的专业深度解析"
        elif pillar.name == "conversion":
            return f"加入我们的 {storyline.title} 体验团，限时开启"
        return "日常分享"
