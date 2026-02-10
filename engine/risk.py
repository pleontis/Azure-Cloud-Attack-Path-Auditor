from enum import Enum


class Severity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RiskFinding:
    def __init__(self, title, severity, details):
        self.title = title
        self.severity = severity
        self.details = details


class RiskEngine:
    def __init__(self):
        self.findings = []
        self.context = {
            "owners": [],
            "sp_secrets": []
        }

    def add_finding(self, finding: RiskFinding):
        self.findings.append(finding)

    def add_owner(self, principal_id, principal_type, scope):
        self.context["owners"].append({
            "principal_id": principal_id,
            "principal_type": principal_type,
            "scope": scope
        })

    def add_sp_secret(self, sp_name, app_id, days_valid):
        self.context["sp_secrets"].append({
            "sp_name": sp_name,
            "app_id": app_id,
            "days_valid": days_valid
        })

    def get_findings(self):
        return self.findings

    def print_report(self):
        print("\n==== SECURITY FINDINGS ====\n")
        if not self.findings:
            print("No findings detected.")
            return

        for f in self.findings:
            print(f"[{f.severity.value}] {f.title}")
            for d in f.details:
                print(f"  - {d}")
            print("")
