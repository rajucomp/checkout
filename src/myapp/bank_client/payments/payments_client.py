from __future__ import absolute_import
from bank_client.api_client import ApiClient
from bank_client.authorization_type import AuthorizationType

from bank_client.client import Client
from bank_client.configuration import Configuration
from bank_client.payments.models import (
    PaymentsQueryFilter,
    ProcessPaymentTransactionRequest,
)


class PaymentsClient(Client):
    __PAYMENTS_PATH = "payments"

    def __init__(self, api_client: ApiClient, configuration: Configuration):
        super().__init__(
            api_client=api_client,
            configuration=configuration,
            authorization_type=AuthorizationType.SECRET_KEY_OR_OAUTH,
        )

    def request_payment(
        self,
        payment_request: ProcessPaymentTransactionRequest,
        idempotency_key: str = None,
    ):
        return self._api_client.post(
            self.__PAYMENTS_PATH,
            #self._authorization(),
            payment_request,
            idempotency_key,
        )

    def get_payments_list(self, query: PaymentsQueryFilter):
        return self._api_client.get(self.__PAYMENTS_PATH, self._authorization(), query)

    def get_payment_details(self, payment_id: str):
        return self._api_client.get(
            self.build_path(self.__PAYMENTS_PATH, payment_id), self._authorization()
        )

    def get_payment_actions(self, payment_id: str):
        return self._api_client.get(
            self.build_path(self.__PAYMENTS_PATH, payment_id, "actions"),
            self._authorization(),
        )
