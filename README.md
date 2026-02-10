# Azure Cloud Attack Path Auditor

An automated Azure cloud security assessment and pentesting-oriented tool focused on identifying **identity misconfigurations**, **over-privileged principals**, and **attack paths that can lead to full subscription compromise**.

The tool combines **cloud security auditing** with **offensive security logic**, correlating Azure RBAC permissions with exposed service principal credentials to uncover real-world takeover scenarios.

---

## Key Features

### 1. Azure Authentication Context
- Uses `AzureCliCredential` for secure, local authentication
- Automatically retrieves the active Azure subscription
- No hardcoded credentials or secrets
- Compatible with free Azure subscriptions

---

### 2. Subscription Owner Enumeration
- Enumerates all role assignments at the subscription scope
- Detects identities assigned the **Owner** role
- Flags over-privileged users, service principals, and managed identities
- Owner role findings are classified as **CRITICAL**

---

### 3. Service Principal Secret Analysis
- Enumerates all Azure AD service principals using Azure CLI
- Inspects password credentials (client secrets)
- Identifies **long-lived secrets** (default threshold: 180 days)
- Highlights increased risk of credential compromise

---

### 4. Attack Path Detection (Pentesting Logic)
- Correlates findings across multiple checks
- Detects attack paths where:
  - A service principal has a long-lived secret
  - **AND** an Owner role exists in the subscription
- Flags scenarios that enable:
  - Full subscription takeover
  - Privilege escalation via compromised CI/CD or automation identities
- Findings are reported as **CRITICAL**

---

### 5. Risk Engine
- Centralized engine for managing findings
- Tracks contextual data (owners, service principal secrets)
- Supports correlation-based security analysis
- Designed for extensibility (risk scoring, MITRE mapping, exports)

---

### 6. Automated Security Reporting
- Generates a professional **Markdown security report**
- Includes:
  - Executive summary
  - Severity overview
  - Detailed technical findings
- Output is suitable for:
  - GitHub repositories
  - Security assessments
  - Portfolio demonstrations

---

## Project Structure

AzureCloudAttackPathAuditor/
│
├── main.py # Tool entry point
├── setup.ps1 # Windows setup script
│
├── core/
│ └── auth.py # Azure authentication & subscription context
│
├── engine/
│ ├── risk.py # Risk engine & findings model
│ └── report.py # Markdown report generator
│
├── checks/
│ ├── identity.py # Subscription owner enumeration
│ ├── service_principals.py # Service principal secret analysis
│ └── attack_paths.py # Attack path correlation logic
│
└── report.md # Generated security report


---

## How It Works

1. Authenticates using the Azure CLI session
2. Enumerates subscription-level RBAC assignments
3. Identifies over-privileged identities
4. Analyzes service principal credentials
5. Correlates findings to detect attack paths
6. Outputs terminal results and a Markdown report

---

## Requirements

- Python 3.10+
- Azure CLI
- Active Azure subscription (Free tier supported)
- Azure CLI login (`az login`)

---

## Installation

### Automated Setup (Windows)

```powershell
git clone https://github.com/yourusername/azure-cloud-attack-path-auditor.git
cd azure-cloud-attack-path-auditor

.\setup.ps1
```

### Manual Setup

git clone https://github.com/yourusername/azure-cloud-attack-path-auditor.git
cd azure-cloud-attack-path-auditor

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

---

## Usage

az login
python main.py

After execution, a report.md file will be generated in the project root

---

## Example Findings

- Over-privileged Owner identities  
- Service principals with long-lived secrets  
- Full subscription takeover attack paths  
- Identity-based privilege escalation scenarios  

---

## Security Focus

This tool is designed with an offensive security mindset, focusing on:

- Identity compromise impact  
- Privilege escalation paths  
- Real-world cloud attack scenarios  
- Defender and red-team visibility  

---

## Disclaimer

This tool is intended for educational and defensive security purposes only.
Run it only against Azure subscriptions you own or are explicitly authorized to test.