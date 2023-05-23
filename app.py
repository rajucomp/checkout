from flask import Flask, request, jsonify
import uuid

from services.payment_service import PaymentService

app = Flask(__name__)

@app.route('/v1/payments', methods=['POST'])
def process_payment():
    data = request.get_json()

    payment_service = PaymentService()
    payment_id = payment_service.process_payment(data)

    if payment_id is None:
        return jsonify({'message': 'Invalid payment details'}), 400

    return jsonify({'transaction_id': payment_id}), 200


@app.route('/v1/payments/<payment_id>', methods=['GET'])
def retrieve_payment(payment_id: str):
    payment_service = PaymentService()
    result = payment_service.get_payment_id_details(payment_id)
    if result is None:
        return jsonify({'message': 'Payment not found'}), 404

    return result