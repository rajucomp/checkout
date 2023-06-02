import json
import uuid
from services.payment_service import PaymentService
from unittest import TestCase
from unittest.mock import patch
import requests

class TestPayments(TestCase):
    @patch("services.payment_service")
    def test_payment_status_matches_success_when_payment_is_successful(self, mock_service) -> None:
        response = {
                "status_code": 200,
                "bank_transaction_id": "d5c472f9-fcbd-4f37-bd7e-2f5aac8dae6e",
                "payment_status": "SUCCESS",
                "response": "Payment processed successfully",
            }
        mock_service.process_payment.return_value = response


        self.request = {
            "data": {
                "processPaymentTransactionRequest": {
                    "requestId": "12345",
                    "merchantId": "JaiShreeRam",
                    "userId": "userId1",
                    "cardDetails": {
                        "cardNumber": "1234-4567-5555-5555",
                        "expiryDate": "2021-01",
                        "cvv": "345",
                    },
                    "amount": "100.00",
                    "currency": "USD",
                }
            }
        }

        base_url = f"http://127.0.0.1:5000/v1/payments"

        response = requests.post(base_url, json=self.request)
        assert response.status_code== 200

    def test_payment_amount_matches_original_amount_when_payment_is_successfuk(
        self,
    ) -> None:
        pass
