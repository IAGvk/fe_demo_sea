import logging
import requests
from msal import ConfidentialClientApplication
from google.auth import impersonated_credentials
from google.oauth2.credentials import Credentials
from google.oauth2 import sts
from google.auth.transport.requests import Request


class AADFederatedCredentialsManager:
    def __init__(
        self,
        workload_identity_pool: str,
        workload_identity_provider: str,
        msal_app: ConfidentialClientApplication,
        sts_client=sts.Client("https://sts.googleapis.com/v1/token")
    ) -> 'AADFederatedCredentialsManager':

        self.sts_client = sts_client
        self.msal_app = msal_app
        self.workload_identity_pool = workload_identity_pool
        self.workload_identity_provider = workload_identity_provider


    def get_credentials(self, app_id: str, google_service_account_email: str) -> str:
        msal_token = self.__get_msal_token(app_id=app_id)
        gcp_token = self.__exchange_azure_token_for_gcp_token(azure_token=msal_token)
        return self.__impersonate_google_account(google_token=gcp_token, google_service_account_email=google_service_account_email)


    def __get_msal_token(self, app_id: str) -> str:
        scopes = [f"api://{app_id}/.default"]

        azure_response = self.msal_app.acquire_token_silent(scopes=scopes, account=None)

        if not azure_response:
            logging.info("No cached token, retrieving token from AAD.")
            azure_response = self.msal_app.acquire_token_for_client(scopes=scopes)

        if "access_token" in azure_response:
            return azure_response["access_token"]

        raise Exception(
            f"Error retrieving token from AAD. Response: {azure_response}")


    def __exchange_azure_token_for_gcp_token(self, azure_token: str) -> str:
        session = requests.Session()
        session.verify = False
        request = Request(session=session)

        # Project number of the Foundations GCP project containing workload identity pools and providers
        workload_identity_federation_project_number = "349604877559"

        audience = f"//iam.googleapis.com/projects/{workload_identity_federation_project_number}/locations/global/workloadIdentityPools/{self.workload_identity_pool}/providers/{self.workload_identity_provider}"

        sts_token_response = self.sts_client.exchange_token(
            request=request,
            grant_type="urn:ietf:params:oauth:grant-type:token-exchange",
            subject_token=azure_token,
            subject_token_type="urn:ietf:params:oauth:token-type:jwt",
            audience=audience,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
            requested_token_type="urn:ietf:params:oauth:token-type:access_token"
        )

        if "access_token" in sts_token_response:
            return sts_token_response["access_token"]

        raise Exception(f"Error exchanging Azure token. Response: {sts_token_response}")


    def __impersonate_google_account(self, google_token: str, google_service_account_email: str) -> str:
        response = requests.post(url=f"https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/{google_service_account_email}:generateAccessToken", 
                      headers={f"Authorization": f"Bearer {google_token}"}, 
                      data={"scope": ["https://www.googleapis.com/auth/cloud-platform", "https://www.googleapis.com/auth/userinfo.email","https://www.googleapis.com/auth/compute",
                                                                                                                                         "https://www.googleapis.com/auth/ndev.clouddns.readwrite",
                                                                                                                                         "https://www.googleapis.com/auth/devstorage.full_control",
                                                                                                                                         "https://www.googleapis.com/auth/cloud-identity"]},
                      verify=False)
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Error impersonating google account {google_service_account_email}. Error response: {response.json()}")