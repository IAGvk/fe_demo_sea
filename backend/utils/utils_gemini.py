import json
import time
import os
import random
import numpy as np
import tiktoken
import datetime


import google.auth
from google.oauth2 import service_account, credentials
from google.cloud import aiplatform
import vertexai
from vertexai.generative_models import GenerativeModel, Part, GenerationConfig, Image
from .GCPShortLivedCredentials.ServiceAccountConfig import ServiceAccountConfig

os.environ["HTTPS_PROXY"] = "cloudproxy.auiag.corp:8080"

class AIUtils():
 
    def __init__(self,model_name="gemini-1.5-pro-002"):
        self.model_name = model_name
        self.project_id = os.getenv("PROJECT_ID")
        self.app_id = os.getenv("APP_ID")
        self.tenant_id = os.getenv("TENANT_ID")
        self.workload_identity_provider = os.getenv("WORKLOAD_IDENTITY_PROVIDER")
        self.google_service_account_email = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
        self.location_id = os.getenv("LOCATION_ID")
        self.private_key_path = os.getenv("PRIVATE_KEY_PATH")
        print(self.private_key_path)
        sa = ServiceAccountConfig(app_id=self.app_id, thumbprint_path=None, private_key_path=self.private_key_path, tenant_id=self.tenant_id,workload_identity_pool="cf-workload-identity-pool-aad", workload_identity_provider=self.workload_identity_provider ,google_service_account_email=self.google_service_account_email)
        self.ACCESS_TOKEN =sa.retrieve_token()["accessToken"]
        print(self.ACCESS_TOKEN)
        credentials = google.oauth2.credentials.Credentials(self.ACCESS_TOKEN)
        vertexai.init(project=self.project_id, location=self.location_id,credentials=credentials)
       
        self.model = GenerativeModel(model_name)
        self.json_model = GenerativeModel(model_name, generation_config={"response_mime_type": "application/json"})
 
    def run_model(self, content, type, attempts):
        try:

            for attempt in range(attempts):
                #try:
                print(f"Attempt {attempt + 1} of {attempts}")
            
                if type == "json":
                    response = self.json_model.generate_content(content)
                    return response.text
                else:
                    response = self.model.generate_content(content)
                    return response.text

        except:
            sa = ServiceAccountConfig(app_id=self.app_id, thumbprint_path=None, private_key_path=self.private_key_path, tenant_id=self.tenant_id,workload_identity_pool="cf-workload-identity-pool-aad", workload_identity_provider=self.workload_identity_provider ,google_service_account_email=self.google_service_account_email)
            self.ACCESS_TOKEN =sa.retrieve_token()["accessToken"]
            print(self.ACCESS_TOKEN)
            credentials = google.oauth2.credentials.Credentials(self.ACCESS_TOKEN)
            vertexai.init(project=self.project_id, location=self.location_id,credentials=credentials, api_transport="rest")
        
            self.model = GenerativeModel(self.model_name)
            self.json_model = GenerativeModel(self.model_name, generation_config={"response_mime_type": "application/json"})

            print("Retry")
            if type == "json":
                response = self.json_model.generate_content(content)
                return response.text
            else:
                response = self.model.generate_content(content)
                return response.text
                 
    def get_completion(self,content,attempts=1):
        return self.run_model(content,"text",attempts)
 
    def get_completion_json(self,content, attempts=1):
        return self.run_model(content,"json", attempts)
    
    def get_completion_img_to_json(self, content, image, model_name="gemini-1.5-pro-001", attempts=1):
        return self.run_model([content, image], "json", attempts)

    def count_tokens(string: str, encoding_name: str = "cl100k_base") -> int:
        """
        Returns the number of tokens in a string.
        """
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens