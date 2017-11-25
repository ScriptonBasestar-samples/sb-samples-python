#!/usr/bin/env python
import pika
import sys

args = sys.argv[1:]


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.56.10'))
channel = connection.channel()

#channel.queue_declare(queue='hello2')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue=args[0],
                      no_ack=True)

channel.start_consuming()
