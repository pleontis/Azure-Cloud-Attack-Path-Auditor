import requests
from azure.identity import DefaultAzureCredential


GRAPH_SCOPE = "https://graph.microsoft.com/.default"
GRAPH_BASE = "https://graph.microsoft.com/v1.0"


def get_graph_token():
    credential = DefaultAzureCredential()
    token = credential.get_token(GRAPH_SCOPE)
    return token.token


def graph_get(endpoint):
    token = get_graph_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{GRAPH_BASE}{endpoint}", headers=headers)
    return response


def resolve_principal(principal_id):
    # Try User
    r = graph_get(f"/users/{principal_id}")
    if r.status_code == 200:
        data = r.json()
        return {
            "type": "User",
            "display_name": data.get("displayName"),
            "identifier": data.get("userPrincipalName")
        }

    # Try Service Principal
    r = graph_get(f"/servicePrincipals/{principal_id}")
    if r.status_code == 200:
        data = r.json()
        return {
            "type": "ServicePrincipal",
            "display_name": data.get("displayName"),
            "identifier": data.get("appId")
        }

    return {
        "type": "Unknown",
        "display_name": "Unknown",
        "identifier": principal_id
    }
