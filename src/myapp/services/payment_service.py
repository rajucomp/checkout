from typing import Any, Dict
from bank_client.bank_api import BankApi
from models.payment_response import PaymentResponse
from models.requests.process_payment_transaction_request import (
    ProcessPaymentTransactionRequest,
)
import uuid

from services.db import DB


class PaymentService:
    def __init__(self, bank_api: BankApi) -> None:
        self.db = DB.get_instance()
        self.bank_api = bank_api

    def update_payment_status(self, update_payment_status_request: Dict[str, Any]):
        self.db.update_payment_status(update_payment_status_request)

    def process_payment(self, request: Dict[str, Any]):
        data = request["data"]["processPaymentTransactionRequest"]

        payment_id = str(uuid.uuid4())

        payment_transaction_request: ProcessPaymentTransactionRequest = {
            "amount": data["amount"],
            "currency": data["currency"],
            "payment_id": str(uuid.uuid4()),
            "user_id": data["userId"],
            "merchant_id": data["merchantId"],
            "card_details": data["cardDetails"],
        }

        response = self.bank_api.payments_client.request_payment(payment_transaction_request)

        if response["payment_status"] not in [("SUCCESS")]:
            return {"payment_id": None, "payment_status": "FAILED"}

        payment_result: PaymentResponse = {
            "payment_status": response["payment_status"],
            "amount": data["amount"],
            "currency": data["currency"],
            "payment_id": payment_id,
            "user_id": data["userId"],
            "merchant_id": data["merchantId"],
            "card_details": data["cardDetails"],
            "bank_transaction_id": response["bank_transaction_id"],
        }

        # Store overall payment details
        db = DB.get_instance()
        db.insert_payment(payment_result)

        return {"payment_id": payment_id, "payment_status": "SUCCESS"}

    def get_payment_id_details(self, payment_id: str):
        return self.db.get_payment_id_details(payment_id=payment_id)
