import os
import logging
import json
from datetime import datetime
from typing import Any, Optional
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile
from app.media.blueprint import BlueprintAssembler
from app.media.engine_canvas import CanvasEngine
from app.media.ai_image_engine import AIImageEngine
from app.media.template_registry import TemplateRegistry
from app.media.models import MediaPackage, RenderAudit
from app.media.render_strategy import RenderStrategy
from app.publish.caption import CaptionSchema
from app.core.paths import ProjectPaths

logger = logging.getLogger("MediaOrchestrator")

class MediaOrchestrator:
    """
    (V5.2) 媒体资产编排器：支持 Canvas 模板与 AI 生图双引擎。
    """
    def __init__(self, asset_root: str = None, mock_mode: bool = False):
        self.asset_root = asset_root or str(ProjectPaths.ASSETS)
        self.mock_mode = mock_mode
        self.strategy = RenderStrategy()
        
        # 引擎初始化
        self.canvas_engine = CanvasEngine(mock_mode=self.mock_mode)
        self.ai_engine = AIImageEngine(mock_mode=self.mock_mode)
        
        self.assembler = BlueprintAssembler()
        self.registry = TemplateRegistry()

    def create_package(self, plan: PostPlan, persona: Persona, brand: BrandProfile, platform: str = "xhs") -> MediaPackage:
        logger.info(f"🎨 Orchestrating media for PostPlan: {plan.id} | Platform: {platform}")
        
        # 1. 决定渲染引擎
        engine_type = self.strategy.decide_engine(plan)
        
        # 2. 准备输出目录
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        package_id = f"pkg_{plan.id}_{timestamp}"
        asset_dir = os.path.join(self.asset_root, plan.id, timestamp)
        os.makedirs(asset_dir, exist_ok=True)
        
        # 3. 执行渲染逻辑
        image_path = ""
        prompt_path = None
        success = False
        audit_meta = {}

        if engine_type == "ai_image":
            res = self.ai_engine.render(plan, persona, brand, asset_dir)
            success = res["success"]
            image_path = res["image_path"]
            prompt_path = res["prompt_path"]
            # 记录完整 Prompt 数据以便审计 (FIXED)
            audit_meta = {
                "image_model": res.get("model"), 
                "prompt_summary": res.get("prompt_summary"),
                "full_prompt_info": res.get("prompt_data") # 需确保 AIImageEngine 返回全量数据
            }
        else:
            blueprint = self.assembler.assemble(plan, persona, brand)
            image_path = os.path.join(asset_dir, "render_01.jpg")
            template_path = self.registry.get_template_path(blueprint.archetype)
            success = self.canvas_engine.render_html(
                template_path=template_path,
                data=blueprint.data,
                output_path=image_path
            )
            audit_meta = {"archetype": blueprint.archetype, "theme": blueprint.theme, "blueprint_data": blueprint.data}

        # 4. 封装结果
        package = MediaPackage(
            id=package_id,
            post_plan_id=plan.id,
            platform=platform,
            media_engine=engine_type,
            asset_dir=asset_dir,
            archetype=audit_meta.get("archetype", "none"),
            theme=audit_meta.get("theme", "none"),
            images=[image_path] if success else [],
            prompt_path=prompt_path,
            status="ready" if success else "failed"
        )
        
        # 5. 写入辅助文件并审计
        self._save_aux_files(package, plan, audit_meta, success)
        
        return package

    def _save_aux_files(self, package: MediaPackage, plan: PostPlan, meta: dict, success: bool):
        # A. CaptionSchema 保持一致性
        # 如果是 AI 生图，从 meta 拿点信息也行，或者保持 plan 语义
        caption = CaptionSchema(
            platform=package.platform,
            title=plan.topic_seed,
            body=plan.story_context,
            hashtags=["personaOps", "AI", package.platform]
        )
        
        cap_path = os.path.join(package.asset_dir, "caption.json")
        with open(cap_path, "w", encoding="utf-8") as f:
            json.dump(caption.to_dict(), f, indent=2, ensure_ascii=False)
        package.caption_path = cap_path
        
        # B. 结构化审计
        audit = RenderAudit(
            plan_id=plan.id,
            render_engine=package.media_engine,
            image_model=meta.get("image_model"),
            archetype=meta.get("archetype"),
            theme=meta.get("theme"),
            asset_paths=package.images,
            caption_summary=f"{plan.topic_seed[:30]}...",
            prompt_summary=meta.get("prompt_summary"),
            prompt_path=package.prompt_path, # (FIXED) 记录 Prompt 物理路径
            media_status="success" if success else "failed",
            mock_mode=self.mock_mode,
            render_log={
                "meta": meta,
                "timestamp": datetime.now().isoformat()
            }
        )
        
        log_path = os.path.join(package.asset_dir, "render_log.json")
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(audit.__dict__, f, indent=2, ensure_ascii=False)
        package.render_log_path = log_path
