from http.client import HTTPException
from flask import Flask, request, jsonify, redirect
import uuid

from requests import Session
from bank_client.bank_api import BankApi
from bank_client.configuration import Configuration
from bank_client.credentials import Credentials
from bank_client.environment import Environment

from services.payment_service import PaymentService
from models.logging import log_debug, log_info, log_warning, log_error, log_critical

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(error):
    # Log the exception
    log_error("An unhandled exception occurred.")
    log_error(str(error))

    # Default error response
    response = {
        "message": "Internal Server Error",
        "status_code": 500
    }

    # Custom error response for specific exceptions
    if isinstance(error, HTTPException):
        response["message"] = error.description
        response["status_code"] = error.code

    return jsonify(response), response["status_code"]



@app.route("/v1/payments", methods=["POST"])
def process_payment():

    data = request.get_json()
    log_debug(data)

    configuration = Configuration(credentials=Credentials(), environment=Environment.production(), http_client=Session())

    bank_api = BankApi(configuration)
    payment_service = PaymentService(bank_api)
    payment_id = payment_service.process_payment(data)

    if payment_id is None:
        return jsonify({"message": "Invalid payment details"}), 400

    return jsonify({"transaction_id": payment_id}), 200


@app.route("/v1/payments/<payment_id>", methods=["GET"])
def retrieve_payment(payment_id: str):
    configuration = Configuration(credentials=Credentials(), environment=Environment.production(), http_client=Session())

    bank_api = BankApi(configuration)
    payment_service = PaymentService(bank_api)
    result = payment_service.get_payment_id_details(payment_id)
    if result is None:
        return jsonify({"message": "Payment not found"}), 404

    return result
