from pydantic import BaseModel, validator
from typing import List, Dict, Optional

class IdentifiedOutputFormat(BaseModel):
    existing_components: Optional[str] = None
    new_components_identified: Optional[str] = None
    perimeter_words_identified: Optional[str] = None
    potential_attacks_identified: Optional[Dict[str, Dict[str, Dict[str, str]]]] = None
    Remarks: Optional[str] = None

    @validator('potential_attacks_identified', pre=True, allow_reuse=True)
    def check_potential_attacks_identified(cls, value):
        if value is None:
            return {}
        return value

class AnalysisInput(BaseModel):
    existing_components: List[str]
    new_components: List[str]
    internet_facing: bool
    data_sensitivity: str