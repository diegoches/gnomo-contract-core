from ..models.contract_description import ContractDescription
from ..models.contract_workflow import ContractWorkflow


class DescriptionToWorkflow:

    @classmethod
    def transform(cls, contract: ContractDescription) -> ContractWorkflow:
        workflow = ContractWorkflow()
        
        return workflow
