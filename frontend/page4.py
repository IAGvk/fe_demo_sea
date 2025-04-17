import streamlit as st
import requests
import pandas as pd
import json




def page4():
    st.header("Recommended IAG Controls")
    # with open("../input/attacks_mapped_to_mit.json", 'r') as f:
    #     attack_mitigations = json.load(f)

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
        
    # Dictionary with mitigation details
    with open("/app/input/rev_mapping_manual_mit_to_controls_final.json", 'r') as f:
        mitigation_details = json.load(f)
    
    
    # Create a list to store the rows for the dataframe
    rows = []
    
    # Iterate over each attack technique
    for attack_id, attack_info in attacks_to_mitigations_output.items():
        # Iterate over each mitigation for the attack technique
        for i, mitigation_id in enumerate(attack_info["mitigation_ids"]):
            # Get the mitigation details
            mitigation_info = mitigation_details.get(mitigation_id, {})
            
            # Create a row for the dataframe
            row = {
                "technique_id": attack_id,
                "technique_name": attack_info["attack_technique_name"],
                "mitigation_id": mitigation_id,
                "mitigation_name": mitigation_info.get("mitigation_name", ""),
                "mitigation_description": mitigation_info.get("mitigation_description", ""),
                "control_ids": mitigation_info.get("control_ids", []),
                "control_names": mitigation_info.get("control_names", []),
                "reasonings": mitigation_info.get("reasonings", []),
                "course_of_action": mitigation_info.get("course_of_action", "")
            }
            
            # Add the row to the list
            rows.append(row)
    
    # Create a dataframe from the rows
    df = pd.DataFrame(rows)
    
    # Display the dataframe
    #after mounting volumes to app input and output in docker compose
    df.to_csv("/app/output/iag_controls_rec.csv", index=False)
    csv = df.to_csv(index=False).encode('utf-8')

    
    df2 = pd.read_csv("/app/output/iag_controls_rec.csv")
    st.dataframe(df2)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='AI_generated_controls_rec_file_downloaded.csv',
        mime='text/csv',
    )

    return False