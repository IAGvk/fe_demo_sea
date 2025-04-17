import streamlit as st
import requests
import json

def page3():
    st.title("Suggestions for Mitigations")
    context = st.session_state.get("context", {})

    if context:
        # response = requests.post("http://localhost:8000/generate_suggestions", json=context)
        # final_suggestions = response.json()
        # with open("output/final_suggestions.json", "w") as f:
        #     json.dump(final_suggestions, f)
        st.write(final_suggestions)
    

    attacks_to_mitigations_output = {
    "T1566": {
      "attack_technique_name": "Phishing",
      "mitigation_ids": [
        "M1017",
        "M1032",
        "M1031",
        "M1043"
      ],
      "mitigation_names": [
        "User Training",
        "Multi-factor Authentication",
        "Email Filtering",
        "Credential Access Protection"
      ],
      "reasonings": [
        "Conduct regular training sessions to educate users about phishing attacks and how to recognize suspicious emails.",
        "Implement multi-factor authentication (MFA) for Azure AD and Google Cloud access to add an extra layer of security.",
        "Use email filtering solutions to detect and block phishing emails before they reach users.",
        "Use tools to monitor and protect against unauthorized access to credentials."
      ]
    },
    "T1190": {
      "attack_technique_name": "Exploitation of Public-Facing Application",
      "mitigation_ids": [
        "M1048",
        "M1030",
        "M1050",
        "M1036"
      ],
      "mitigation_names": [
        "Application Isolation and Sandboxing",
        "Network Segmentation",
        "Vulnerability Scanning",
        "Web Application Firewall"
      ],
      "reasonings": [
        "Isolate public-facing applications to limit the impact of a potential compromise.",
        "Segment the network to limit access to critical systems and data.",
        "Regularly scan for vulnerabilities in public-facing applications and services.",
        "Deploy a web application firewall (WAF) to protect against common web exploits."
      ]
    },
    "T1195": {
      "attack_technique_name": "Supply Chain Compromise",
      "mitigation_ids": [
        "M1040",
        "M1045",
        "M1044"
      ],
      "mitigation_names": [
        "Supply Chain Management",
        "Code Signing",
        "Application Developer Guidance"
      ],
      "reasonings": [
        "Implement strict supply chain management policies and vet third-party vendors.",
        "Use code signing to ensure the integrity and authenticity of software from third-party vendors.",
        "Provide guidance to developers on secure coding practices and third-party library usage."
      ]
    },
    "T1557": {
      "attack_technique_name": "Man-in-the-Middle",
      "mitigation_ids": [
        "M1021",
        "M1031",
        "M1056"
      ],
      "mitigation_names": [
        "Encrypted Communication",
        "Network Intrusion Prevention",
        "Public Key Infrastructure"
      ],
      "reasonings": [
        "Enforce TLS encryption for all data transfers between components.",
        "Use network intrusion prevention systems to detect and block man-in-the-middle attacks.",
        "Implement a robust public key infrastructure (PKI) to manage and distribute encryption keys."
      ]
    },
    "T1074": {
      "attack_technique_name": "Insider Threat",
      "mitigation_ids": [
        "M1018",
        "M1021",
        "M1040"
      ],
      "mitigation_names": [
        "User Account Management",
        "Data Loss Prevention",
        "User Activity Monitoring"
      ],
      "reasonings": [
        "Implement strict user account management policies, including least privilege access.",
        "Use data loss prevention (DLP) tools to monitor and prevent unauthorized data access or transfer.",
        "Monitor user activities for suspicious behavior and potential insider threats."
      ]
    },
    "T1003": {
      "attack_technique_name": "Credential Dumping",
      "mitigation_ids": [
        "M1027",
        "M1040",
        "M1026"
      ],
      "mitigation_names": [
        "Credential Management",
        "Endpoint Security",
        "Privileged Account Management"
      ],
      "reasonings": [
        "Use strong credential management practices, including regular password changes and MFA.",
        "Deploy endpoint security solutions to detect and prevent credential dumping attempts.",
        "Implement privileged account management to control and monitor the use of privileged accounts."
      ]
    },
    "T1485": {
      "attack_technique_name": "Data Destruction",
      "mitigation_ids": [
        "M1053",
        "M1026",
        "M1049"
      ],
      "mitigation_names": [
        "Data Backup",
        "Access Control",
        "Data Integrity Monitoring"
      ],
      "reasonings": [
        "Regularly back up data stored in Cloud Storage, Alloy DB, and BigQuery to prevent data loss.",
        "Implement strict access control policies to limit who can delete data.",
        "Use tools to monitor data integrity and detect unauthorized data deletion."
      ]
    },
    "T1098": {
      "attack_technique_name": "Misuse of Admin Privileges",
      "mitigation_ids": [
        "M1026",
        "M1058",
        "M1047"
      ],
      "mitigation_names": [
        "Privileged Account Management",
        "Separation of Duties",
        "Audit"
      ],
      "reasonings": [
        "Implement privileged account management to control and monitor the use of admin privileges.",
        "Enforce separation of duties to prevent misuse of admin privileges.",
        "Regularly audit admin activities to detect and respond to unauthorized actions."
      ]
    },
    "T1570": {
      "attack_technique_name": "Misconfiguration",
      "mitigation_ids": [
        "M1040",
        "M1044",
        "M1050"
      ],
      "mitigation_names": [
        "Configuration Management",
        "Security Best Practices",
        "Continuous Monitoring"
      ],
      "reasonings": [
        "Implement configuration management tools to ensure proper configuration of cloud services.",
        "Follow security best practices for configuring IAM roles, network security settings, and Key Management Service.",
        "Continuously monitor configurations for deviations from security policies."
      ]
    },
    "T1078": {
      "attack_technique_name": "Insufficient Logging and Monitoring",
      "mitigation_ids": [
        "M1049",
        "M1050",
        "M1049"
      ],
      "mitigation_names": [
        "Log Analysis",
        "Security Information and Event Management (SIEM)",
        "Alerting"
      ],
      "reasonings": [
        "Implement log analysis tools to monitor and analyze logs from Cloud Logging and Splunk.",
        "Use SIEM solutions to aggregate and analyze security events.",
        "Set up alerting mechanisms to notify security teams of suspicious activities."
      ]
    },
    "T1059": {
      "attack_technique_name": "Insecure API Usage",
      "mitigation_ids": [
        "M1050",
        "M1044",
        "M1030"
      ],
      "mitigation_names": [
        "API Security",
        "Secure Coding Practices",
        "API Gateway"
      ],
      "reasonings": [
        "Implement API security best practices, including authentication, authorization, and input validation.",
        "Train developers on secure coding practices to prevent insecure API usage.",
        "Use an API gateway to manage and secure API traffic."
      ]
    }
  }
    for technique_id, details in attacks_to_mitigations_output.items():
        with st.expander(f"{technique_id}: {details['attack_technique_name']}"):
            st.markdown(f"**Mitigations:**")
            for mitigation_id, mitigation_name, reasoning in zip(details['mitigation_ids'], details['mitigation_names'], details['reasonings']):
                st.markdown(f"- **{mitigation_id} ({mitigation_name}):** {reasoning}")
                
    # st.write(final_suggestions)