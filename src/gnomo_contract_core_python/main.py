from transformers.description_to_workflow import DescriptionToWorkflow
from models.contract_description_model import ContractDescriptionModel


def main():
    print('####################')
    print('Gnomo Contract Core')
    print('####################')

    transformer = DescriptionToWorkflow()
    print(transformer)
    
    description = ContractDescriptionModel.from_file('basic_property_contract_description.json')
    print(description)
    print(type(description.global_mappings['host']))


if __name__ == '__main__':
    main()
