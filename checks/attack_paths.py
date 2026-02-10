from engine.risk import RiskFinding, Severity


def check_attack_paths(risk_engine):
    owners = risk_engine.context["owners"]
    sp_secrets = risk_engine.context["sp_secrets"]

    if not owners or not sp_secrets:
        return

    for sp in sp_secrets:
        risk_engine.add_finding(
            RiskFinding(
                title="Attack Path: Service Principal → Subscription Takeover",
                severity=Severity.CRITICAL,
                details=[
                    f"Service Principal: {sp['sp_name']}",
                    f"App ID: {sp['app_id']}",
                    f"Secret valid for {sp['days_valid']} days",
                    "Owner role detected in subscription",
                    "Impact: Full subscription compromise possible"
                ]
            )
        )
