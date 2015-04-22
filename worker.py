#!usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # new durable queue
print ' [*] Waiting for messages. To exit press CTRL+C'

# called by pika library when message received from the queue
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag) # unacked messages will be redelivered

# callback func receives messages from queue 
# we know it exists bc we created it in both send and receive to make sure
channel.basic_qos(prefetch_count=1) # don't give more than one message to a worker at a time
channel.basic_consume(callback,
                      queue='task_queue',)

channel.start_consuming()
