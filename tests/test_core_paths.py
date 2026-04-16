import unittest
import os
import tempfile
import shutil
from pathlib import Path
from app.core.paths import ProjectPaths

class TestProjectPaths(unittest.TestCase):
    def setUp(self):
        self.original_data = ProjectPaths.DATA

    def tearDown(self):
        ProjectPaths.rebase(self.original_data)

    def test_root_detection(self):
        root = ProjectPaths.ROOT
        self.assertTrue(os.path.exists(root))
        self.assertTrue(os.path.isdir(root))

    def test_rebase(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            ProjectPaths.rebase(tmp_dir)
            self.assertEqual(str(ProjectPaths.DATA), str(Path(tmp_dir).resolve()))
            self.assertEqual(str(ProjectPaths.AUDIT), str(Path(tmp_dir).resolve() / "audit"))
            
            ProjectPaths.ensure_dirs()
            self.assertTrue(os.path.exists(ProjectPaths.AUDIT))

    def test_get_path_helpers(self):
        p = ProjectPaths.get_persona_path("test.json")
        self.assertIn("data/entities/personas/test.json", p)

if __name__ == "__main__":
    unittest.main()
