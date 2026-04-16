import logging
import os
import uuid
from typing import Dict, Any, List, Optional
from app.publish.models import PublishRequest, PublishResult
from app.publish.session_manager import SessionManager
from app.publish.platforms.xhs.driver import XHSDriver
from app.publish.platforms.instagram.driver import InstagramDriver
from app.audit.models import AuditRecord
from app.core.paths import ProjectPaths

logger = logging.getLogger("RuntimeManager")

class RuntimeManager:
    """
    (V4.2) 运行时管理器：负责调度具体的平台驱动并记录审计日志。
    """
    def __init__(self):
        self.session_manager = SessionManager()
        self.drivers = {
            "xhs": XHSDriver,
            "instagram": InstagramDriver
        }

    def submit_publish(self, request: PublishRequest) -> PublishResult:
        logger.info(f"🚀 Dispatching publish request for {request.platform} | Account: {request.account_id}")
        
        # 1. 查找驱动类
        driver_cls = self.drivers.get(request.platform)
        if not driver_cls:
            return PublishResult(success=False, platform=request.platform, account_id=request.account_id, error=f"Driver not found for {request.platform}")

        # 2. 准备 Session
        session_info = self.session_manager.resolve_session(request.platform, request.account_id)
        
        # 3. 实例化驱动
        driver = driver_cls(headless=True, mock_mode=request.mock_mode)
        
        # 4. 执行发布
        audit_id = f"aud_{uuid.uuid4().hex[:8]}"
        try:
            res_dict = driver.publish(
                images=request.images,
                caption=request.caption,
                auth_file=session_info["auth_file"]
            )
            
            # 5. 生成结果
            result = PublishResult(
                success=res_dict.get("success", False),
                platform=request.platform,
                account_id=request.account_id,
                post_id=res_dict.get("post_id"),
                receipt=res_dict.get("receipt", {}),
                error=res_dict.get("error"),
                audit_id=audit_id
            )
            
            # 6. 持久化审计记录 (V4.2)
            self._save_audit(request, result)
            return result
            
        except Exception as e:
            logger.error(f"Execution error in RuntimeManager: {e}")
            return PublishResult(success=False, platform=request.platform, account_id=request.account_id, error=str(e), audit_id=audit_id)

    def _save_audit(self, request: PublishRequest, result: PublishResult):
        """保存执行审计到统一审计目录 (V6.0 FIXED)"""
        import json
        
        record = AuditRecord(
            id=result.audit_id,
            plan_id=request.post_plan_id or "unplanned",
            platform=result.platform,
            account_id=result.account_id,
            status="success" if result.success else "failed",
            mode="mock" if request.mock_mode else "real",
            driver_name=request.platform.upper(),
            error=result.error,
            receipt=result.receipt
        )
        
        save_path = ProjectPaths.get_audit_path(record.id)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(record.__dict__, f, indent=2, ensure_ascii=False)
        logger.info(f"📊 Audit record saved: {save_path}")
