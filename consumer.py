#!/usr/bin/env python
import pika, sys, os, requests

def connectConsumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get('RABBITMQ_IP')))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    def callback(ch, method, properties, body):
        data = body.decode()
        data = data.split(".")
        data = {'followerId': data[0], 'followedId':data[1]}
        url = "http://34.138.201.211:7777/notifications/createNotification/"
        requests.post(url, json=data)
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages.')
    channel.start_consuming()
