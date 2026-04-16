import os
import logging
import requests
from typing import Optional, Dict, Any
from app.core.settings import get_vectorengine_config

logger = logging.getLogger("ImageClient")

class ImageClient:
    """
    (V5.2) 图片生成 API 客户端。
    封装对 VectorEngine/OpenAI 兼容接口的调用。
    """
    def __init__(self):
        self.config = get_vectorengine_config()

    def generate_image(self, prompt: str, output_path: str, size: str = "1024x1024") -> bool:
        logger.info(f"🎨 Generating AI image: {prompt[:50]}...")
        
        if not self.config.api_key:
            logger.error("VECTORENGINE_API_KEY is missing.")
            return False

        try:
            # 兼容 OpenAI 的调用方式 (使用 requests 直接调用以避免 sdk 版本冲突)
            url = f"{self.config.base_url.rstrip('/')}/images/generations"
            headers = {
                "Authorization": f"Bearer {self.config.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.config.image_model,
                "prompt": prompt,
                "n": 1,
                "size": size
            }
            
            response = requests.post(url, headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            
            result = response.json()
            image_url = result['data'][0]['url']
            
            # 下载图片
            img_data = requests.get(image_url, timeout=30).content
            with open(output_path, "wb") as f:
                f.write(img_data)
                
            return os.path.getsize(output_path) > 0
            
        except Exception as e:
            logger.error(f"Image generation failed: {e}")
            return False
