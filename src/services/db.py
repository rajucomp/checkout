import threading
from typing import Any, Dict
from models.requests.payment_event import PaymentEventCreationRequest
from models.requests.payment_order import PaymentOrderCreationRequest
from models.payment_response import PaymentResponse
from services.card_masker import CardMasker


class DB:
    __instance = None

    @staticmethod
    def get_instance():
        lock = threading.Lock()
        if DB.__instance is None:
            with lock:
                if DB.__instance is None:
                    DB()
        return DB.__instance

    def __init__(self):
        if DB.__instance is not None:
            raise Exception(
                "Singleton instance already exists. Use get_instance() to access it."
            )
        else:
            DB.__instance = self
            self._payment_events: Dict[str, Any] = {}
            self._payment_orders: Dict[str, Any] = {}

    def insert_payment(self, payment_result: Dict[str, Any]):
        payment_event_creation_request: PaymentEventCreationRequest = {
            "user_id": payment_result["user_id"],
            "payment_id": payment_result["payment_id"],
            "merchant_id": payment_result["merchant_id"],
            "card_details": payment_result["card_details"],
            "amount": payment_result["amount"],
            "currency": payment_result["currency"],
            "payment_status": payment_result["payment_status"],
        }

        self.create_payment_event(payment_event=payment_event_creation_request)

        payment_order_creation_request: PaymentOrderCreationRequest = {
            "user_id": payment_result["user_id"],
            "payment_id": payment_result["payment_id"],
            "merchant_id": payment_result["merchant_id"],
            "card_details": payment_result["card_details"],
            "amount": payment_result["amount"],
            "currency": payment_result["currency"],
            "payment_status": payment_result["payment_status"],
        }
        self.create_payment_order(payment_order=payment_order_creation_request)

    def create_payment_event(self, payment_event: PaymentEventCreationRequest):
        lock = threading.Lock()

        with lock:
            self._payment_events[payment_event["payment_id"]] = payment_event

    def create_payment_order(self, payment_order: PaymentOrderCreationRequest):
        lock = threading.Lock()

        with lock:
            self._payment_orders[payment_order["payment_id"]] = payment_order
    
    def update_payment_status(self, update_payment_status_request: Dict[str, Any]):
        payment_id = update_payment_status_request["payment_id"]
        payment_status = update_payment_status_request["status"]
        bank_transaction_id = update_payment_status_request["bank_transaction_id"]

        if payment_id not in self._payment_orders:
            raise Exception("PaymentId Not Found")
        self._payment_orders[payment_id]["payment_status"] = payment_status
        self._payment_orders[payment_id]["bank_transaction_id"] = bank_transaction_id

    def get_payment_id_details(self, payment_id: str):
        if payment_id not in self._payment_orders:
            return None
        
        payment_details = self._payment_orders[payment_id]
        payment_details["card_details"] = CardMasker.mask_credit_card_info(payment_details["card_details"])

        return payment_details
