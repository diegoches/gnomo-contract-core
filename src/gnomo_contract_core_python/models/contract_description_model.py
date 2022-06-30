import json
from dataclasses import dataclass, field
from typing import Dict, List

from src.gnomo_contract_core_python.models.description_mapping_model import DescriptionMappingModel
from src.gnomo_contract_core_python.models.basic_model import BasicModel

'''
Main Dict Structure:
{
    'global_mappings': {<key>: <Mapping>},
    'sections': [<Section>]
}

Section Dict Structure:
{
    'id': '',
    'text': '',
    'metadata': {<key>: <value>},
    'mappings': {<key>: <Mapping>}
}

Mapping Dict Structure:
{
    'type': '<STRING|INTEGER|FLOAT|OPTIONS|DATE>',
    'options'?: {<key>: <value>}
}
'''


@dataclass
class ContractDescriptionModel(BasicModel):
    global_mappings: Dict[str, DescriptionMappingModel] = field(init=False, repr=False, compare=False)
    sections: List

    # @classmethod
    # def from_dict(cls, dict_object):
    #     return cls(**dict_object)

    @classmethod
    def from_file(cls, file_name):
        dict_object = cls.load_from_file(file_name)
        return cls.from_dict(dict_object)

    @classmethod
    def load_from_file(cls, file_name):
        with open(cls.get_mock_file_path(file_name)) as json_file:
            json_object = json.load(json_file)
        return json_object

    @classmethod
    def get_mock_file_path(cls, file_name):
        return f'./mockups/{file_name}'
