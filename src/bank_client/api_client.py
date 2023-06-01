from __future__ import absolute_import

import json
import logging
import mimetypes
from pathlib import Path
import uuid

from requests.exceptions import HTTPError
from bank_client.configuration import Configuration
from bank_client.authorization import Authorization
from bank_client.exceptions.exceptions import CheckoutApiException, CheckoutException
from bank_client.properties import VERSION


class ApiClient:
    _logger = logging.getLogger("checkout")

    def __init__(self, configuration: Configuration, base_uri: str):
        self._http_client = configuration.http_client
        self._base_uri = base_uri

    def get(self, path, authorization: Authorization, params=None):
        return self.invoke(
            method="GET", path=path, authorization=authorization, params=params
        )

    def post(
        self,
        path,
        authorization: Authorization,
        request=None,
        idempotency_key: str = None,
    ):
        return self.invoke(
            method="POST",
            path=path,
            authorization=authorization,
            body=request,
            idempotency_key=idempotency_key,
        )

    def put(self, path, authorization: Authorization, request=None):
        return self.invoke(
            method="PUT", path=path, authorization=authorization, body=request
        )

    def patch(self, path, authorization: Authorization, request=None):
        return self.invoke(
            method="PATCH", path=path, authorization=authorization, body=request
        )

    def delete(self, path, authorization: Authorization):
        return self.invoke(method="DELETE", path=path, authorization=authorization)

    def invoke(
        self,
        method: str,
        path: str,
        authorization: Authorization,
        body=None,
        idempotency_key: str = None,
        params=None,
    ):
        headers = {
            "User-Agent": "checkout-bank-client-python/" + VERSION,
            "Accept": "application/json",
            # "Authorization": authorization.get_authorization_header(),
            "Content-Type": "application/json",
        }

        if idempotency_key is not None:
            headers["Cko-Idempotency-Key"] = idempotency_key

        base_uri = self._base_uri + path

        try:
            json_body = None
            params_dict = None

            if body is not None:
                json_body = json.dumps(body)
            elif params is not None:
                params_dict = json.loads(json.dumps(params))

            self._logger.info(method + " " + path)

            
            # response = self._http_client.request(
            #     method=method,
            #     url=base_uri,
            #     headers=headers,
            #     params=params_dict,
            #     data=json_body,
            # )
            
            response = {
                "status_code": 200,
                "bank_transaction_id": str(uuid.uuid4()),
                "payment_status": "SUCCESS",
                "response": "Payment processed successfully",
            }

            #response.raise_for_status()
        except HTTPError as err:
            self._logger.error(err)
            raise CheckoutApiException(err.response) from err
        except OSError as err:
            error = err.strerror
            raise CheckoutException(error) from err

        return response
