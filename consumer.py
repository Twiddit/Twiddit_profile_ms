#!/usr/bin/env python
import pika, sys, os, requests

def connectConsumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages.')
    channel.start_consuming()
