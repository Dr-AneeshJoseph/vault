import os
from .alloy.isolator import AlloyIsolator
from .tumblers.compliance import ComplianceTumblers

class VaultOverseer:
    def __init__(self, context_str: str = ""):
        self.isolator = AlloyIsolator()
        self.tumblers = ComplianceTumblers()
        self.context = context_str
        
        # Load System Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'door', 'policy_prompt.md')
        with open(prompt_path, 'r') as f:
            self.base_prompt = f.read()

    def construct_prompt(self, user_query: str) -> str:
        """Constructs the full Context Sandwich."""
        quarantined_input = self.isolator.quarantine_input(user_query)
        
        full_prompt = (
            f"{self.base_prompt}\n\n"
            f"# BANK KNOWLEDGE BASE\n{self.context}\n\n"
            f"USER_DATA_STRING:\n{quarantined_input}"
        )
        return full_prompt

    def process_response(self, llm_raw_response: str):
        """
        Pipeline: Extract -> Validate -> Return
        """
        # 1. Extract Public Response
        public_text = self.isolator.extract_result(llm_raw_response)
        if not public_text:
            return {"valid": False, "error": "Output format violation (No __RESULT__)"}

        # 2. Validate Compliance
        is_compliant, msg = self.tumblers.validate(public_text)

        if is_compliant:
            return {"valid": True, "response": public_text, "status": "SECURE"}
        else:
            return {"valid": False, "error": msg, "rejected_response": public_text}
          
