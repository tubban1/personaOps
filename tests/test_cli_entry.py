import unittest
from unittest.mock import patch, MagicMock
import sys
from main import main
from app.core.paths import ProjectPaths

class TestCLIEntry(unittest.TestCase):
    def setUp(self):
        ProjectPaths.ensure_dirs()
        self.persona = ProjectPaths.get_persona_path("lin_xiaotang.json")
        self.brand = ProjectPaths.get_brand_path("chuan_xing.json")
        self.channel = ProjectPaths.get_channel_path("xhs_main.json")

    @patch('main.PipelineRunner')
    def test_default_cli_run(self, mock_runner_cls):
        mock_runner = mock_runner_cls.return_value
        mock_runner.run.return_value = MagicMock(status="success", id="test_run")
        
        # 模拟命令行参数 python3 main.py
        with patch.object(sys, 'argv', ['main.py']):
            main()
            
        mock_runner.run.assert_called_once()
        args, kwargs = mock_runner.run.call_args
        self.assertEqual(kwargs['mode'], 'full')
        self.assertEqual(kwargs['persona_path'], self.persona)

    @patch('main.PipelineRunner')
    def test_mode_switch(self, mock_runner_cls):
        mock_runner = mock_runner_cls.return_value
        mock_runner.run.return_value = MagicMock(status="success", id="test_run")
        
        # 模拟命令行参数 python3 main.py --mode plan
        with patch.object(sys, 'argv', ['main.py', '--mode', 'plan']):
            main()
            
        mock_runner.run.assert_called_once()
        _, kwargs = mock_runner.run.call_args
        self.assertEqual(kwargs['mode'], 'plan')

    @patch('main.PipelineRunner')
    def test_overrides(self, mock_runner_cls):
        mock_runner = mock_runner_cls.return_value
        mock_runner.run.return_value = MagicMock(status="success", id="test_run")
        
        # 模拟命令行参数 python3 main.py --platform instagram --account test_acc
        with patch.object(sys, 'argv', ['main.py', '--platform', 'instagram', '--account', 'test_acc']):
            main()
            
        _, kwargs = mock_runner.run.call_args
        self.assertEqual(kwargs['platform'], 'instagram')
        self.assertEqual(kwargs['account'], 'test_acc')

if __name__ == "__main__":
    unittest.main()
