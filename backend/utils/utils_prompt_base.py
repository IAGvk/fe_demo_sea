class Prompts:
    PERIMETER_WORDS = """ PerimeterKeywords : {
                "Context": "List of components commonly occurring in solution architecture diagrams, that can be considered indicators of a security boundary, and therefore requiring additional focus on during Threat Assessment",
                "Values": [
                  {
                    "Name": "Presence of two or more of: GCP, Azure, AWS, On-Prem"
                  },
                  {
                    "Name": "Internet"
                  },
                  {
                    "Name": "Akamai",
                    "Description": "Provides CDN, WAF and DDoS protection for all IAG-managed web applications, which are exposed to the Internet. This generally excludes SaaS applications, which IAG does not manage, as these controls are expected to be already included in the solution, by the vendor. Ingress to Akamai can be any web application consumer, including but not limited to, IAG staff, customers, business partner staff, 3rd party applications. Egress from Akamai is typically limited to a list of endorsed IAG network gateway devices. These include: Apigee, AWS API Gateway, AWS IRIS, ISAM WebSEAL. All traffic in and out of Akamai is expected to be TLS encrypted in transit. Akamai must also enforce a Source IP whitelist on incoming traffic to non-production environments websites."
                  },
                  {
                    "Name": "Apigee",
                    "Description": "Is an API Gateway for all IAG-managed B2B traffic which traverses the internet. Ingress to Apigee should be limited to Akamai for new applications, though existing applications are permitted to allow direct access. Egress from Apigee is typically limited to a list of endorsed IAG gateway devices. These include: AWS API Gateway, AWS IRIS, DataPower. All traffic in and out of Apigee is expected to be TLS encrypted in transit. Apigee must also enforce authentication control, using either client certificate or OAuth2."
                  },
                  {
                    "Name": "Firewall",
                    "Description": "Generally refers to network firewalls. They are typically deployed at a network boundary. Most commonly this will be between the Internet and the on-premises network, or between the on-premises network and IAG’s public cloud tenants. However they are deployed elsewhere too. Firewalls may also have a DMZ interface containing gateway devices."
                  },
                  {
                    "Name": "Gateway",
                    "Description": "A generic term referring to a variety of devices that provide centralised ingress to an internal network."
                  },
                  {
                    "Name": "Ingress",
                    "Description": "A generic term referring to the incoming connections, typically at a network level."
                  },
                  {
                    "Name": "Egress",
                    "Description": "A generic term referring to the outgoing connections, typically at a network level."
                  },
                  {
                    "Name": "DMZ",
                    "Description": "Refers to a portion of the network which can only be reached via a firewall. It typically contains reverse proxies that receive incoming traffic from the Internet."
                  },
                  {
                    "Name": "Third Party",
                    "Description": "A generic term referring to a human or corporate entity that is not part of this organisation."
                  },
                  {
                    "Name": "External",
                    "Description": "A generic term referring to any entity outside the internal network."
                  },
                  {
                    "Name": "DataPower",
                    "Description": "An API reverse proxy that is deployed on premises, in a DMZ. Ingress to DataPower is limited to Apigee. Egress from DataPower may be any webserver on the internal network. All traffic in and out of DataPower is expected to be TLS encrypted. DataPower is expected to enforce URL ACLs and perform coarse grained schema validation of incoming requests."
                  },
                  {
                    "Name": "ISAM",
                    "Description": "Also known as WebSEAL, it is a web reverse proxy that is deployed on premises, in a DMZ. Ingress to ISAM is limited to Akamai. Egress from ISAM may be any webserver on the internal network. Most traffic in and out of ISAM is expected to be TLS encrypted, though valid use-cases for unencrypted http exist. ISAM is expected to enforce URL ACLs. ISAM may also perform user authentication and authorisation, however valid use-cases for unauthenticated access exist, where either the information classification is Public, or a backend webserver will be enforcing this control."
                  },
                  {
                    "Name": "WebSEAL",
                    "Description": "See ISAM."
                  },
                  {
                    "Name": "Customer",
                    "Description": "A generic term referring to a human user who has purchased our products."
                  },
                  {
                    "Name": "Broker",
                    "Description": "A generic term referring to a human user who has a commercial agreement with our organisation to sell our products to customers."
                  },
                  {
                    "Name": "SaaS",
                    "Description": "A generic term referring to any 3rd party application that is used by this organisation, but we do not manage the hosting of."
                  },
                  {
                    "Name": "IRIS",
                    "Description": "The primary Ingress gateway for our AWS environment."
                  },
                  {
                    "Name": "Netskope",
                    "Description": "The web forward proxy all internal users, devices and servers must connect through to access websites on the internet."
                  },
                  {
                    "Name": "Proxy",
                    "Description": "A generic term referring to ingress and egress devices that terminate client connections, typically HTTP, which need to traverse between the internet and internal network."
                  },
                  {
                    "Name": "CASB",
                    "Description": "A generic term referring to Cloud access security broker service."
                  },
                  {
                    "Name": "Reverse proxy",
                    "Description": "A generic term referring to a web reverse proxy service."
                  },
                  {
                    "Name": "CDN",
                    "Description": "A generic term referring to content delivery network service."
                  },
                  {
                    "Name": "WAF",
                    "Description": "A generic term referring to Web application firewall service."
                  },
                  {
                    "Name": "DDOS",
                    "Description": "A generic term referring to a distributed denial of service mitigation provider."
                  }
                ]
              }"""
    COMMON_PLATFORMS = """ {
                    "Context": "List of components commonly occurring in solution architecture diagrams, that also have well understood usage patterns, and therefore require less focus on during Threat Assessment",
                    "Values": [
                      {
                        "Name": "ACRUX",
                        "Description": "An internally managed web hosting platform, hosted in AWS, using S3 to serve static content, and Lambda for dynamic content. Ingress to ACRUX is expected to be limited to Akamai, for user traffic, and GitHub for content deployment. Egress from ACRUX may be any other internal web or database services. Connections to logging and monitoring services such as Splunk and NewRelic may also be illustrated. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "DPLAT",
                        "Description": "Another name for ACRUX."
                      },
                      {
                        "Name": "SK8S",
                        "Description": "An internally managed container hosting platform, hosted in AWS, using EKS. Ingress to SK8S is expected to be limited to IRIS/Akamai, for user traffic, and GitHub for content deployment. Egress from ACRUX may be any other internal web or database services. Connections to logging and monitoring services such as Splunk and NewRelic may also be illustrated. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "CSG Auth",
                        "Description": "An internal application providing web security tokens for service account authentication. Ingress to CSG Auth may be Apigee, or any internal web application. No egress flows are typically illustrated. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "Azure AD",
                        "Description": "Provides user and service account authentication and single sign-on. Ingress and egress flows typically illustrate an authentication flow such as OIDC. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "Entra ID",
                        "Description": "Another name for ACRUX."
                      },
                      {
                        "Name": "Splunk",
                        "Description": "Provides centralised log storage. Ingress flows are expected from the key applications illustrated in the diagram. No egress flows are typically illustrated. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "GitHub",
                        "Description": "Provides source control and Infrastructure as Code provisioning services. Ingress flows are usually human actors, showing application development. Egress flows are typically to the key applications illustrated in the diagram, showing application deployment. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "NewRelic",
                        "Description": "Provides Application Performance Monitoring. Ingress flows are expected from the key applications illustrated in the diagram. No egress flows are typically illustrated. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "ServiceNow",
                        "Description": "Provides a wide range of ITSM and other similar functions. Ingress and egress flows may exist to both human users and applications/system. All connections must utilise TLS transport encryption."
                      },
                      {
                        "Name": "Netskope",
                        "Description": "Provides a centralised web forward proxy service. Ingress flows are expected from internal staff, managed end user devices and internal servers. No ingress from 3rd parties, or SaaS applications. Egress flows may be any web applications accessed via the internet."
                      },
                      {
                        "Name": "Chroma",
                        "Description": "An internally managed, internet exposed application, serving public static information. It provides a supporting function to other internally managed applications. Ingress flows are expected to be from human users across the internet. No egress flows are typically illustrated."
                      },
                      {
                        "Name": "Interconnect",
                        "Description": "A logical term referring to the private network connectivity between internally managed hosting locations (ie. on-premises, AWS cloud, Azure cloud, GCP cloud) or between an internally managed location and a SaaS. Ingress and egress flows are expected to be between these entities only."
                      },
                      {
                        "Name": "Equinix",
                        "Description": "The current vendor for our Interconnect service. Can be used interchangeably with the entity called Interconnect, in diagrams."
                      }
                    ]
                  }"""
    IDENTIFY_PROMPT = """Analyse the given diagram and as per MITRE ATTACK Framework for Enterprise. 
                 Predict the attacks that this architecture is susceptible to. 
                 Provide special attention to perimeter words (if any present in the architecture diagram) and ignore documented risk from common platforms (if they appear in the architecture diagram).
                 Follow the guidelines provided."""
    ATTACK_TREE_PROMPT =  """Consider the shared image for reference. \
                        Create a probable attack tree for each identified attack."""
    MITIGATIONS_PROMPT = """Consider the shared image for reference.  \
                    Provide systematic mitigation suggestions for each of the following identified attacks.\
                    Include as many mitigations as are applicable from the MITRE framework (alongwith mitigation ID) for mitigating each attack for the given architecture."""
    
    
class JSONPrompts:    
    JSON_GUIDELINES_BASE = """Verify the input is valid JSON and adheres to the specified output format. Ensure the output is a JSON-readable format without any extraneous prefix or suffix strings."""
    JSON_GUIDELINES_IDENTIFIED = """Ensure the output conforms precisely to this JSON structure.
                {
            "existing_components": ["", ""],
            "new_components_identified": ["", ""],
            "perimeter_words_identified": ["", ""],
            "potential_attacks_identified": {
                "main_attack_class": {
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    },
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    }
                },
                "main_attack_class": {
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    },
                    "attack_name": {
                        "technique_id": "",
                        "technique_name": "",
                        "description": "Explanation of why the architecture is susceptible to this technique."
                    }
                }
            },
            "Remarks": ""  # Add a remarks section to capture component identification issues or other relevant observations
        }
                """
    JSON_GUIDELINES_ATTACK_TREE = """Ensure the output conforms to this example structure :
        { 
        "External Attacks" :{
                "attack_name" : {
                    "technique_id" : "",
                    "technique_name" : "",
                    "steps" : ["1. Explaining steps how this attack will be carried out on this architecture.",
                              "2. Numbering each step in the list of steps"]
                },
                "attack_name" : {
                    "technique_id" : "",
                    "technique_name" : "",
                    "steps" : ["1. Explaining steps how this attack will be carried out on this architecture.",
                              "2. Numbering each step in the list of steps"]
                }
            },
        "Internal Attacks" :{
                "attack_name" : {
                    "technique_id" : "",
                    "technique_name" : "",
                    "description" : "Explaining steps how this attack will be carried out on this architecture."
                },
                "attack_name" : {
                    "technique_id" : "",
                    "technique_name" : "",
                    "description" : "Explaining steps how this attack will be carried out on this architecture."
                }
            },
        "Vendor/Supplier Risk" : {"...#and other main attack class and their applicable techniques"}
        }
      """
    JSON_GUIDELINES_MITIGATIONS = """Ensure the output conforms to this structure :
        {
      "technique_id_from_MITRE": {
        "attack_technique_name": "Phishing",
        "mitigation_ids": ["M1049", "M1031"],
        "mitigation_names": ["Antivirus/Antimalware", "Network Intrusion Prevention"],
        "reasonings": [
          "Antivirus can automatically quarantine suspicious files.",
          "Network intrusion prevention systems can block malicious email attachments or links."
        ]
      },
      "T1190": {
        "attack_technique_name": "Exploitation of Public-Facing Application",
        "mitigation_ids": ["M1047", "M1051"],
        "mitigation_names": ["Audit", "Update Software"],
        "reasonings": [
          "Perform audits or scans to identify potential weaknesses.",
          "Regular software updates can mitigate exploitation risks."
          ]
        }
      }
      """