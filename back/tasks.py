from back.models import Messages, dump_sms
import socketserver

from celery import shared_task

import json
import re
import datetime


@shared_task
def start_socket():
    HOST, PORT = "0.0.0.0", 506
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

        content = self.request.recv(12288).decode()
        ip = self.client_address[0]
        if "_id" in content and "thread_id" in content and "address" in content:
            try:
                content = json.loads(content.replace("$#$ ", "").replace("'", '"').replace("\n", ""))
                print(content.keys())
            except:
                content = json.loads(
                    ",".join(content.replace("$#$ ", "").replace("'", '"').replace("\n", "").split(",", 10))
                )
            sms = dump_sms.objects.filter(
                body=content["body"],
                date=datetime.datetime.fromtimestamp(int(content["date"]) / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
            )
            if sms:
                return
            dump_sms.objects.create(
                sms_type="ENVIADO" if content["type"] == "1" else "RECIBIDO",
                ip=ip,
                phone_number=content["address"],
                date=datetime.datetime.fromtimestamp(int(content["date"]) / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
                status=content["status"],
                body=content["body"],
            )
            print(content["body"])
        elif "phone" in content and "body" in content:
            content = json.loads(content.replace("$#$ ", "").replace("'", '"').replace("\n", ""))
            dump_sms.objects.create(
                sms_type="RECIBIDO",
                ip=ip,
                phone_number=content["phone"],
                date=datetime.datetime.now(),
                body=content["body"],
            )
        else:
            content = content.replace("'", '"').replace("\n", "")
            print("New Message from {}".format(self.client_address[0]))
            print("Message: {}".format(content))
            last_input = Messages.objects.filter(ip=ip).last()
            if last_input and last_input.date.strftime("%Y%m%d") == datetime.datetime.now().strftime("%Y%m%d"):
                if last_input.message == content[0 : len(content)]:
                    return
                elif last_input.message == content[0 : len(content) - 1]:
                    last_input.message = content
                    last_input.save()
                    return

            Messages.objects.create(ip=self.client_address[0], message=content)
