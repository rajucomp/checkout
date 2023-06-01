class Environment:
    def __init__(
        self, base_uri, authorization_uri, is_sandbox
    ):
        self.base_uri = base_uri
        self.authorization_uri = authorization_uri
        self.is_sandbox = is_sandbox

    @staticmethod
    def sandbox():
        return Environment(
            base_uri="https://api.sandbox.checkout.com/",
            authorization_uri="https://access.sandbox.checkout.com/connect/token",
            is_sandbox=True,
        )

    @staticmethod
    def production():
        return Environment(
            base_uri="https://api.checkout.com/",
            authorization_uri="https://access.checkout.com/connect/token",
            is_sandbox=False,
        )
