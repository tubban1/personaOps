from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class BrandProfile:
    id: str
    name: str
    industry: str = "General"
    business_goal: str = "awareness"  # potential values: 'leads', 'brand', 'conversion'
    target_audience: str = "General"
    tone_constraints: List[str] = field(default_factory=list)
    compliance_rules: List[str] = field(default_factory=list)
    service_catalog: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> 'BrandProfile':
        import inspect
        fields = inspect.signature(cls).parameters
        filtered_data = {k: v for k, v in data.items() if k in fields}
        return cls(**filtered_data)

    @classmethod
    def load_from_file(cls, path: str) -> 'BrandProfile':
        import json
        with open(path, "r", encoding="utf-8") as f:
            return cls.from_dict(json.load(f))

@dataclass
class BrandBinding:
    id: str
    persona_id: str
    brand_id: str
    role_in_brand: str = "Member"  # e.g., 'Intern Guide', 'Ambassador'
    allowed_topics: List[str] = field(default_factory=list)
    blocked_topics: List[str] = field(default_factory=list)
    # Weights for content pillars
    business_weight: float = 0.25
    lifestyle_weight: float = 0.60
    conversion_weight: float = 0.15
