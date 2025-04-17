from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import json
import base64


from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    image_bytes = base64.b64decode(data.image) if data.image else None
    # Call OpenAI API to generate description and options
    description = "Generated description based on image and questions"
    options = ["Attack 1", "Attack 2", "Attack 3"]
    return {"description": description, "options": options}

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

