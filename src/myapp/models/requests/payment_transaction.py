from typing import Any, Dict, TypedDict

class PaymentTransactionRequest(TypedDict, total = False):
    amount: str
    currency: str
    payment_order_id: str
    user_id: str
    merchant_id: str
    card_details: Dict[str, str]