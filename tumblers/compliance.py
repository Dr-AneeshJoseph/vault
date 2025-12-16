import re

class ComplianceTumblers:
    """
    Layer 3: The Tumblers
    Validates output against Financial Regulations (e.g., No Advice, No Guarantees).
    """

    # Liability Triggers: Words a support bot should NEVER say
    FORBIDDEN_TERMS = [
        r"guarantee", r"promise", r"sure thing", 
        r"buy now", r"sell now", r"invest in", 
        r"100% return", r"risk-free", r"predict",
        r"you should buy", r"trust me"
    ]

    def validate(self, agent_response: str):
        """
        Returns (is_compliant: bool, violation: str)
        """
        if not agent_response:
            return False, "EMPTY RESPONSE"
            
        response_lower = agent_response.lower()

        # CHECK 1: The "No Advice" Rule
        for pattern in self.FORBIDDEN_TERMS:
            if re.search(pattern, response_lower):
                return False, f"LIABILITY VIOLATION: Forbidden term '{pattern}' detected."

        # CHECK 2: Length Check (Anti-Hallucination)
        # Support answers shouldn't be essays.
        if len(agent_response) > 2000:
             return False, "QUALITY VIOLATION: Response too long."

        return True, "COMPLIANT"
      
