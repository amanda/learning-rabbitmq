#!/usr/bin/env python

import pika

# establish a connection with rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

# create a queue/check to see if queue exists, idempotent
channel.queue_declare(queue='hello')

# empty string means default exchange, key means hello queue made above
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"

connection.close()
