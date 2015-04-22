#!usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# infinitely wait for data and runs callback func when necessary 
print ' [*] Waiting for messages. To exit press CTRL+C'

# called by pika library when message received from the queue
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

# callback func receives messages from "hello" queue 
# we know it exists bc we created it above, in both send and receive so exists
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
