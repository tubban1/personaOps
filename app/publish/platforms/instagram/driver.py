import os
import time
import logging
import json
import re
from pathlib import Path
from typing import Optional, List, Dict, Any
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
from app.publish.base import BaseDriver
from app.publish.caption import CaptionSchema

logger = logging.getLogger("InstagramDriver")

INSTAGRAM_URL = "https://www.instagram.com/"
NAV_TIMEOUT_MS = 90000

class InstagramDriver(BaseDriver):
    """
    (Migrated) 支持多图发布与原片比例的 Instagram 驱动。
    """

    def __init__(self, headless: bool = True, mock_mode: bool = False):
        self.headless = headless
        self.mock_mode = mock_mode

    def _auth_state_has_session(self, auth_file: str) -> bool:
        if self.mock_mode: return True
        if not os.path.exists(auth_file): return False
        try:
            with open(auth_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            cookies = state.get("cookies", [])
            return any(c.get("name") == "sessionid" and c.get("value") for c in cookies)
        except: return False

    def login(self, auth_data: Dict[str, Any]) -> bool:
        if self.mock_mode: return True
        auth_file = auth_data.get("auth_file")
        return self._auth_state_has_session(auth_file) if auth_file else False

    def publish(self, images: List[str], caption: CaptionSchema, **kwargs) -> Dict[str, Any]:
        auth_file = kwargs.get("auth_file")
        result = {"success": False, "post_id": None, "error": None}
        
        if not auth_file and not self.mock_mode:
            result["error"] = "Instagram mission missing auth_file."
            return result

        if not self.mock_mode and not self._auth_state_has_session(auth_file):
            result["error"] = "Instagram session invalid."
            return result
            
        publish_text = caption.build_full_text() # IG 习惯标题和正文连在一起显示

        if self.mock_mode:
            logger.info(f"🌵 [MockMode] Instagram Driver simulate publish for {len(images)} images.")
            return {"success": True, "post_id": "mock_ig_456", "receipt": {"mode": "mock", "platform": "instagram"}}

        with sync_playwright() as p:
            browser = None
            try:
                launch_kwargs = {"headless": self.headless, "args": ["--disable-blink-features=AutomationControlled"]}
                browser = p.chromium.launch(**launch_kwargs)
                context = browser.new_context(storage_state=auth_file)
                page = context.new_page()
                page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                
                page.goto(INSTAGRAM_URL, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
                time.sleep(3)
                
                # 1. 点击“新建”
                create_btn = page.locator("svg[aria-label='New post'], svg[aria-label='新帖子']").locator("..").first
                create_btn.click()
                
                # 2. 上传
                page.set_input_files("input[type='file']", images)
                time.sleep(3)
                
                # 3. 比例优化 (原片)
                try:
                    crop_btn = page.locator("button:has(svg[aria-label*='crop']), button:has(svg[aria-label*='裁剪'])").first
                    if crop_btn.is_visible(timeout=3000):
                        crop_btn.click()
                        original_opt = page.locator("span").filter(has_text=re.compile("^Original$|^原版$", re.I)).first
                        if original_opt.is_visible(timeout=2000):
                            original_opt.click()
                except: pass

                # 4. 下一步链条
                for _ in range(2):
                    next_btn = page.locator("button:has-text('下一步'), button:has-text('Next')").first
                    next_btn.click()
                    time.sleep(2)
                
                # 5. 填写文案
                editor = page.locator("div[aria-label*='caption'], div[role='textbox']").first
                editor.fill(publish_text)
                
                # 6. 分享
                share_btn = page.locator("button:has-text('分享'), button:has-text('Share')").first
                share_btn.click()
                
                time.sleep(5)
                # 确认成功
                if "/create/" not in page.url:
                    result["success"] = True
                    logger.info("✅ Instagram publish likely success.")
                    
            except Exception as e:
                result["error"] = str(e)
                logger.error(f"Instagram Publish Failed: {e}")
            finally:
                if browser: browser.close()
        
        return result
