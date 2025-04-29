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
        self.identified_op_format = {
            "existing_components": "",
            "new_components_identified": "",
            "perimeter_words_identified": "",
            "potential_attacks_identified": {
                "main_attack_class": {
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    },
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    }
                },
                "main_attack_class": {
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    },
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    }
                }
            },
            "Remarks": ""  # Add a remarks section to capture component identification issues or other relevant observations
        }

    def analyze_architecture(self, image: str, existing_components: list, new_components: list, internet_facing: bool, data_sensitivity: str, attempts: int = 1) -> str:
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
        identify_prompt = self.prompt_service.get_identify_prompt()
        perimeter_words = self.prompt_service.get_perimeter_words()
        common_platforms = self.prompt_service.get_common_platforms()
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
        formatting_prompt = self.prompt_service.build_formatting_prompt(
            identified_output, self.identified_op_format)

        json_output = self.ai_utils.get_completion_json(
            formatting_prompt, attempts=attempts)
        return json_output
