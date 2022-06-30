from abc import ABC
from dataclasses import fields, dataclass, is_dataclass
from typing import Dict, List
from pprint import pprint


@dataclass
class BasicModel(ABC):

    @classmethod
    def from_dict(cls, dict_object):
        model = cls(**cls.clean_dict(dict_object))
        model.set_not_init_attributes(dict_object)
        return model

    @classmethod
    def clean_dict(cls, raw_dict: Dict) -> Dict:
        """
        This function creates a new dict with only valid keys for this dataclass
        :param raw_dict: dictionary with some keys that correspond to this dataclass attributes
         and other keys that do not.
        :return: a dictionary with keys that correspond only to this dataclass __init__ attributes
        """
        valid_keys = [f.name for f in fields(cls) if f.init]
        return {k: v for (k, v) in raw_dict.items() if k in valid_keys}

    def set_not_init_attributes(self, raw_dict: Dict):
        """
        It assigns 'not init' attributes from a dictionary.
        :param raw_dict: dictionary with assignable keys.
        """
        assignable_attributes = [f.name for f in fields(self) if not f.init]
        for key in assignable_attributes:
            if raw_dict.get(key, None) is not None:
                value = raw_dict.get(key)
                if type(value) == dict or type(value) == Dict:
                    self.set_dictionary_attribute(key, value)
                elif type(value) == list or type(value) == List:
                    self.set_list_attribute(key, value)
                else:
                    setattr(self, key, value)

    def set_dictionary_attribute(self, attribute_name: str, attribute_dict: Dict):
        dict_sub_types = tuple((e.type for e in fields(self) if e.name == attribute_name))[0]
        value_type = getattr(dict_sub_types, '__args__')[1]
        if is_dataclass(value_type):
            if issubclass(value_type, BasicModel):
                subclass_dictionary = {k: value_type.from_dict(v) for (k, v) in attribute_dict.items()}
                setattr(self, attribute_name, subclass_dictionary)
            else:
                fixed_dictionary = {k: value_type(**v) for (k, v) in attribute_dict.items()}
                setattr(self, attribute_name, fixed_dictionary)
        else:
            setattr(self, attribute_name, attribute_dict)

    def set_list_attribute(self, attribute_name: str, attribute_list: List):
        list_sub_type = tuple((e.type for e in fields(self) if e.name == attribute_name))[0]
        value_type = getattr(list_sub_type, '__args__')[0]
        if is_dataclass(value_type):
            if issubclass(value_type, BasicModel):
                subclass_list = [value_type.from_dict(e) for e in attribute_list]
                setattr(self, attribute_name, subclass_list)
            else:
                fixed_list = [value_type(**e) for e in attribute_list]
                setattr(self, attribute_name, fixed_list)
        else:
            setattr(self, attribute_name, attribute_list)
