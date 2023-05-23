from typing import Any, Dict
from models.card_details import Card


class CardMasker:
    @staticmethod
    def mask_credit_card_info(
        card_details: Dict[str, str]
    ) -> Dict[str, Any]:
        card_number = card_details["cardNumber"]

        masked_card_details: Card = {
            "expirydate": card_details["expiryDate"],
            "card_number": "*" * (len(card_number) - 4) + card_number[-4:],
            "cvv_number": None
        }

        return masked_card_details
