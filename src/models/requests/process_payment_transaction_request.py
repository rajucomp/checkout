from typing import Any, Dict, TypedDict


class ProcessPaymentTransactionRequest(TypedDict, total = False):
    request_id: str
    merchant_id: str
    user_id: str
    card_details: Dict[str, str]
    amount: str
    currency: str