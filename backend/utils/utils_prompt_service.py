from typing import Dict
from .utils_prompt_base import Prompts
from .utils_prompt_base import JSONPrompts

class PromptService:
    def __init__(self):
        self.prompts = Prompts()
        self.json_prompts = JSONPrompts()

    def get_perimeter_words(self) -> str:
        return self.prompts.PERIMETER_WORDS

    def get_common_platforms(self) -> str:
        return self.prompts.COMMON_PLATFORMS


    def get_identify_prompt(self) -> str:
        return self.prompts.IDENTIFY_PROMPT

    def get_attack_tree_prompt(self) -> str:
        return self.prompts.ATTACK_TREE_PROMPT
        
    def get_mitigations_prompt(self) -> str:
        return self.prompts.MITIGATIONS_PROMPT
    
    def get_json_guidelines(self) -> Dict[str, str]:
        return {
            "base": self.json_prompts.JSON_GUIDELINES_BASE,
            "identified": self.json_prompts.JSON_GUIDELINES_IDENTIFIED,
            "attack_tree": self.json_prompts.JSON_GUIDELINES_ATTACK_TREE,
            "mitigations" : self.json_prompts.JSON_GUIDELINES_MITIGATIONS
        }

    def build_guiding_prompt(self, existing_components: str, new_components: str, internet_facing: str, data_sensitivity: str) -> str:
        """Builds the guiding prompt based on the provided context."""
        guiding_prompt = f"""
        Consider the following:

        1.  Component Identification:
            *   Existing components: {existing_components}
            *   New components: {new_components}
            * Analyse components in the architecture and identify new or existing components based on the above context( if either of them is blank).
                

        2.  Threat Modeling:
            *   Identify potential attacks from both external and internal actors (e.g. developers, authorized users, admins etc). Consider both malicious and accidental actions.
            *   Include risks associated with vendors/suppliers (e.g. supply chain risks).

        3.  Contextual Factors:
            *   Internet Facing: {internet_facing} (Consider vulnerabilities related to internet exposure if Yes.)
            *   Data Sensitivity: {data_sensitivity} (Consider vulnerabilities related to sensitive data handling if it is Protected to Highly Protected. Can be lax for Public and Internal.)

        4.  MITRE ATT&CK Mapping: For each identified attack, provide the corresponding MITRE ATT&CK technique ID and name.

        5.  Output Reasoning: Provide an explanation of why the current architecture is susceptible to each identified technique.
        """
        return guiding_prompt

    def build_identified_formatting_prompt(self, identified_output: str) -> str:
        """Builds the formatting prompt for JSON conversion."""
        json_guidelines = self.get_json_guidelines()
        formatting_prompt = f"""
        Here is the security analysis of an architecture diagram: {identified_output}
        {json_guidelines["base"]}
        {json_guidelines["identified"]}
        """
        return formatting_prompt

    def build_attack_tree_formatting_prompt(self, attack_tree_output: str) -> str:
        """Builds the formatting prompt for JSON conversion."""
        json_guidelines = self.get_json_guidelines()
        formatting_prompt = f"""
        Here is the previously generated attack trees for the architecture diagram: {attack_tree_output}
        {json_guidelines["base"]}
        {json_guidelines["attack_tree"]}
        """
        return formatting_prompt

    def build_mitigations_formatting_prompt(self, mitigations_output: str) -> str:
        """Builds the formatting prompt for JSON conversion."""
        json_guidelines = self.get_json_guidelines()
        formatting_prompt = f"""
        Here is the previously generated attack trees for the architecture diagram: {mitigations_output}
        {json_guidelines["base"]}
        {json_guidelines["mitigations"]}
        """
        return formatting_prompt

