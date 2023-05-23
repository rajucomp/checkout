# Project: Checkout - A Simple Payment Gateway

## Overview
This project is a Flask-based implementation of a payment gateway that provides merchants with the ability to process payments and retrieve payment details. The gateway exposes several APIs to facilitate these operations.

## Requirements
The product requirements for this initial phase are as follows:
1. Merchants should be able to process payments and receive a response indicating success or failure.
2. Merchants should be able to retrieve details of previously made payments.

## API Endpoints
The payment gateway exposes the following API endpoints:

1. Process Payment:
   - **HTTP Method**: POST
   - **Endpoint**: `/v1/payments`
   - **Request Body**:
     ```json
     {
         "merchantId": "merchant123",
         "userId": "user123",
         "cardNumber": "1234567890123456",
         "expiryDate": "12/24",
         "cvv": "123",
         "amount": 99.99,
         "currency": "USD"
     }
     ```
   - **Response**: Success or failure message

2. Retrieve Payment Details:
   - **HTTP Method**: GET
   - **Endpoint**: `/v1/payments/{paymentId}`
   - **Response**: Payment details including masked card number, transaction amount, currency, and status.

3. Webhook (Payment Status Update):
   - **HTTP Method**: POST
   - **Endpoint**: `/v1/webhook`
   - **Request Body**:
     ```json
     {
         "paymentId": "payment123",
         "status": "success"
     }
     ```
   - **Response**: Success or failure message

## Running the Project
To run the project, follow these steps:

1. Navigate to the project directory.
2. Build the Docker image using the following command:
   ```bash
   docker build -t checkout .
   ```
3. Once the image is built, run a container with the following command:
    ```bash
    docker run -it -p 5000:5000 checkout
    ```
This command starts the container and exposes the APIs on port 5000.
Conclusion
The Checkout payment gateway provides a simple and straightforward way for merchants to process payments and retrieve payment details. Feel free to explore the APIs and integrate them into your application.
