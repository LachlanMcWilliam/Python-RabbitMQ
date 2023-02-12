# Python RabbitMQ

Made this to learn how to use RabbitMQ with Python. The project consists of 3 services: RabbitMQ, Sender and Receiver. The Sender service sends messages to RabbitMQ and the Receiver service receives messages from RabbitMQ. The Receiver service is deployed in replicated mode with 3 replicas to check that laod balancing across the containers works. The Receiver is deployed as a Flask application so that multiple requests can be made to a API endpoint in order to send messages to RabbitMQ.

## Requirements

The following software and tools are required to run this project:

- Docker
- Docker Compose

## Running the Project

To run the project, follow these steps:

- Clone the repository to your local machine
- Navigate to the project directory using your terminal
- Run the following command: make up

## Usage

The Sender service exposes an API endpoint that can be used to send messages to RabbitMQ. The following command can be used to send a message to RabbitMQ:

`curl -f localhost:8080`

this will send a single message to RabbitMQ. The Receiver services will receive the message and print it to the console.

## Services

This project consists of the following services:

- RabbitMQ: A messaging broker service
- Sender: A service that sends messages to RabbitMQ
- Receiver: A service that receives messages from RabbitMQ

## Network

The project uses a Docker network named python_rabbitmq_net for communication between services.

## Ports

The following ports are exposed by the services:

- RabbitMQ: Port 15672 is exposed for management purposes.
- Sender: Port 8080 is exposed and maps to the application's default port 5000.
- Receiver: No ports are exposed as this service only receives messages from RabbitMQ.

## Volumes

The following volumes are used by the services:

RabbitMQ:

- ~/.docker-conf/rabbitmq/data/ maps to /var/lib/rabbitmq/
- ~/.docker-conf/rabbitmq/log/ maps to /var/log/rabbitmq

Sender:

- ./sender maps to the /sender directory in the container

Receiver:

- ./reciever maps to the /reciever directory in the container

## Deployment

The Receiver service is deployed in replicated mode with 3 replicas.

## Healthchecks

RabbitMQ has a healthcheck configured that pings the service using the rabbitmq-diagnostics -q ping command. The check is performed every 30 seconds with a timeout of 30 seconds and 3 retries.
