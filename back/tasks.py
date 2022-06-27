from back.models import Messages, dump_sms
import socketserver

from celery import shared_task

import json
import re
import datetime


@shared_task
def start_socket():
    HOST, PORT = "0.0.0.0", 510
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client

        content = self.request.recv(1024).decode()
        ip = self.client_address[0]
        if "$#$" == content[0:3]:
            content = json.loads(content.replace("$#$ ", "").replace("'", '"').replace("\n", " "))
            dump_sms.objects.create(
                sms_type=content["type"],
                phone_number=content["address"],
                date=datetime.datetime.fromtimestamp(int(content["date"]) / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
                status=content["status"],
                body=content["body"],
            )
            print(content["body"])
        else:
            # Messages.objects.create(ip=self.client_address[0], message=self.request.recv(1024).decode())
            print("New Message from {}".format(self.client_address[0]))
            print("Message: {}".format(self.request.recv(1024)))
            Messages.objects.create(ip=self.client_address[0], message=self.request.recv(1024).decode())

            # just send back the same data, but upper-cased
