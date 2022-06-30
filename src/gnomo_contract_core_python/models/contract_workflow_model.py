"""
Main Dict Structure:
{
    'title': '',
    'description': '',
    'steps': [<Step>]
}

Step Dict Structure:
{
    'id': '',
    'title': '',
    'description': '',
    'questions': [<Question>]
}

Question Dict Structure:
{
    'id': '',
    'type': '<INPUT|CHECKBOX|DROPDOWN|DATE>',
    'text': '',
    'description': '',
    'value': '',
    'metadata': {<key>: <value>}
}
"""


class ContractWorkflowModel:

    def __init__(self):
        self.data = {}
