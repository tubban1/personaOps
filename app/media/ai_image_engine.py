import os
import logging
import json
from datetime import datetime
from app.media.image_client import ImageClient
from app.media.image_prompt_builder import ImagePromptBuilder
from app.media.models import MediaPackage, RenderAudit
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile

logger = logging.getLogger("AIImageEngine")

class AIImageEngine:
    """
    (V5.2) AI 图像生成引擎。
    执行提示词构建、API 调用与资产保存。
    """
    def __init__(self, mock_mode: bool = False):
        self.mock_mode = mock_mode
        self._client = None # 延后初始化
        self.prompt_builder = ImagePromptBuilder()

    @property
    def client(self) -> ImageClient:
        if self._client is None:
            from app.media.image_client import ImageClient
            self._client = ImageClient()
        return self._client

    def render(self, plan: PostPlan, persona: Persona, brand: BrandProfile, asset_dir: str) -> dict:
        logger.info(f"🤖 AI Image Engine rendering for {plan.id}...")
        
        # 1. 构建 Prompt
        prompt_data = self.prompt_builder.build_prompt(plan, persona, brand)
        
        # 2. 导出 Prompt 记录
        prompt_path = os.path.join(asset_dir, "prompt.json")
        with open(prompt_path, "w", encoding="utf-8") as f:
            json.dump(prompt_data, f, indent=2, ensure_ascii=False)
            
        # 3. 执行生成
        image_path = os.path.join(asset_dir, "render_01.jpg")
        
        if self.mock_mode:
            logger.info("🌵 [MockAI] Simulating AI image generation.")
            # 使用简单的哑文件
            with open(image_path, "wb") as f:
                f.write(b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xFF\xDB\x00C\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xFF\xC0\x00\x09\x08\x00\x01\x00\x01\x01\x01\x00\xFF\xDA\x00\x08\x01\x01\x00\x00\x3F\x00\xD2\xCF\x20\xFF\xD9")
            success = True
        else:
            success = self.client.generate_image(prompt_data["prompt"], image_path)
            
        return {
            "success": success,
            "image_path": image_path,
            "prompt_path": prompt_path,
            "prompt_data": prompt_data,
            "prompt_summary": prompt_data["prompt"][:100],
            "model": self.client.config.image_model if not self.mock_mode else "mock-model"
        }
