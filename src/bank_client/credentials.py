from __future__ import absolute_import

from abc import abstractmethod

from bank_client.authorization_type import AuthorizationType


class Credentials:

    @abstractmethod
    def get_authorization(self, authorization_type: AuthorizationType):
        pass