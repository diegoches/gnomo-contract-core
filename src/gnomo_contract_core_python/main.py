from transformers.description_to_workflow import DescriptionToWorkflow
from models.contract_description_model import ContractDescriptionModel


def main():
    print('####################')
    print('Gnomo Contract Core')
    print('####################')

    transformer = DescriptionToWorkflow()
    
    description = ContractDescriptionModel.from_file('basic_property_contract_description.json')
    print(description.sections[1].mappings['host_doc_type'].options)
    print(description.global_mappings.keys())


if __name__ == '__main__':
    main()
