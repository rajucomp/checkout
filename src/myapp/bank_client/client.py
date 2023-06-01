from bank_client.api_client import ApiClient
from bank_client.authorization_type import AuthorizationType
from bank_client.configuration import Configuration


class Client:
    def __init__(
        self,
        api_client: ApiClient,
        configuration: Configuration,
        authorization_type: AuthorizationType,
    ):
        self._api_client = api_client
        self._authorization_type = authorization_type
        self._configuration = configuration

    def _authorization(self, authorization_type: AuthorizationType = None):
        if authorization_type is not None:
            return self._configuration.credentials.get_authorization(authorization_type)
        else:
            return self._configuration.credentials.get_authorization(
                self._authorization_type
            )

    def is_sandbox(self):
        return self._configuration.environment.is_sandbox

    @staticmethod
    def build_path(*params):
        return "/".join(params)
