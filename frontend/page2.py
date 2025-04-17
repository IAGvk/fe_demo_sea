import streamlit as st
import requests
import json
import os

def page2():
    st.title("Susceptible Attacks")

        
    # options = st.session_state.get("options", [])

    # if options:
    #     selected_options = []
    #     for option in options:
    #         i = options.index(option) + 1
    #         col1, col2 = st.columns([1, 4])
    #         with col1:
    #             if st.checkbox(f"{i}"):
    #                 selected_options.append(option)
    #         with col2:
    #             st.write(f"**{option}**")
    #             st.write("Potential of this attack...")  # Replace with actual content

    #     st.write(selected_options)
    #     if st.button("Submit Selected Options"):
    #         data = {"options": selected_options}
    #         try:
    #             response = requests.post("http://localhost:8000/fetch_context", json=data)
    #             response.raise_for_status()  # Check if the request was successful
    #             context_result = response.json()  # Attempt to parse JSON
    #             with open("output/context.json", "w") as f:
    #                 json.dump(context_result, f)
    #             st.session_state["context"] = context_result
    #             st.success("Context fetched successfully!")
    #             return True
    #         except requests.exceptions.RequestException as e:
    #             st.error(f"Request failed: {e}")
    #         except json.JSONDecodeError:
    #             st.error("Failed to decode JSON response from the server.")
    # else:
    #     st.write("No options available.")
    # return False

    identified_json = {
  "existing_components": [
    "Azure AD",
    "Splunk",
    "GENI BOT endpoint",
    "Internal IAG User",
    "Internal IAG Apps"
  ],
  "new_components_identified": [
    "Google Cloud AAP (Runtime Project)",
    "Cloud Run Orchestrator",
    "Vertex AI",
    "Load Balancer",
    "DNS",
    "Interconnect",
    "Cloud Logging",
    "Pub/Sub",
    "Cloud Storage",
    "Alloy DB",
    "BigQuery",
    "Key Management Service",
    "IAM User",
    "IAM Service Account",
    "Secret Manager",
    "Google Cloud GKE",
    "Docker",
    "Angular"
  ],
  "perimeter_words_identified": [
    "GCP",
    "Internet",
    "Firewall",
    "Gateway",
    "Ingress",
    "Egress",
    "DMZ",
    "Third Party",
    "External",
    "Proxy",
    "Reverse Proxy",
    "CDN",
    "WAF",
    "DDOS"
  ],
  "potential_attacks_identified": {
    "external_threats": {
      "phishing": {
        "technique_id": "T1566",
        "technique_name": "Phishing",
        "description": "Attackers may target internal IAG users with phishing emails to gain access to Azure AD credentials, which can then be used to access the Google Cloud environment."
      },
      "exploitation_of_public_facing_application": {
        "technique_id": "T1190",
        "technique_name": "Exploitation of Public-Facing Application",
        "description": "Although the application is not internet-facing, any misconfiguration in the Load Balancer or DNS settings could expose services unintentionally, making them susceptible to exploitation."
      },
      "supply_chain_compromise": {
        "technique_id": "T1195",
        "technique_name": "Supply Chain Compromise",
        "description": "Risks associated with third-party vendors and suppliers, such as the GENI BOT endpoint and any other external services integrated into the architecture. Compromise of these services could lead to unauthorized access or data breaches."
      },
      "man_in_the_middle": {
        "technique_id": "T1557",
        "technique_name": "Man-in-the-Middle",
        "description": "Intercepting traffic between components, especially if TLS encryption is not properly enforced. This could be a risk at the Interconnect or during data transfer between Google Cloud services."
      }
    },
    "internal_threats": {
      "insider_threat": {
        "technique_id": "T1074",
        "technique_name": "Insider Threat",
        "description": "Malicious or accidental actions by internal IAG users, developers, or admins with access to the Google Cloud environment. This includes unauthorized data access, data deletion, or configuration changes."
      },
      "credential_dumping": {
        "technique_id": "T1003",
        "technique_name": "Credential Dumping",
        "description": "Attackers or malicious insiders could attempt to dump credentials from IAM User or IAM Service Account to gain elevated access within the Google Cloud environment."
      },
      "data_destruction": {
        "technique_id": "T1485",
        "technique_name": "Data Destruction",
        "description": "Accidental or intentional deletion of data stored in Cloud Storage, Alloy DB, or BigQuery by authorized users or compromised accounts."
      },
      "misuse_of_admin_privileges": {
        "technique_id": "T1098",
        "technique_name": "Misuse of Admin Privileges",
        "description": "Abuse of admin privileges by internal users to access sensitive data or perform unauthorized actions within the Google Cloud environment."
      }
    },
    "configuration_and_access_risks": {
      "misconfiguration": {
        "technique_id": "T1570",
        "technique_name": "Misconfiguration",
        "description": "Misconfiguration of cloud services, such as improper IAM roles, insufficient network security settings, or incorrect Key Management Service configurations, leading to unauthorized access or data exposure."
      },
      "insufficient_logging_and_monitoring": {
        "technique_id": "T1078",
        "technique_name": "Insufficient Logging and Monitoring",
        "description": "Lack of proper logging and monitoring in Cloud Logging and Splunk, making it difficult to detect and respond to security incidents in a timely manner."
      },
      "insecure_api_usage": {
        "technique_id": "T1059",
        "technique_name": "Insecure API Usage",
        "description": "Insecure use of APIs between components, such as Cloud Run Orchestrator, Vertex AI, and Pub/Sub, which could be exploited to gain unauthorized access or manipulate data."
      }
    }
  }
}
    predicted_attacks_and_risks = identified_json["potential_attacks_identified"]
    st.write("based on ...")
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("Existing Components"):
            st.write(", ".join(identified_json["existing_components"]))
    
    with col2:
        with st.expander("New Components Identified"):
            st.write(", ".join(identified_json["new_components_identified"]))
    
    with col3:
        with st.expander("Perimeter Words Identified"):
            st.write(", ".join(identified_json["perimeter_words_identified"]))
            
    selected_options = {}

    select_all = st.checkbox("Select All Attacks as Relevant")
    st.write("or individually select relevant attacks applicable!")
    
    for category, attacks in predicted_attacks_and_risks.items():
        st.header(category)
        selected_options[category] = {}
        for attack, description in attacks.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.checkbox(f"Select {attack}", value=select_all):
                    selected_options[category][attack] = description
            with col2:
                st.write(f' **{description["technique_name"]}** ')
                st.write(description["description"])

    st.session_state["selected_options"] = selected_options
    
    if st.button("Submit Selected Options"):
        # data = {"options": selected_options}
        try:
        #     response = requests.post("http://backend:8000/fetch_context", json=data)
        #     response.raise_for_status()  # Check if the request was successful
        #     context_result = response.json()  # Attempt to parse JSON
        #     # tests
        #     curpath = os.path.abspath(os.curdir)
        #     st.write(curpath)
            
        #     with open("../output/context.json", "w") as f:
        #         json.dump(context_result, f)
        #     st.session_state["context"] = context_result
            st.success("Context fetched successfully!")
            return True
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
        except json.JSONDecodeError:
            st.error("Failed to decode JSON response from the server.")
    return False

   
    

    