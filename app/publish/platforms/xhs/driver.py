import os
import time
import logging
import json
from pathlib import Path
from typing import Optional, List, Dict, Any
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
from app.publish.base import BaseDriver
from app.publish.caption import CaptionSchema

logger = logging.getLogger("XHSDriver")

XHS_CREATOR_URL = "https://creator.xiaohongshu.com/"
XHS_IMAGE_PUBLISH_URL = "https://creator.xiaohongshu.com/publish/publish?from=menu&target=image"
NAV_TIMEOUT_MS = 90000

class XHSDriver(BaseDriver):
    """
    (Migrated) 支持状态持久化的小红书发布驱动。
    """

    def __init__(self, headless: bool = True, mock_mode: bool = False):
        self.headless = headless
        self.mock_mode = mock_mode

    def _auth_state_has_session(self, auth_file: str) -> bool:
        """检查 XHS 状态文件是否包含有效会话"""
        if self.mock_mode: return True # Mock 模式下总是认为有会话
        
        if not os.path.exists(auth_file):
            return False
            
        try:
            with open(auth_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 兼容创作者中心新字段判定
            cookies = data.get("cookies", [])
            cookie_names = {c.get("name") for c in cookies if c.get("value")}
            
            valid_cookies = {"web_session", "xhs_sso1", "customer-sso-sid", "galaxy_creator_session_id"}
            has_cookie = any(x in cookie_names for x in valid_cookies)
            
            if has_cookie:
                return True
            return False
        except Exception as e:
            logger.error(f"Error checking XHS session in {auth_file}: {e}")
            return False

    def login(self, auth_data: Dict[str, Any]) -> bool:
        """
        验证登录状态。
        auth_data 预期包含 'auth_file'。
        """
        if self.mock_mode: return True
        
        auth_file = auth_data.get("auth_file")
        if not auth_file:
            logger.error("No auth_file provided for XHS login.")
            return False
            
        if self._auth_state_has_session(auth_file):
            logger.info(f"Verified session for XHS from {auth_file}")
            return True
        return False

    def publish(self, images: List[str], caption: CaptionSchema, **kwargs) -> Dict[str, Any]:
        """
        执行发布。
        :param images: 图片物理路径列表
        :param caption: 结构化文案对象 (CaptionSchema)
        :param kwargs: 必须包含 'auth_file'
        """
        auth_file = kwargs.get("auth_file")
        result = {"success": False, "post_id": None, "error": None}
        
        if not auth_file and not self.mock_mode:
            result["error"] = "XHS mission missing auth_file."
            return result

        if not self.mock_mode and not self._auth_state_has_session(auth_file):
            result["error"] = "XHS session invalid."
            return result
            
        # 从 Schema 提取内容
        title_text = caption.title
        body_text = caption.build_body_text() # (FIXED) 只取正文，避免标题重复
        
        if self.mock_mode:
            logger.info(f"🌵 [MockMode] XHS Driver simulate publish for '{title_text}'")
            return {"success": True, "post_id": "mock_xhs_123", "receipt": {"mode": "mock"}}

        with sync_playwright() as p:
            browser = None
            try:
                launch_kwargs = {"headless": self.headless, "args": ["--disable-blink-features=AutomationControlled"]}
                browser = p.chromium.launch(**launch_kwargs)
                context = browser.new_context(storage_state=auth_file)
                page = context.new_page()
                page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                
                # 1. 访问发布页
                page.goto(XHS_IMAGE_PUBLISH_URL, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
                
                # 2. 上传文件
                logger.info(f"Uploading {len(images)} images...")
                page.locator("input[type='file'][accept*='image']").first.set_input_files(images)
                page.wait_for_selector(".img-container, .upload-image-wrapper", timeout=45000)
                
                # 3. 填写文案
                if title_text:
                    title_input = page.locator("input.d-text[placeholder*='标题']").first
                    title_input.wait_for(state="visible", timeout=10000)
                    title_input.fill(title_text)

                editor = page.locator(".edit-container .tiptap[role='textbox']").first
                editor.wait_for(state="visible", timeout=10000)
                editor.click()
                page.keyboard.insert_text(body_text)

                # 4. 发布
                publish_btn = page.locator("button:has-text('发布'), .custom-button.bg-red").first
                publish_btn.click()
                
                # 5. 结果确认
                try:
                    page.locator("text='发布成功'").wait_for(state="visible", timeout=20000)
                    result["success"] = True
                    logger.info("✅ XHS publish confirmed.")
                except:
                    result["error"] = "Confirmation indicator not found."
                    
            except Exception as e:
                result["error"] = str(e)
                logger.error(f"XHS Publish Failed: {e}")
            finally:
                if browser: browser.close()
        
        return result
