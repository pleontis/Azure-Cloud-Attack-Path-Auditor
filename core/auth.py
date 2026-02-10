from azure.identity import AzureCliCredential
from azure.mgmt.resource import SubscriptionClient


def get_azure_context():
    credential = AzureCliCredential()

    sub_client = SubscriptionClient(credential)
    subscription = next(sub_client.subscriptions.list())

    return {
        "credential": credential,
        "subscription_id": subscription.subscription_id
    }
