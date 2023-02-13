import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest'), heartbeat=30,
                              blocked_connection_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='hello')


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print('[X] Waiting for messages.')
channel.start_consuming()
