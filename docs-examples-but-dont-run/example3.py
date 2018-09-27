import pika

## Single publish

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='test')
channel.basic_publish(exchange='',
                  routing_key='hello',
                  body='Hello W0rld!')
print(" [x] Sent 'Hello World!'")
connection.close()
