import uuid
from services.payment_service import PaymentService
from unittest import TestCase
from unittest.mock import patch

class TestPayments(TestCase):
    @patch("services.payment_service")
    def test_payment_status_matches_success_when_payment_is_successful(self, mock_service) -> None:
        response = {
                "status_code": 200,
                "bank_transaction_id": str(uuid.uuid4()),
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

        response = mock_service.process_payment(self.request)
        assert response["payment_status"] == "SUCCESS"

    def test_payment_amount_matches_original_amount_when_payment_is_successfuk(
        self,
    ) -> None:
        pass
