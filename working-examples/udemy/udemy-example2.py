import pika, time

## Publisher

message_count = 15
count = 1

def connect_machine():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='sample_test', durable=True)

    return connection, channel

def disconnect_machine(connection):
    connection.close()

while count <= message_count:
    body_content = "Message number " + str(count)
    count = count + 1
    connection, channel = connect_machine()
    channel.basic_publish(exchange='', routing_key='sample_test', body=body_content)
    disconnect_machine(connection)

## You can run this
# python udemy-example2.py