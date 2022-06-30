from dataclasses import dataclass
from typing import Dict


@dataclass
class DescriptionSectionModel:
    id: str
    text: str
    metadata: Dict
    mappings: Dict
