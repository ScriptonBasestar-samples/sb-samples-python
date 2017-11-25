#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.10'))
channel = connection.channel()

channel.queue_declare(queue='hello2')

t0 = time.time()
for inum in range(1,1000):
    channel.basic_publish(exchange='',
        routing_key='hello2',
        body='Hello World! '+ str(inum))

#channel.basic_publish(exchange='',
#                      routing_key='hello2',
#                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
t1 = time.time()
print (t1-t0)
