import os
from pathlib import Path

class ProjectPaths:
    """
    (V6.0) 统一路径管理器。
    确保系统在任何工作目录下都能准确定位项目资源与持久化数据。
    """
    # 根目录定位：相对于此脚本的位置
    ROOT = Path(__file__).resolve().parent.parent.parent

    # 核心子目录
    APP = ROOT / "app"
    DATA = ROOT / "data"
    DOCS = ROOT / "docs"
    TESTS = ROOT / "tests"

    # 数据子目录 (基于 DATA)
    @classmethod
    def rebase(cls, new_data_root: str):
        """(V6.1) 为测试提供的动态重定向：重新定位 DATA 根目录"""
        cls.DATA = Path(new_data_root).resolve()
        cls.ENTITIES = cls.DATA / "entities"
        cls.PERSONAS = cls.ENTITIES / "personas"
        cls.BRANDS = cls.ENTITIES / "brands"
        cls.CHANNELS = cls.ENTITIES / "channels"
        cls.ASSETS = cls.DATA / "assets"
        cls.AUDIT = cls.DATA / "audit"
        cls.AUTH = cls.DATA / "auth"
        cls.MEMORY = cls.DATA / "memory"

    # 初始状态
    ENTITIES = DATA / "entities"
    PERSONAS = ENTITIES / "personas"
    BRANDS = ENTITIES / "brands"
    CHANNELS = ENTITIES / "channels"
    ASSETS = DATA / "assets"
    AUDIT = DATA / "audit"
    AUTH = DATA / "auth"
    MEMORY = DATA / "memory"

    @classmethod
    def ensure_dirs(cls):
        """初始化必要的物理目录结构"""
        dirs = [
            cls.DATA, cls.ENTITIES, cls.PERSONAS, cls.BRANDS, cls.CHANNELS,
            cls.ASSETS, cls.AUDIT, cls.AUTH, cls.MEMORY
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

    @classmethod
    def get_persona_path(cls, filename: str) -> str:
        return str(cls.PERSONAS / filename)

    @classmethod
    def get_brand_path(cls, filename: str) -> str:
        return str(cls.BRANDS / filename)

    @classmethod
    def get_channel_path(cls, filename: str) -> str:
        return str(cls.CHANNELS / filename)

    @classmethod
    def get_asset_dir(cls, plan_id: str, timestamp: str) -> str:
        d = cls.ASSETS / plan_id / timestamp
        os.makedirs(d, exist_ok=True)
        return str(d)

    @classmethod
    def get_audit_path(cls, audit_id: str) -> str:
        if audit_id.startswith("aud_"):
            return str(cls.AUDIT / f"{audit_id}.json")
        return str(cls.AUDIT / f"aud_{audit_id}.json")
