#!/usr/bin/env python

import pika
import sys

# establish a connection with rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

# create a queue/check to see if queue exists, idempotent
channel.queue_declare(queue='task_queue', durable=True)


# empty string means default exchange, key means hello queue made above
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print " [x] Sent %r" % (message,)

connection.close()
