import os
from typing import Dict, Any, Optional
from dataclasses import dataclass
from dotenv import load_dotenv

def _load_env_from_data():
    """从约定位置 data/.env 加载配置"""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    env_path = os.path.join(base_dir, "data", ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        # 兼容性：尝试当前目录的 .env
        load_dotenv()

# 执行加载
_load_env_from_data()

@dataclass
class VectorEngineConfig:
    api_key: str
    base_url: str
    image_model: str
    brain_model: str
    planner_model: str
    vision_model: str
    chat_model: str
    router_model: Optional[str] = None
    embedding_model: Optional[str] = None

def get_vectorengine_config() -> VectorEngineConfig:
    """
    (V4.2) 统一获取 VectorEngine 系统配置。
    严格从环境变量读取，不硬编码。
    """
    api_key = os.getenv("VECTORENGINE_API_KEY")
    base_url = os.getenv("VECTORENGINE_URL")
    image_model = os.getenv("VECTORENGINE_IMAGE_MODEL")
    
    # 核心字段严格校验 (FIXED)
    missing = []
    if not api_key: missing.append("VECTORENGINE_API_KEY")
    if not base_url: missing.append("VECTORENGINE_URL")
    if not image_model: missing.append("VECTORENGINE_IMAGE_MODEL")
    
    if missing:
        # 如果是在完全 Mock 模式下运行，可以考虑降级，但根据指令要求，此处应明确报错
        # 为了保证本地 Demo 运行，建议用户在本地 .env 中配置假值
        raise RuntimeError(f"Missing mandatory environment variables: {', '.join(missing)}")

    return VectorEngineConfig(
        api_key=api_key or "",
        base_url=base_url or "",
        image_model=image_model or "dall-e-3",
        brain_model=os.getenv("VECTORENGINE_BRAIN_MODEL", "gpt-4o"),
        planner_model=os.getenv("VECTORENGINE_PLANNER_MODEL", "gpt-4o"),
        vision_model=os.getenv("VECTORENGINE_VISION_MODEL", "gpt-4o-vision"),
        chat_model=os.getenv("VECTORENGINE_CHAT_MODEL", "gpt-4o"),
        router_model=os.getenv("VECTORENGINE_ROUTER_MODEL"), # 可能是 ggpt typo，作为可选
        embedding_model=os.getenv("VECTORENGINE_EMBEDDING_MODEL")
    )
