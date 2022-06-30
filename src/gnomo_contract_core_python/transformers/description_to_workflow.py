from src.gnomo_contract_core_python.models.contract_description_model import ContractDescriptionModel
from src.gnomo_contract_core_python.models.contract_workflow_model import ContractWorkflowModel


class DescriptionToWorkflow:

    @classmethod
    def transform(cls, contract: ContractDescriptionModel) -> ContractWorkflowModel:
        workflow = ContractWorkflowModel()
        
        return workflow
