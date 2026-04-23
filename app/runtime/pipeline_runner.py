import logging
import json
import os
from datetime import datetime
from typing import List, Optional
from app.persona.models import Persona
from app.brand.models import BrandProfile, BrandBinding
from app.planning.models import PostPlan, ChannelProfile, ContentPillar
from app.planning.content_brain import ContentBrain
from app.memory.models import Storyline, StoryBeat
from app.media.coordinator import MediaCoordinator
from app.runtime.manager import RuntimeManager
from app.runtime.models import PipelineRunRecord
from app.publish.models import PublishRequest
from app.publish.caption import CaptionSchema
from app.core.paths import ProjectPaths

logger = logging.getLogger("PipelineRunner")

class PipelineRunner:
    """
    (V6.0) 核心管道执行器：解耦主逻辑与 CLI 界面。
    职责：负责从实体加载到资产生成、发布的全量任务调度。
    """
    def __init__(self, mock_mode: bool = True):
        self.mock_mode = mock_mode
        self.media_coord = MediaCoordinator(mock_mode=mock_mode)
        self.runtime = RuntimeManager()
        self.brain = ContentBrain()
        ProjectPaths.ensure_dirs()

    def run(self, persona_path: str, brand_path: str, channel_path: str, 
            mode: str = "full", platform: str = None, account: str = None,
            plan_id: str = None, package_path: str = None) -> PipelineRunRecord:
        
        run_id = f"run_p_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        logger.info(f"🚀 Running Pipeline [{run_id}] Mode: {mode.upper()} (Mock: {self.mock_mode})")

        # 1. 资源准备
        try:
            persona = Persona.load_from_file(persona_path)
            brand = BrandProfile.load_from_file(brand_path)
            channel = ChannelProfile.load_from_file(channel_path)
            
            if platform: channel.platform = platform
            if account: channel.account_id = account
            
            record = PipelineRunRecord(
                id=run_id, persona_id=persona.id, brand_id=brand.id,
                channel_id=channel.id, platform=channel.platform, 
                account_id=channel.account_id, mode=mode, 
                mock_mode=self.mock_mode, status="running"
            )
        except Exception as e:
            logger.error(f"Initialization Error: {e}")
            return PipelineRunRecord(id=run_id, persona_id="error", brand_id="error", channel_id="error", platform="error", account_id="error", mode=mode, status="failed", error=str(e))

        # 2. 逻辑执行 (V6.1: 真正可独立运行的 Mode)
        try:
            plans = []
            package = None

            # A. Planning 段
            if mode in ["full", "plan"]:
                logger.info("🧠 Brain is planning...")
                binding = BrandBinding(id="bind_001", persona_id=persona.id, brand_id=brand.id)
                pillars = [
                    ContentPillar(id="pill_l", binding_id=binding.id, name="lifestyle", weight=0.6, description="Lifestyle sharing"),
                    ContentPillar(id="pill_b", binding_id=binding.id, name="business", weight=0.4, description="Business value")
                ]
                storyline = Storyline(id="story_001", persona_id=persona.id, brand_id=brand.id, title="成都探索日记", current_stage="intro", goals=["engagement"])
                beats = [StoryBeat(id="beat_01", storyline_id=storyline.id, beat_type="casual", summary="初抵成都")]
                
                _, plans = self.brain.generate_weekly_plan(persona, brand, binding, channel, pillars, storyline, beats)
            elif mode == "media" and plan_id:
                # 如果是 media 模式，且给了 plan_id，尝试从库中寻找或恢复 plan (此处简化为模拟加载)
                logger.info(f"💾 Attempting to load plan: {plan_id}")
                plans = [
                    PostPlan(
                        id=plan_id, 
                        persona_id=persona.id, 
                        brand_id=brand.id, 
                        channel_profile_id=channel.id, 
                        intent="lifestyle", 
                        story_context="Restored from CLI", 
                        content_goal="engagement", 
                        topic_seed="Restored Plan"
                    )
                ]
            
            for p in plans: record.post_plan_ids.append(p.id)
            current_plan = plans[0] if plans else None

            # B. Media Generation 段
            if mode in ["full", "media"] and current_plan:
                logger.info(f"📸 Generating assets for {current_plan.id}...")
                package = self.media_coord.prepare_assets(current_plan, persona, brand, platform=channel.platform)
                record.media_package_ids.append(package.id)
            elif mode == "publish" and package_path:
                logger.info(f"📥 Loading existing package from: {package_path}")
                # 从路径加载 package 审计信息 (简化逻辑)
                log_f = os.path.join(package_path, "render_log.json")
                if os.path.exists(log_f):
                    with open(log_f, "r", encoding="utf-8") as f:
                        audit_data = json.load(f)
                        record.media_package_ids.append(audit_data.get("id", "legacy_pkg"))
                        # 构造最小 package 对象以供发布
                        from app.media.models import MediaPackage
                        package = MediaPackage(
                            id=audit_data.get("id", "legacy_pkg"),
                            post_plan_id=audit_data.get("plan_id"),
                            platform=channel.platform,
                            media_engine=audit_data.get("render_engine"),
                            asset_dir=package_path,
                            images=audit_data.get("asset_paths", []),
                            caption_path=os.path.join(package_path, "caption.json"),
                            status="ready"
                        )
                else:
                    raise FileNotFoundError(f"render_log.json not found in {package_path}")

            # C. Publishing 段
            if mode in ["full", "publish"] and package:
                logger.info(f"📡 Dispatching to runtime: {channel.platform}@{channel.account_id}")
                if not os.path.exists(package.caption_path):
                    raise FileNotFoundError(f"Caption file missing: {package.caption_path}")
                
                with open(package.caption_path, "r", encoding="utf-8") as f:
                    cap_dict = json.load(f)
                
                request = PublishRequest(
                    account_id=channel.account_id, platform=channel.platform,
                    images=package.images, caption=CaptionSchema.from_dict(cap_dict),
                    post_plan_id=package.post_plan_id or (current_plan.id if current_plan else "unplanned"),
                    mock_mode=self.mock_mode
                )
                pub_result = self.runtime.submit_publish(request)
                if pub_result.success: record.publish_audit_ids.append(pub_result.audit_id)
            elif mode != "plan" and not package:
                logger.warning(f"⏩ Execution chain interrupted in {mode} mode: No package/plan resolved.")

            record.complete(success=True)
            self._save_run_record(record)
            logger.info(f"🏁 Run [{run_id}] completed successfully.")
            return record

        except Exception as e:
            logger.error(f"Runtime Exception: {e}")
            record.complete(success=False, error=str(e))
            self._save_run_record(record)
            return record

    def _save_run_record(self, record: PipelineRunRecord):
        p = ProjectPaths.AUDIT / f"run_{record.id}.json"
        with open(p, "w", encoding="utf-8") as f:
            json.dump(record.__dict__, f, indent=2, ensure_ascii=False)
        logger.info(f"📊 Run Audit saved: {p}")
