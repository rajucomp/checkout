

from datetime import datetime
from enum import Enum
from typing import Dict, TypedDict

from bank_client.authorization_type import AuthorizationType


class BankDetails:
    name: str
    branch: str
    address: str


class AccountHolder:
    type: str
    first_name: str
    last_name: str
    company_name: str
    tax_id: str
    date_of_birth: str
    country_of_birth: str
    billing_address: str
    phone: str
    email: str
    gender: str
    middle_name: str


class PaymentSourceType(str, Enum):
    CARD = "card"
    BANK_ACCOUNT = "bank_account"


class InstructionScheme(str, Enum):
    LOCAL = "local"


class PaymentSenderType(str, Enum):
    CORPORATE = "corporate"


class PaymentType(str, Enum):
    REGULAR = "Regular"


class PaymentDestinationType(str, Enum):
    BANK_ACCOUNT = "bank_account"
    CARD = "card"
    ID = "id"
    TOKEN = "token"


class PreferredSchema(str, Enum):
    VISA = "visa"
    MASTERCARD = "mastercard"


class PaymentInstruction:
    purpose: str
    charge_bearer: str
    repair: bool
    scheme: InstructionScheme
    quote_id: str


# Payment Sender
class PaymentSender:
    type: PaymentSenderType

    def __init__(self, type_p: PaymentSenderType):
        self.type = type_p


class PaymentCorporateSender(PaymentSender):
    company_name: str
    address: str
    reference_type: str
    id: str

    def __init__(self):
        super().__init__(PaymentSenderType.CORPORATE)


# Payment Request Source
class PaymentRequestSource:
    type: str

    def __init__(self, type_p: str):
        self.type = type_p


class PaymentRequestCardSource(PaymentRequestSource):
    number: str
    expiry_month: int
    expiry_year: int
    name: str
    cvv: str
    stored: bool
    store_for_future_use: bool
    billing_address: str
    phone: str

    def __init__(self):
        super().__init__(PaymentSourceType.CARD)


class RequestBankAccountSource(PaymentRequestSource):
    payment_method: str
    account_type: str
    country: str
    account_number: str
    bank_code: str
    account_holder: AccountHolder

    def __init__(self):
        super().__init__(PaymentSourceType.BANK_ACCOUNT)


class PaymentRecipient:
    dob: str
    account_number: str
    address: str
    zip: str
    first_name: str
    last_name: str
    country: str


class SenderInformation:
    firstName: str
    lastName: str
    dob: str
    address: str
    city: str
    state: str
    country: str


class Product:
    name: str
    quantity: int
    unit_price: int
    total_amount: int


class CustomerRequest:
    id: str
    email: str
    name: str
    phone: str


# Request Payment
class ProcessPaymentTransactionRequest(TypedDict, total = False):
    request_id: str
    merchant_id: str
    user_id: str
    card_details: Dict[str, str]
    amount: str
    currency: str

# Payment Request Destination
class PaymentRequestDestination:
    type: PaymentDestinationType

    def __init__(self, type_p: PaymentDestinationType):
        self.type = type_p


class PaymentBankAccountDestination(PaymentRequestDestination):
    account_number: str
    bank_code: str
    branch_code: str
    iban: str
    swift_bic: str
    country: str
    account_holder: str
    bank: BankDetails

    def __init__(self):
        super().__init__(PaymentDestinationType.BANK_ACCOUNT)


class PaymentRequestIdDestination(PaymentRequestDestination):
    id: str

    def __init__(self):
        super().__init__(PaymentDestinationType.ID)


# Query
class PaymentsQueryFilter:
    limit: int
    skip: int
    reference: str


# Authorization
class AuthorizationRequest:
    amount: int
    reference: str
    metadata: dict
