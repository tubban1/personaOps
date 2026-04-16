from typing import List, Optional
import json

class CaptionSchema:
    """
    (V4.8 Migrated) | SCHEMA_VERSION: 1.0.0
    结构化文案 Schema。
    文案不再是单一字符串，而是带有元数据的结构化对象。
    在 personaOps 中，此 Schema 作为下发给执行器的核心文案契约。
    """
    def __init__(self, 
                 platform: str, 
                 title: str = "", 
                 body: str = "", 
                 hashtags: List[str] = None, 
                 call_to_action: str = "", 
                 language: str = "zh-CN"):
        self.platform = platform
        self.title = title
        self.body = body
        self.hashtags = hashtags or []
        self.call_to_action = call_to_action
        self.language = language
        self.source = "persona_driven"
        
    def build_body_text(self) -> str:
        """只拼接正文和标签，不含标题"""
        tag_str = " ".join([f"#{t}" for t in self.hashtags])
        parts = []
        if self.body: parts.append(self.body)
        if self.call_to_action: parts.append(self.call_to_action)
        if tag_str: parts.append(tag_str)
        return "\n\n".join(parts)

    def build_full_text(self) -> str:
        """根据平台特性拼接最终展示文案（含标题）"""
        body = self.build_body_text()
        if self.title and self.platform != "instagram":
            return f"{self.title}\n\n{body}"
        return body

    def to_dict(self) -> dict:
        return {
            "platform": self.platform,
            "title": self.title,
            "body": self.body,
            "hashtags": self.hashtags,
            "call_to_action": self.call_to_action,
            "full_text": self.build_full_text(),
            "language": self.language,
            "source": self.source
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'CaptionSchema':
        return cls(
            platform=data.get("platform", "general"),
            title=data.get("title", ""),
            body=data.get("body", ""),
            hashtags=data.get("hashtags", []),
            call_to_action=data.get("call_to_action", ""),
            language=data.get("language", "zh-CN")
        )

    def save(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
