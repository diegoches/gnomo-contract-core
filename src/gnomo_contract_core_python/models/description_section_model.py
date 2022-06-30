from dataclasses import dataclass, field
from typing import Dict

from src.gnomo_contract_core_python.models.basic_model import BasicModel
from src.gnomo_contract_core_python.models.description_mapping_model import DescriptionMappingModel

'''
Section Dict Structure:
{
    'id': '',
    'text': '',
    'metadata': {<key>: <value>},
    'mappings': {<key>: <Mapping>}
}
'''


@dataclass
class DescriptionSectionModel(BasicModel):
    id: str
    text: str
    metadata: Dict
    mappings: Dict[str, DescriptionMappingModel] = field(init=False, repr=False, compare=False)
