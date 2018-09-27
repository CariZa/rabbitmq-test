import pika

## Consumer

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='sample_test', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue="sample_test", no_ack=True)

print(' [*] Waiting for message. Press CTRL + C to exit.')
channel.start_consuming()

## You can run this
# python udemy-example1.py