import logging
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile
from app.media.orchestrator import MediaOrchestrator
from app.media.models import MediaPackage
from app.core.paths import ProjectPaths

logger = logging.getLogger("MediaCoordinator")

class MediaCoordinator:
    """
    (Phase 5A) 媒体资产协调器：作为外部接入的单一入口。
    """
    def __init__(self, workspace: str = None, mock_mode: bool = False):
        # 使用 ProjectPaths 统一管理资产根目录 (V6.0 FIXED)
        asset_root = workspace or str(ProjectPaths.ASSETS)
        self.orchestrator = MediaOrchestrator(asset_root=asset_root, mock_mode=mock_mode)
        
    def prepare_assets(self, plan: PostPlan, persona: Persona, brand: BrandProfile, platform: str = "xhs") -> MediaPackage:
        logger.info(f"🏗️ Preparing media assets for plan {plan.id} on {platform}...")
        return self.orchestrator.create_package(plan, persona, brand, platform=platform)
