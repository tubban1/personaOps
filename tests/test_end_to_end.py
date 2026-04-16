import unittest
import os
import json
import tempfile
import shutil
from pathlib import Path
from app.runtime.pipeline_runner import PipelineRunner
from app.core.paths import ProjectPaths

class TestEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 1. 保存原始路径，创建临时工作空间
        cls.original_data = ProjectPaths.DATA
        cls.test_dir = tempfile.TemporaryDirectory()
        ProjectPaths.rebase(cls.test_dir.name)
        ProjectPaths.ensure_dirs()
        
        # 2. 拷贝必要的测试实体到临时目录
        # 假设原始实体位于 ProjectPaths.ROOT / "data" / "entities"
        src_entities = cls.original_data / "entities"
        if os.path.exists(src_entities):
            shutil.copytree(src_entities, ProjectPaths.ENTITIES, dirs_exist_ok=True)
        else:
            # 备选：如果原始目录不存在，构造最小 Mock 实体供测试
            os.makedirs(ProjectPaths.PERSONAS, exist_ok=True)
            with open(ProjectPaths.get_persona_path("lin_xiaotang.json"), "w") as f:
                json.dump({"id": "p01", "name": "Test"}, f)
            os.makedirs(ProjectPaths.BRANDS, exist_ok=True)
            with open(ProjectPaths.get_brand_path("chuan_xing.json"), "w") as f:
                json.dump({"id": "b01", "name": "Test"}, f)
            os.makedirs(ProjectPaths.CHANNELS, exist_ok=True)
            with open(ProjectPaths.get_channel_path("xhs_main.json"), "w") as f:
                json.dump({"id": "c01", "account_id": "acc", "platform": "xhs"}, f)

    @classmethod
    def tearDownClass(cls):
        ProjectPaths.rebase(cls.original_data)
        cls.test_dir.cleanup()

    def setUp(self):
        self.runner = PipelineRunner(mock_mode=True)
        self.persona_path = ProjectPaths.get_persona_path("lin_xiaotang.json")
        self.brand_path = ProjectPaths.get_brand_path("chuan_xing.json")
        self.channel_path = ProjectPaths.get_channel_path("xhs_main.json")

    def test_full_pipeline_mock_run(self):
        """测试全链路 Mock 闭环：Planning -> Render -> Publish -> Audit (V6.1 Robust)"""
        record = self.runner.run(
            persona_path=self.persona_path,
            brand_path=self.brand_path,
            channel_path=self.channel_path,
            mode="full"
        )
        
        self.assertEqual(record.status, "success", f"Pipeline failed with error: {record.error}")
        self.assertTrue(len(record.post_plan_ids) > 0)
        self.assertTrue(len(record.media_package_ids) > 0)
        self.assertTrue(len(record.publish_audit_ids) > 0)
        
        # 检查 Run Audit 文件是否落盘 (使用 ProjectPaths.AUDIT 定位)
        audit_file_path = ProjectPaths.get_audit_path(f"run_{record.id}")
        # 注意 Runner 用的是 run_{id}，RuntimeManager 用的是 aud_{id}。
        # 这里验证的是 PipelineRunner 自身产生的 run_... 日志
        run_audit_path = ProjectPaths.AUDIT / f"run_{record.id}.json"
        self.assertTrue(os.path.exists(run_audit_path), f"Audit file not found at {run_audit_path}")

    def test_planning_only_mode(self):
        """测试仅规划模式"""
        record = self.runner.run(
            persona_path=self.persona_path,
            brand_path=self.brand_path,
            channel_path=self.channel_path,
            mode="plan"
        )
        self.assertEqual(record.status, "success")
        self.assertTrue(len(record.post_plan_ids) > 0)
        self.assertEqual(len(record.media_package_ids), 0)

if __name__ == "__main__":
    unittest.main()
