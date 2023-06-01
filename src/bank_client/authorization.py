from __future__ import absolute_import

from bank_client.exceptions.exceptions import CheckoutAuthorizationException
from bank_client.authorization_platform_type import AuthorizationPlatformType


class Authorization:

    def __init__(self, authorization_platform_type, credential):
        self.authorization_platform_type = authorization_platform_type
        self.credential = credential

    def get_authorization_header(self):
        pass
        '''
        if self.authorization_platform_type in (AuthorizationPlatformType.CUSTOM):
            return self.credential
        if self.authorization_platform_type in (AuthorizationPlatformType.DEFAULT, AuthorizationPlatformType.OAUTH):
            return 'Bearer ' + self.credential
        raise CheckoutAuthorizationException('Invalid authorization platform type')
        '''