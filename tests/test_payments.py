from services.payment_service import PaymentService


class TestPayments:
    def test_payment_status_matches_success_when_payment_is_successful(self) -> None:
        payment_service = PaymentService()

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

        response = payment_service.process_payment(self.request)
        print(response)
        assert response["payment_status"] == "SUCCESS"

    def test_payment_amount_matches_original_amount_when_payment_is_successfuk(
        self,
    ) -> None:
        pass
