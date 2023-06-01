from abc import ABC, abstractmethod


class CardValidator(ABC):
    @abstractmethod
    def validate(self, card):
        pass

class CreditCardValidator(CardValidator):
    def validate(self, card):
        # Validate credit card details
        pass

class DebitCardValidator(CardValidator):
    def validate(self, card):
        # Validate debit card details
        pass
