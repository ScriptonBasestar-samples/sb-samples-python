#!/usr/bin/env python
import pika
import time
import multiprocessing
import logging                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

def produce(startNo):
#    channel = paramDict["channel"]
#    startNo = paramDict["startNo"]
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.10'))
    channel = connection.channel()
    channel.queue_declare(queue='hello1')
    for inum in range(startNo,startNo+1000):
        channel.basic_publish(exchange='',
                              routing_key='hello1',
                              body='Hello World! '+ str(inum))
        #channel.basic_publish(exchange='',
        #                      routing_key='hello1',
        #                      body='Hello World! 111')
        print " [x] Sent 'Hello World!%s'" % (str(inum))
    connection.close()
    pass


t0 = time.time()

pool = multiprocessing.Pool(20)
paramDict = dict()


for startNo in (1,1001,2001,3001,4001,5001,6001,7001,8001,9001):
    pool.apply_async(produce, [startNo])


pool.close()
pool.join()

t1 = time.time()
print (t1-t0)
