from __future__ import absolute_import

from requests import Session

from bank_client.environment import Environment
from bank_client.credentials import Credentials


class Configuration:

    def __init__(self,
                 credentials: Credentials,
                 environment: Environment,
                 http_client: Session):
        self.credentials = credentials
        self.environment = environment
        self.http_client = http_client