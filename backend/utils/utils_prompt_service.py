from typing import Dict
from .utils_prompt_base import Prompts

class PromptService:
    def __init__(self):
        self.prompts = Prompts()

    def get_identify_prompt(self) -> str:
        return self.prompts.IDENTIFY_PROMPT
    
    def get_perimeter_words(self) -> str:
        return self.prompts.PERIMETER_WORDS

    def get_common_platforms(self) -> str:
        return self.prompts.COMMON_PLATFORMS

    def get_json_guidelines(self) -> Dict[str, str]:
        return {
            "base": self.prompts.JSON_GUIDELINES_BASE,
            "identified": self.prompts.JSON_GUIDELINES_IDENTIFIED
        }

    def build_guiding_prompt(self, existing_components: list, new_components: list, internet_facing: bool, data_sensitivity: str) -> str:
        """Builds the guiding prompt based on the provided context."""
        guiding_prompt = f"""
        Analyze the architecture diagram, focusing on security vulnerabilities. Consider the following:

        1.  **Component Identification:**
            *   Identify components based on the legend and color coding.
            *   List components as either "Existing" or "New" based on the following context:
                *   Existing components: {existing_components}
                *   New components: {new_components}
            *   If you cannot identify a specific component, explicitly state it.

        2.  **Threat Modeling:**
            *   Identify potential attacks from both external and internal actors (developers, authorized users, admins). Consider both malicious and accidental actions.
            *   Include risks associated with vendors/suppliers (supply chain risks).

        3.  **Contextual Factors:**
            *   Internet Facing: {internet_facing} (Consider vulnerabilities related to internet exposure)
            *   Data Sensitivity: {data_sensitivity} (Consider vulnerabilities related to sensitive data handling)

        4.  **MITRE ATT&CK Mapping:** For each identified attack, provide the corresponding MITRE ATT&CK technique ID and name.

        5.  **Output Reasoning:** Provide a detailed explanation of why the current architecture is susceptible to each identified technique.
        """
        return guiding_prompt

    def build_formatting_prompt(self, identified_output: str, identified_op_format: dict) -> str:
        """Builds the formatting prompt for JSON conversion."""
        json_guidelines = self.get_json_guidelines()
        formatting_prompt = f"""
        Here is the analysis of the architecture diagram: {identified_output}

        Please reformat the above analysis into a JSON structure, following these guidelines:

        {json_guidelines["base"]}
        Ensure the output conforms precisely to this JSON structure: {identified_op_format}
        """
        return formatting_prompt

