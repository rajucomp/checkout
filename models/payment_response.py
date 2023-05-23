from typing import TypedDict


class PaymentResponse(TypedDict):
    status_code: str
    amount: str
    currency: str
    payment_id: str
    user_id: str
    merchant_id: str
    bank_transaction_id: str
    payment_status: str
