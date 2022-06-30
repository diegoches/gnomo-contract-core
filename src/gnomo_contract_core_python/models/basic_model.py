from abc import ABC, abstractmethod
from dataclasses import fields, dataclass
from typing import Dict


@dataclass
class BasicModel(ABC):

    @classmethod
    def from_dict(cls, dict_object):
        print('---------------------------------------')
        print(dict_object.keys())
        print(cls.clean_dict(dict_object).keys())
        model = cls(**cls.clean_dict(dict_object))
        print(model)
        model.set_not_init_attributes(dict_object)
        print(model)
        print('---------------------------------------')
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
                setattr(self, key, raw_dict.get(key))


