from typing import TypedDict


class PaymentOrderCreationRequest(TypedDict, total = False):
    merchant_id: str
    amount: str
    currency: str
    user_id: str
    payment_order_id: str
    payment_order_status: str