import os
import logging
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

logger = logging.getLogger("CanvasEngine")

class CanvasEngine:
    """
    (V4.2 Migrated) 基于 Playwright 的本地模板渲染引擎。
    """
    def __init__(self, mock_mode: bool = False):
        self.mock_mode = mock_mode

    def _make_html_resolvable(self, html_content: str, template_path: str) -> str:
        base_href = Path(template_path).resolve().parent.as_uri() + "/"
        if "<head>" in html_content:
            return html_content.replace("<head>", f'<head><base href="{base_href}">', 1)
        return f'<base href="{base_href}">' + html_content

    def _capture_target(self, page, selector: str, output_path: str) -> bool:
        candidate_selectors = [selector, ".visual-engine", ".card-container", "body"]
        for candidate in candidate_selectors:
            try:
                element = page.locator(candidate).first
                if element.is_visible():
                    element.screenshot(path=output_path, type="jpeg", quality=95)
                    logger.info(f"📸 Captured successful: {candidate}")
                    return True
            except Exception:
                continue
        return False

    def render_html(self, template_path: str, data: dict, output_path: str, selector: str = ".visual-engine", viewport: dict = None) -> bool:
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if self.mock_mode:
            logger.info(f"🌵 [MockRender] Simulating render for {template_path}")
            # 创建一个空的哑文件作为占位符
            with open(output_path, "wb") as f:
                f.write(b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xFF\xDB\x00C\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\xFF\xC0\x00\x09\x08\x00\x01\x00\x01\x01\x01\x00\xFF\xDA\x00\x08\x01\x01\x00\x00\x3F\x00\xD2\xCF\x20\xFF\xD9")
            return True

        if not os.path.exists(template_path):
            logger.error(f"Template not found: {template_path}")
            return False

        with open(template_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 简单变量替换
        for key, value in data.items():
            html_content = html_content.replace(f"{{{{{key}}}}}", str(value))
            
        html_content = self._make_html_resolvable(html_content, template_path)

        if not viewport:
            viewport = {'width': 1200, 'height': 1600}

        with sync_playwright() as p:
            browser = None
            try:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(viewport=viewport)
                page = context.new_page()
                page.set_content(html_content, wait_until="networkidle")
                
                success = self._capture_target(page, selector, output_path)
                return success and os.path.exists(output_path)
            except Exception as e:
                logger.error(f"Render Error: {e}")
                return False
            finally:
                if browser: browser.close()
