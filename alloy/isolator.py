import re

class AlloyIsolator:
    """
    Layer 2: The Alloy
    Responsible for quarantining user input to prevent prompt injection.
    """
    
    @staticmethod
    def quarantine_input(user_query: str) -> str:
        """
        Wraps user input in triple quotes and escapes existing quotes.
        """
        # Neutralize triple quotes to prevent escaping the wrapper
        safe_query = user_query.replace('"""', "'")
        return f'"""\n{safe_query}\n"""'

    @staticmethod
    def extract_result(llm_response: str) -> str:
        """
        Parses the __RESULT__ block from the LLM output.
        """
        match = re.search(r"__RESULT__\s*(.*?)\s*(__STATE__|$)", llm_response, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
      
