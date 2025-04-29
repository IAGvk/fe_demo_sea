from msal import ConfidentialClientApplication
from .AADFederatedCredentialsManager import AADFederatedCredentialsManager
import os
import base64

class ServiceAccountConfig:
        def __init__(
        self,
        app_id: str,
        thumbprint_path: str,
        private_key_path: str,
        tenant_id: str,
        workload_identity_pool: str,
        workload_identity_provider: str,
        google_service_account_email: str):
        
            self.app_id = app_id
            self.thumbprint_path = thumbprint_path
            self.workload_identity_pool = workload_identity_pool
            self.workload_identity_provider = workload_identity_provider
            self.private_key_path = private_key_path
            self.tenant_id = tenant_id
            self.google_service_account_email = google_service_account_email

        def get_private_key(self):
            private_key = os.getenv("PRIVATE_KEY")
            if private_key:
                 return base64.b64decode(private_key).decode('utf-8')
            with open(self.private_key_path, "rb") as key:
                private_key = key.read()
            return private_key


        def get_thumbprint(self):
            thumbprint = os.getenv("THUMBPRINT")
            if thumbprint:
                 return thumbprint
            with open(self.thumbprint_path, "r") as key:
                thumbprint = key.read()
            return thumbprint
        
        def retrieve_token(self):
            msal_app = ConfidentialClientApplication(
            client_id=self.app_id,
            authority=f"https://sts.windows.net/{self.tenant_id}", 
            client_credential={"thumbprint": self.get_thumbprint(), "private_key": self.get_private_key()},
            validate_authority=False,
            verify=False)
                
            credentials_manager = AADFederatedCredentialsManager(
                workload_identity_pool=self.workload_identity_pool,
                workload_identity_provider=self.workload_identity_provider, 
                msal_app=msal_app
            )

            return credentials_manager.get_credentials(app_id=self.app_id, google_service_account_email=self.google_service_account_email)