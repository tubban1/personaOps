import unittest
import os
import tempfile
from pathlib import Path
from app.media.coordinator import MediaCoordinator
from app.planning.models import PostPlan
from app.persona.models import Persona
from app.brand.models import BrandProfile
from app.core.paths import ProjectPaths

class TestMediaPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_data = ProjectPaths.DATA
        cls.test_dir = tempfile.TemporaryDirectory()
        ProjectPaths.rebase(cls.test_dir.name)
        ProjectPaths.ensure_dirs()

    @classmethod
    def tearDownClass(cls):
        ProjectPaths.rebase(cls.original_data)
        cls.test_dir.cleanup()

    def setUp(self):
        self.coordinator = MediaCoordinator(mock_mode=True)
        self.persona = Persona(id="p_test", name="Test Persona")
        self.brand = BrandProfile(id="b_test", name="Test Brand")
        
    def test_lifestyle_ai_image_path(self):
        plan = PostPlan(
            id="plan_lifestyle_test",
            channel_profile_id="ch_test",
            persona_id="p_test",
            brand_id="b_test",
            intent="lifestyle",
            story_context="Lifestyle sharing",
            content_goal="engagement",
            topic_seed="Lifestyle topic"
        )
        package = self.coordinator.prepare_assets(plan, self.persona, self.brand)
        self.assertEqual(package.status, "ready")
        self.assertEqual(package.media_engine, "ai_image")
        self.assertTrue(package.asset_dir.startswith(str(ProjectPaths.ASSETS)))
        self.assertTrue(os.path.exists(package.render_log_path))

    def test_business_template_path(self):
        plan = PostPlan(
            id="plan_business_test",
            channel_profile_id="ch_test",
            persona_id="p_test",
            brand_id="b_test",
            intent="business",
            story_context="Business sharing",
            content_goal="leads",
            topic_seed="Business topic"
        )
        package = self.coordinator.prepare_assets(plan, self.persona, self.brand)
        self.assertEqual(package.status, "ready")
        self.assertEqual(package.media_engine, "template")
        self.assertTrue(os.path.exists(package.asset_dir))

if __name__ == "__main__":
    unittest.main()
