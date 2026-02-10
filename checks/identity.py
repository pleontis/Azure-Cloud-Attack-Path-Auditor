from azure.mgmt.authorization import AuthorizationManagementClient
from engine.risk import RiskFinding, Severity

OWNER_ROLE_ID = "8e3af657-a8ff-443c-a75c-2fe8c4bcb635"


def check_subscription_owners(credential, subscription_id, risk_engine):
    client = AuthorizationManagementClient(credential, subscription_id)

    scope = f"/subscriptions/{subscription_id}"

    assignments = client.role_assignments.list_for_scope(scope)

    for a in assignments:
        if not a.role_definition_id:
            continue

        if a.role_definition_id.lower().endswith(OWNER_ROLE_ID):
            risk_engine.add_owner(
                principal_id=a.principal_id,
                principal_type=a.principal_type,
                scope=a.scope
            )

            risk_engine.add_finding(
                RiskFinding(
                    title="Over-privileged identity (Owner role)",
                    severity=Severity.CRITICAL,
                    details=[
                        f"Principal ID: {a.principal_id}",
                        f"Principal Type: {a.principal_type}",
                        f"Scope: {a.scope}",
                        "Owner role grants full subscription control"
                    ]
                )
            )
