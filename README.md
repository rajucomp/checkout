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


## Assumptions Made
1. This is a very basic API that doesn't handle authentication, authorization, and validation.

2. We trust the client to send us data in the expected format as expected.

3. The service is built such that it will run on a single instance. It is not designed to be built on a distributed design as that is out of scope.



## Areas for Improvement
1. There are a lot of areas for improvement. Each one of the areas listed below is essential to a production-grade payment gateway.

2. Each request needs to check for authentication, authorization, validation, and fraud detection before it is allowed to enter the internal system.

3. There should be a schema registry that allows us to register our schema and view others' schemas so as to know what kinds of requests need to be made. This also helps with backward compatibility.

4. Currently, the project only supports one payment method. Ideally, it should support multiple payment methods like debit/credit cards, internet banking, gift cards, etc.

5. The data is not securely stored, which is extremely important for a payment gateway. Ideally, we should use clients that are compliant with the appropriate security standards or, if we are going to store the data itself, great care should be taken to securely encrypt and store the data.

6. Billing and subscription features should be added for a seamless customer experience.

7. Reporting and analytics should be added as additional features.

8. Test-driven development (TDD) and behavior-driven development (BDD) need to be implemented. Currently, only a basic testing scenario is implemented.

9. Since we are dealing with external services, we should use a circuit breaker to shield the system from long-term downtimes and save costs.

10. Ledger bookkeeping and wallet features should be added so that transactions can be reconciled at the end of the day.