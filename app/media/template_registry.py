import os

# (V4.2) personaOps 统一模板注册表
# 定义了不同原型 (Archetype) 的渲染能力与默认配置

ARCHETYPE_REGISTRY = {
    "cover": {
        "desc": "封面视觉原型 (强视觉、大标题)",
        "template_file": "cover.html",
        "capacity": {"hero": 1.0, "summary": 0.6}
    },
    "card": {
        "desc": "万能内容卡片 (文章、清单、引用)",
        "template_file": "card.html",
        "capacity": {"hero": 0.6, "summary": 0.4, "text": 0.9}
    },
    "data_card": {
        "desc": "数据可视化原型 (图表、指标)",
        "template_file": "data_card.html",
        "capacity": {"chart": 1.2, "stats": 0.8}
    },
    "structured_card": {
        "desc": "结构化知识原型 (流程图、逻辑框架)",
        "template_file": "structured_card.html",
        "capacity": {"workflow": 1.4, "formula": 0.7}
    },
    "rough_note": {
        "desc": "手绘故事原型 (草图感、随笔)",
        "template_file": "rough_note.html",
        "capacity": {"hero": 0.8, "summary": 0.4}
    },
    "editorial_card": {
        "desc": "社论风格原型 (大文字量、分栏)",
        "template_file": "editorial_card.html",
        "capacity": {"text": 2.0}
    },
    "formula_card": {
        "desc": "逻辑/公式原型 (KaTeX、代码块)",
        "template_file": "formula_card.html",
        "capacity": {"formula": 1.0, "code": 1.0}
    },
    "workflow": {
        "desc": "流程/思维导图原型 (Mermaid)",
        "template_file": "workflow.html",
        "capacity": {"workflow": 1.5}
    }
}

class TemplateRegistry:
    def __init__(self):
        self.base_dir = os.path.join(os.path.dirname(__file__), "archetypes")

    def get_template_path(self, archetype: str) -> str:
        config = ARCHETYPE_REGISTRY.get(archetype)
        if not config:
            return os.path.join(self.base_dir, "card.html") # Fallback
        return os.path.join(self.base_dir, config["template_file"])

    def get_archetype_config(self, archetype: str) -> dict:
        return ARCHETYPE_REGISTRY.get(archetype, ARCHETYPE_REGISTRY["card"])
