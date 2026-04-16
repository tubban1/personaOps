import os
import logging
from typing import Optional, Dict, Any
from app.publish.models import PublishAccount

logger = logging.getLogger("SessionManager")

class SessionManager:
    """
    负责管理账号会话、定位 auth 文件并校验稳定性。
    """
    def __init__(self, auth_root: str = "data/auth"):
        self.auth_root = auth_root
        os.makedirs(self.auth_root, exist_ok=True)

    def get_account_auth_path(self, platform: str, account_id: str) -> str:
        """
        统一根据平台和账号识别码定位 Auth 文件路径。
        """
        # 兼容性处理：如果是 xhs_abc 这种形式，提取 abc
        clean_id = account_id.replace(f"{platform}_", "")
        return os.path.join(self.auth_root, f"{platform}_{clean_id}.json")

    def resolve_session(self, platform: str, account_id: str) -> Dict[str, Any]:
        """
        解析并返回用于 Driver 的认证数据字典。
        """
        auth_file = self.get_account_auth_path(platform, account_id)
        exists = os.path.exists(auth_file)
        
        return {
            "auth_file": auth_file,
            "exists": exists,
            "platform": platform,
            "account_id": account_id
        }
