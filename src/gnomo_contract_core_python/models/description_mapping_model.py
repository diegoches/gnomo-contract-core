from dataclasses import dataclass, field
from typing import Dict

from src.gnomo_contract_core_python.models.basic_model import BasicModel

'''
Mapping Dict Structure:
{
    'type': '<STRING|INTEGER|FLOAT|OPTIONS|DATE>',
    'options'?: {<key>: <value>}
}
'''


@dataclass
class DescriptionMappingModel(BasicModel):
    type: str
    options: Dict = field(init=False, repr=False, compare=False)
