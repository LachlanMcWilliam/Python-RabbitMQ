from flask import Flask
import pika

app = Flask(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest'), heartbeat=30,
                              blocked_connection_timeout=300))


@app.route('/')
def send():
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

    return '[x] Sent message'

# As of right now the connection to rabbitmq is not closed, should be handled but as I am restarting the container every time I dont mind that much rn
