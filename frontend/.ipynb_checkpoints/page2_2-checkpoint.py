import streamlit as st





detailed_attack_tree = {
  "Phishing": {
    "Goal": "Gain unauthorized access to the system",
    "Steps": {
      "Step 1": {
        "Description": "Identify Target",
        "Details": [
          "Identify employees with access to sensitive systems.",
          "Identify high-value targets (e.g., administrators, developers)."
        ]
      },
      "Step 2": {
        "Description": "Craft Phishing Email",
        "Details": [
          "Create a convincing email that appears to come from a trusted source.",
          "Include a malicious link or attachment."
        ]
      },
      "Step 3": {
        "Description": "Send Phishing Email",
        "Details": [
          "Use email spoofing techniques to send the email.",
          "Use social engineering to increase the likelihood of the target clicking the link or opening the attachment."
        ]
      },
      "Step 4": {
        "Description": "Exploit",
        "Details": [
          "If the target clicks the link, redirect them to a fake login page to capture credentials.",
          "If the target opens the attachment, execute malware to gain access to the system."
        ]
      }
    }
  },
  "Exploitation of Public-Facing Application": {
    "Goal": "Exploit misconfigured public-facing services",
    "Steps": {
      "Step 1": {
        "Description": "Identify Misconfiguration",
        "Details": [
          "Scan for misconfigured Load Balancer or DNS settings.",
          "Identify exposed services unintentionally."
        ]
      },
      "Step 2": {
        "Description": "Craft Exploit",
        "Details": [
          "Develop an exploit targeting the identified misconfiguration.",
          "Test the exploit in a controlled environment."
        ]
      },
      "Step 3": {
        "Description": "Execute Exploit",
        "Details": [
          "Deploy the exploit against the misconfigured service.",
          "Gain unauthorized access to the exposed service."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor.",
          "Cover tracks to avoid detection."
        ]
      }
    }
  },
  "Supply Chain Compromise": {
    "Goal": "Compromise third-party services to gain unauthorized access",
    "Steps": {
      "Step 1": {
        "Description": "Identify Third-Party Services",
        "Details": [
          "Identify third-party vendors and suppliers (e.g., GENI BOT endpoint).",
          "Assess the security posture of these services."
        ]
      },
      "Step 2": {
        "Description": "Compromise Third-Party Service",
        "Details": [
          "Exploit vulnerabilities in the third-party service.",
          "Gain unauthorized access to the third-party service."
        ]
      },
      "Step 3": {
        "Description": "Leverage Compromised Service",
        "Details": [
          "Use the compromised service to access the target architecture.",
          "Exfiltrate data or perform unauthorized actions."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor in the compromised service.",
          "Cover tracks to avoid detection."
        ]
      }
    }
  },
  "Man-in-the-Middle": {
    "Goal": "Intercept and manipulate traffic between components",
    "Steps": {
      "Step 1": {
        "Description": "Identify Target Communication",
        "Details": [
          "Identify communication channels between components (e.g., Interconnect, data transfer).",
          "Assess the use of TLS encryption."
        ]
      },
      "Step 2": {
        "Description": "Position Attacker",
        "Details": [
          "Position the attacker in the communication path.",
          "Use techniques like ARP spoofing or DNS poisoning."
        ]
      },
      "Step 3": {
        "Description": "Intercept Traffic",
        "Details": [
          "Capture traffic between components.",
          "Decrypt traffic if TLS encryption is not properly enforced."
        ]
      },
      "Step 4": {
        "Description": "Manipulate Traffic",
        "Details": [
          "Modify intercepted traffic to achieve the attacker's goals.",
          "Inject malicious payloads or exfiltrate data."
        ]
      }
    }
  },
  "Insider Threat": {
    "Goal": "Perform unauthorized actions within the environment",
    "Steps": {
      "Step 1": {
        "Description": "Identify Insider",
        "Details": [
          "Identify internal IAG users, developers, or admins with access.",
          "Assess their access levels and potential motivations."
        ]
      },
      "Step 2": {
        "Description": "Gain Access",
        "Details": [
          "Use legitimate credentials to access the environment.",
          "Exploit any existing privileges."
        ]
      },
      "Step 3": {
        "Description": "Perform Unauthorized Actions",
        "Details": [
          "Access sensitive data or perform unauthorized configuration changes.",
          "Delete or exfiltrate data."
        ]
      },
      "Step 4": {
        "Description": "Cover Tracks",
        "Details": [
          "Use techniques to avoid detection (e.g., log tampering).",
          "Maintain access for future actions."
        ]
      }
    }
  },
  "Credential Dumping": {
    "Goal": "Gain elevated access by dumping credentials",
    "Steps": {
      "Step 1": {
        "Description": "Identify Target Accounts",
        "Details": [
          "Identify IAM User or IAM Service Account with elevated privileges.",
          "Assess the security posture of these accounts."
        ]
      },
      "Step 2": {
        "Description": "Dump Credentials",
        "Details": [
          "Use tools or techniques to dump credentials from the target accounts.",
          "Extract passwords or tokens."
        ]
      },
      "Step 3": {
        "Description": "Gain Elevated Access",
        "Details": [
          "Use the dumped credentials to gain elevated access within the environment.",
          "Perform unauthorized actions."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor using the dumped credentials.",
          "Cover tracks to avoid detection."
        ]
      }
    }
  },
  "Data Destruction": {
    "Goal": "Delete or corrupt data within the environment",
    "Steps": {
      "Step 1": {
        "Description": "Identify Target Data",
        "Details": [
          "Identify critical data stored in Cloud Storage, Alloy DB, or BigQuery.",
          "Assess the impact of data loss."
        ]
      },
      "Step 2": {
        "Description": "Gain Access",
        "Details": [
          "Use legitimate credentials or exploit vulnerabilities to access the target data.",
          "Bypass any security controls."
        ]
      },
      "Step 3": {
        "Description": "Delete or Corrupt Data",
        "Details": [
          "Delete or corrupt the target data.",
          "Ensure the data cannot be easily recovered."
        ]
      },
      "Step 4": {
        "Description": "Cover Tracks",
        "Details": [
          "Use techniques to avoid detection (e.g., log tampering).",
          "Maintain access for future actions."
        ]
      }
    }
  },
  "Misuse of Admin Privileges": {
    "Goal": "Abuse admin privileges to perform unauthorized actions",
    "Steps": {
      "Step 1": {
        "Description": "Identify Admin Accounts",
        "Details": [
          "Identify internal users with admin privileges.",
          "Assess their access levels and potential motivations."
        ]
      },
      "Step 2": {
        "Description": "Gain Access",
        "Details": [
          "Use legitimate credentials to access the environment.",
          "Exploit any existing privileges."
        ]
      },
      "Step 3": {
        "Description": "Perform Unauthorized Actions",
        "Details": [
          "Access sensitive data or perform unauthorized configuration changes.",
          "Delete or exfiltrate data."
        ]
      },
      "Step 4": {
        "Description": "Cover Tracks",
        "Details": [
          "Use techniques to avoid detection (e.g., log tampering).",
          "Maintain access for future actions."
        ]
      }
    }
  },
  "Misconfiguration": {
    "Goal": "Exploit misconfigured cloud services",
    "Steps": {
      "Step 1": {
        "Description": "Identify Misconfiguration",
        "Details": [
          "Scan for misconfigured IAM roles, network security settings, or Key Management Service configurations.",
          "Identify potential vulnerabilities."
        ]
      },
      "Step 2": {
        "Description": "Craft Exploit",
        "Details": [
          "Develop an exploit targeting the identified misconfiguration.",
          "Test the exploit in a controlled environment."
        ]
      },
      "Step 3": {
        "Description": "Execute Exploit",
        "Details": [
          "Deploy the exploit against the misconfigured service.",
          "Gain unauthorized access or expose data."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor.",
          "Cover tracks to avoid detection."
        ]
      }
    }
  },
  "Insufficient Logging and Monitoring": {
    "Goal": "Exploit lack of logging and monitoring to avoid detection",
    "Steps": {
      "Step 1": {
        "Description": "Identify Logging Gaps",
        "Details":[
          "Assess the logging and monitoring setup in Cloud Logging and Splunk.",
          "Identify gaps or weaknesses."
        ]
      },
      "Step 2": {
        "Description": "Perform Actions",
        "Details": [
          "Perform unauthorized actions within the environment.",
          "Exploit the identified logging gaps to avoid detection."
        ]
      },
      "Step 3": {
        "Description": "Cover Tracks",
        "Details": [
          "Use techniques to avoid detection (e.g., log tampering).",
          "Ensure actions are not logged or monitored."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor.",
          "Continue exploiting the logging gaps."
        ]
      }
    }
  },
  "Insecure API Usage": {
    "Goal": "Exploit insecure APIs to gain unauthorized access",
    "Steps": {
      "Step 1": {
        "Description": "Identify Insecure APIs",
        "Details": [
          "Identify APIs used between components (e.g., Cloud Run Orchestrator, Vertex AI, Pub/Sub).",
          "Assess the security posture of these APIs."
        ]
      },
      "Step 2": {
        "Description": "Craft Exploit",
        "Details": [
          "Develop an exploit targeting the identified insecure APIs.",
          "Test the exploit in a controlled environment."
        ]
      },
      "Step 3": {
        "Description": "Execute Exploit",
        "Details": [
          "Deploy the exploit against the insecure APIs.",
          "Gain unauthorized access or manipulate data."
        ]
      },
      "Step 4": {
        "Description": "Maintain Access",
        "Details": [
          "Establish a persistent backdoor.",
          "Cover tracks to avoid detection."
        ]
      }
    }
  }
}


def page2_2():
    st.header("Detailed Attack Trees")
    selected_options = st.session_state.get("selected_options", {})
    # st.json(selected_options)
    # if selected_options:
    #     for attack in selected_options:
    #         if attack in detailed_attack_tree:
    #             st.header(attack)
    #             st.write(f"**Goal:** {detailed_attack_tree[attack]['Goal']}")
    #             for step, details in detailed_attack_tree[attack]['Steps'].items():
    #                 st.subheader(step)
    #                 st.write(f"**Description:** {details['Description']}")
    #                 st.write("**Details:**")
    #                 for detail in details['Details']:
    #                     st.write(f"- {detail}")
    #     return True
    # else:
    #     st.write("No Options")

    # def dict_to_markdown(detailed_attack_tree):
    #     markdown = ""
    #     for attack, details in detailed_attack_tree.items():
    #         markdown += f"## {attack}\n"
    #         markdown += f"**Goal:** {details['Goal']}\n\n"
    #         markdown += f"### Steps:\n"
    #         for step, step_details in details['Steps'].items():
    #             markdown += f"#### {step}: {step_details['Description']}\n"
    #             markdown += f"**Details:**\n"
    #             for detail in step_details['Details']:
    #                 markdown += f"- {detail}\n"
    #         markdown += "\n"
    #     return markdown

    # # Convert dictionary to markdown
    # markdown_output = dict_to_markdown(detailed_attack_tree)

    def dict_to_markdown(detailed_attack_tree):
        markdown = ""
        for attack, details in detailed_attack_tree.items():
            with st.expander(f"{attack}"):
                st.markdown(f"**Goal:** {details['Goal']}\n")
                st.markdown(f"### Steps:")
                for step, step_details in details['Steps'].items():
                    st.markdown(f"#### {step}: {step_details['Description']}\n")
                    st.markdown(f"**Details:**")
                    for detail in step_details['Details']:
                        st.markdown(f"- {detail}\n")

    # Convert dictionary to markdown
    dict_to_markdown(detailed_attack_tree)

    
    return False