from core.auth import get_azure_context
from engine.risk import RiskEngine
from engine.report import generate_markdown_report
from checks.identity import check_subscription_owners
from checks.service_principals import check_service_principal_secrets
from checks.attack_paths import check_attack_paths


def main():
    ctx = get_azure_context()

    credential = ctx["credential"]
    subscription_id = ctx["subscription_id"]

    risk_engine = RiskEngine()

    check_subscription_owners(credential, subscription_id, risk_engine)
    check_service_principal_secrets(risk_engine)
    check_attack_paths(risk_engine)

    risk_engine.print_report()
    generate_markdown_report(risk_engine.get_findings())


if __name__ == "__main__":
    main()
