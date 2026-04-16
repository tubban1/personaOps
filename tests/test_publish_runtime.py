import unittest
import os
import tempfile
from pathlib import Path
from app.runtime.manager import RuntimeManager
from app.publish.models import PublishRequest
from app.publish.caption import CaptionSchema
from app.core.paths import ProjectPaths

class TestPublishRuntime(unittest.TestCase):
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
        self.manager = RuntimeManager()
        self.caption = CaptionSchema(platform="xhs", title="Test Title", body="Test Body")

    def test_mock_xhs_publish(self):
        request = PublishRequest(
            account_id="xhs_test",
            platform="xhs",
            images=["test.jpg"],
            caption=self.caption,
            post_plan_id="plan_p_1",
            mock_mode=True
        )
        result = self.manager.submit_publish(request)
        self.assertTrue(result.success)
        self.assertIsNotNone(result.audit_id)
        # 验证审计文件是否根据 ProjectPaths 正确落盘
        audit_path = ProjectPaths.get_audit_path(result.audit_id)
        self.assertTrue(os.path.exists(audit_path), f"Audit not found at: {audit_path}")

    def test_mock_instagram_publish(self):
        request = PublishRequest(
            account_id="insta_test",
            platform="instagram",
            images=["test.jpg"],
            caption=self.caption,
            post_plan_id="plan_p_1",
            mock_mode=True
        )
        result = self.manager.submit_publish(request)
        self.assertTrue(result.success)

if __name__ == "__main__":
    unittest.main()
