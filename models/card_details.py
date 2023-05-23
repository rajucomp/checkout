from abc import ABC
from typing import TypedDict

class Card(TypedDict, total = False):
    number: str
    expiry_date: str
    cvv_number: str

class CreditCard(Card):
    pass

class DebitCard(Card):
    pass