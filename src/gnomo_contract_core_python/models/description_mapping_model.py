from dataclasses import dataclass
from typing import Dict


@dataclass
class DescriptionMappingModel:
    type: str
    options: Dict
