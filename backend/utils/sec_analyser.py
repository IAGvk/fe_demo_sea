from .utils_gemini import AIUtils  # Assuming utils_gemini.py is in a utils directory
from .utils_prompt_service import PromptService
from .utils_data_models import AnalysisInput, IdentifiedOutputFormat
import json

class SecurityAnalyzer:
    def __init__(self, ai_utils: AIUtils, prompt_service: PromptService):
        """
        Initializes the SecurityAnalyzer with AIUtils and PromptService instances.
        """
        self.ai_utils = ai_utils
        self.prompt_service = prompt_service

    def identify_architecture_gaps(self, image: str, existing_components: str, new_components: str, internet_facing: str, data_sensitivity: str, attempts: int = 1) -> str:
        """Analyzes the architecture diagram for security vulnerabilities."""
        try:
            # Validate input data
            input_data = AnalysisInput(
                existing_components=existing_components,
                new_components=new_components,
                internet_facing=internet_facing,
                data_sensitivity=data_sensitivity
            )
        except Exception as e:
            return json.dumps({"error": f"Invalid input data: {e}"})

        # Build prompts
        perimeter_words = self.prompt_service.get_perimeter_words()
        common_platforms = self.prompt_service.get_common_platforms()
        identify_prompt = self.prompt_service.get_identify_prompt()
        guiding_prompt = self.prompt_service.build_guiding_prompt(
            existing_components, new_components, internet_facing, data_sensitivity)
            
        full_identify_prompt = f"{identify_prompt} \
                 Perimeter words : {perimeter_words},\
                 Common Platforms : {common_platforms} \
                 Guidelines : {guiding_prompt}"

        # First Pass: Get the initial analysis
        identified_output = self.ai_utils.get_completion_img_to_json(
            full_identify_prompt, image, attempts=attempts)

        # Second Pass: Format the output as JSON
        formatting_prompt = self.prompt_service.build_identified_formatting_prompt(
            identified_output)

        json_output = self.ai_utils.get_completion_json(
            formatting_prompt, attempts=attempts)
        return json_output

    def generate_attack_trees(self, image: str, analysis_result_dict: dict, attempts: int = 1) -> str:
        try:
            #'Validate the data'
            pass
        except Exception as e:
            return json.dumps({"error": f"Invalid input data: {e}"})

        
        attack_tree_prompt = self.prompt_service.get_attack_tree_prompt()
        
        identified_output = analysis_result_dict 

        full_attack_tree_prompt = f"{attack_tree_prompt} \
                 Identified Attacks : {identified_output}"

        
        # First Pass: Get the initial analysis
        attack_tree_output = self.ai_utils.get_completion_img_to_json(
            full_attack_tree_prompt, image, attempts=attempts)

        attack_tree_formatting_prompt = self.prompt_service.build_attack_tree_formatting_prompt(
            attack_tree_output)

        json_output = self.ai_utils.get_completion_json(
            attack_tree_formatting_prompt, attempts=attempts)
        return json_output

    def generate_mitigations(self, image: str, analysis_result_dict: dict, attempts: int = 1) -> str:
        try:
            #'Validate the data'
            pass
        except Exception as e:
            return json.dumps({"error": f"Invalid input data: {e}"})

        
        mitigation_prompt = self.prompt_service.get_mitigations_prompt()
        
        previously_generated_analysis = analysis_result_dict 

        full_mitigation_prompt = f"{mitigation_prompt} \
                 Identified Attacks : {previously_generated_analysis}"

        
        # First Pass: Get the initial analysis
        mitigation_output = self.ai_utils.get_completion_img_to_json(
            full_mitigation_prompt, image, attempts=attempts)

        mitigation_formatting_prompt = self.prompt_service.build_mitigations_formatting_prompt(
            mitigation_output)

        json_output = self.ai_utils.get_completion_json(
            mitigation_formatting_prompt, attempts=attempts)
        return json_output