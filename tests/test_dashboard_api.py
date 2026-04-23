import os
import json
import pytest
import tempfile
import shutil
from fastapi.testclient import TestClient
from datetime import datetime

from app.core.paths import ProjectPaths
from dashboard_main import create_app
from app.dashboard.service import DashboardService
from app.dashboard.models import RunHealth, RunStatus

@pytest.fixture
def temp_workspace():
    # Setup
    old_root = ProjectPaths.DATA
    tmp_dir = tempfile.mkdtemp()
    ProjectPaths.rebase(tmp_dir)
    ProjectPaths.ensure_dirs()
    
    yield tmp_dir
    
    # Teardown
    ProjectPaths.rebase(old_root)
    shutil.rmtree(tmp_dir)

@pytest.fixture
def client(temp_workspace):
    # 使用 factory 创建 app，确保 static mount 绑定到当前的 temp_workspace
    app = create_app()
    return TestClient(app)

def test_list_runs_discovery_all_naming(temp_workspace, client):
    # Test discovery of runs with different naming (run_ ID vs plain ID)
    audit_dir = ProjectPaths.AUDIT
    
    # 1. Standard prefix
    with open(os.path.join(audit_dir, "run_p_001.json"), "w") as f:
        json.dump({"id": "p_001", "started_at": datetime.now().isoformat()}, f)
    
    # 2. Plain ID (no run_ prefix)
    with open(os.path.join(audit_dir, "p_002.json"), "w") as f:
        json.dump({"id": "p_002", "started_at": datetime.now().isoformat()}, f)
        
    # 3. Should EXCLUDE audit files (aud_*)
    with open(os.path.join(audit_dir, "aud_001.json"), "w") as f:
        json.dump({"audit_id": "aud_001"}, f)

    response = client.get("/api/dashboard/runs")
    data = response.json()
    assert len(data) == 2 # Only p_001 and p_002
    ids = [r["run_id"] for r in data]
    assert "p_001" in ids
    assert "p_002" in ids

def test_semantic_health_full_failed_publish(temp_workspace, client):
    # Scenario: Mode full, but no publish_audit_ids (common failure)
    run_id = "run_fail"
    audit_dir = ProjectPaths.AUDIT
    
    run_data = {
        "id": run_id,
        "mode": "full",
        "status": "success", # Maybe it claimed success but broke in the middle
        "media_package_ids": ["pkg_1"],
        "publish_audit_ids": [], # Semantic Gap!
        "post_plan_ids": ["plan_1"],
        "started_at": datetime.now().isoformat()
    }
    
    # Make media package exist so it's not a physical missing error but a semantic one
    os.makedirs(os.path.join(ProjectPaths.ASSETS, "plan_1", "pkg_1"))
    
    with open(os.path.join(audit_dir, f"{run_id}.json"), "w") as f:
        json.dump(run_data, f)
        
    service = DashboardService()
    runs = service.list_runs()
    assert runs[0].health == RunHealth.PARTIAL

def test_static_asset_mount_isolation(temp_workspace, client):
    # Verify that the static mount actually points to the temp workspace
    plan_id = "test_plan"
    pkg_id = "test_pkg"
    img_name = "test.png"
    pkg_dir = os.path.join(ProjectPaths.ASSETS, plan_id, pkg_id)
    os.makedirs(pkg_dir)
    
    img_content = b"fake image"
    with open(os.path.join(pkg_dir, img_name), "wb") as f:
        f.write(img_content)
        
    response = client.get(f"/assets/{plan_id}/{pkg_id}/{img_name}")
    assert response.status_code == 200
    assert response.content == img_content
