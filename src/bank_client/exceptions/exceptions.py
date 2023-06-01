from __future__ import absolute_import

from bank_client.authorization_type import AuthorizationType


class CheckoutException(Exception):

    def __init__(self, message=None):
        super().__init__(message)


class CheckoutArgumentException(CheckoutException):
    pass


class CheckoutAuthorizationException(CheckoutException):

    def __init__(self, message=None):
        super().__init__(message)

    @staticmethod
    def invalid_authorization_type(authorization_type: AuthorizationType):
        raise CheckoutAuthorizationException(
            'The ' + authorization_type.name + ' authorization type is required.')

    @staticmethod
    def invalid_key(key_type: AuthorizationType):
        raise CheckoutAuthorizationException('%s is required.' % key_type.name)


class CheckoutApiException(CheckoutException):
    http_metadata: dict
    error_details: dict
    error_type: str

    def __init__(self, response):
        if response.text:
            payload = response.json()
            self.error_details = payload['error_codes'] if 'error_codes' in payload else None
            self.error_type = payload['error_type'] if 'error_type' in payload else None
        super().__init__('The API response status code ({}) does not indicate success.'
                         .format(response.status_code))