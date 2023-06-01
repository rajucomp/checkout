from bank_client.api_client import ApiClient
from bank_client.configuration import Configuration
from bank_client.payments.payments_client import PaymentsClient


def get_base_api_client(configuration: Configuration) -> ApiClient:
    return ApiClient(configuration, configuration.environment.base_uri)


class BankApi:
    def __init__(self, configuration: Configuration):
        base_api_client = get_base_api_client(configuration)

        self.payments_client = PaymentsClient(
            api_client=base_api_client, configuration=configuration
        )
