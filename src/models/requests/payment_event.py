from typing import Any, Dict, TypedDict

class PaymentEventCreationRequest(TypedDict):
    user_id: str
    payment_id: str
    merchant_id: str
    card_details: Dict[str, str]
    payment_status: str
    amount: str
    currency: str
