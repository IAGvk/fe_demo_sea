from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import json
import base64

from utils.utils_gemini import AIUtils 
from utils.utils_prompt_service import PromptService 
from utils.sec_analyser import SecurityAnalyzer 
import json

from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Initialize AI utilities
ai_utils = AIUtils()
    # Initialize Prompt Service
prompt_service = PromptService()
    # Initialize Security Analyzer
security_analyzer = SecurityAnalyzer(ai_utils, prompt_service)



class InputData(BaseModel):
    image: str
    questions: list

class OptionsData(BaseModel):
    options: dict

class ContextData(BaseModel):
    context: dict

@app.post("/generate_description")
async def generate_description(data: InputData):
    # Decode the Base64 image
    # image_bytes = base64.b64decode(data.image) if data.image else None
    # Call OpenAI API to generate description and options
    description = "Generated BE description based on image and questions"
    options = ["Attack 4", "Attack 5", "Attack 6"]
    
    existing_components = ["Load Balancer", "Web Server", "Database"]
    new_components = ["API Gateway", "Cache Server"]
    internet_facing = True
    data_sensitivity = "Personally Identifiable Information (PII)"

    # Analyze the architecture
    analysis_result = security_analyzer.analyze_architecture(
        data.image, existing_components, new_components, internet_facing, data_sensitivity, attempts=3)

    # Print the analysis result
    print(analysis_result)
    print(type(analysis_result))
    analysis_result_dict = json.loads(analysis_result)

    return {"description": analysis_result_dict, "options": options}

@app.post("/fetch_context")
async def fetch_context(data: OptionsData):
    context = {}
    for category, attacks in data.options.items():
        context[category] = {}
        for attack in attacks:
            # Fetch context from Qdrant vector DB
            search_result = qdrant_client.search(
                collection_name="subtechniques",
                query_vector=[0.1, 0.2, 0.3],  # Example query vector, replace with actual vector
                query_filter=Filter(
                    must=[
                        FieldCondition(
                            key="option",
                            match=MatchValue(value=attack)
                        )
                    ]
                ),
                top=1  # Fetch top 1 result
            )
            if search_result:
                context[category][attack] = search_result[0].payload.get("context", "No context found")
            else:
                context[category][attack] = "No context found"
    return context

@app.post("/generate_suggestions")
async def generate_suggestions(data: ContextData):
    # Call OpenAI API to generate final suggestions
    suggestions = {option: "Suggestion for " + option for option in data.context.keys()}
    return suggestions

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

