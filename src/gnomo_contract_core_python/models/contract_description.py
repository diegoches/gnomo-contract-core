import json

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


class ContractDescription:

    def __init__(self, file_name):
        self.data = self.load_from_file(file_name)

    @classmethod
    def load_from_file(cls, file_name):
        with open(cls.get_mock_file_path(file_name)) as json_file:
            json_object = json.load(json_file)
        return json_object

    @classmethod
    def get_mock_file_path(cls, file_name):
        return f'./mockups/{file_name}'
