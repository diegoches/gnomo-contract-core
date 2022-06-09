from transformers.description_to_workflow import ModelToWorkflow
from models.contract_description import ContractDescription


def main():
    print('####################')
    print('Gnomo Contract Core')
    print('####################')

    transformer = ModelToWorkflow()
    print(transformer)
    
    description = ContractDescription('basic_property_contract_description.json')
    print(description.data)


if __name__ == '__main__':
    main()
