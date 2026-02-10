import json
import subprocess
from datetime import datetime
from engine.risk import RiskFinding, Severity

AZ_PATH = r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"
LONG_LIVED_DAYS = 180


def check_service_principal_secrets(risk_engine):
    result = subprocess.run(
        [AZ_PATH, "ad", "sp", "list", "--all"],
        capture_output=True,
        text=True,
        shell=False
    )

    if result.returncode != 0:
        print("Failed to execute Azure CLI")
        print(result.stderr)
        return

    sps = json.loads(result.stdout)

    for sp in sps:
        for cred in sp.get("passwordCredentials", []):
            end_date = cred.get("endDateTime")
            if not end_date:
                continue

            expiry = datetime.fromisoformat(end_date.replace("Z", ""))
            days = (expiry - datetime.utcnow()).days

            if days > LONG_LIVED_DAYS:
                risk_engine.add_sp_secret(
                    sp_name=sp.get("displayName"),
                    app_id=sp.get("appId"),
                    days_valid=days
                )

                risk_engine.add_finding(
                    RiskFinding(
                        title="Service Principal with long-lived secret",
                        severity=Severity.HIGH,
                        details=[
                            f"Service Principal: {sp.get('displayName')}",
                            f"App ID: {sp.get('appId')}",
                            f"Secret valid for {days} days",
                            "Long-lived secrets increase compromise risk"
                        ]
                    )
                )
