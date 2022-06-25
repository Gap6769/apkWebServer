from back.models import Messages, dump_sms
import socketserver
from celery import shared_task
import ast


@shared_task
def start_socket():
    HOST, PORT = "0.0.0.0", 505
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

        """$#$  _id:1 thread_id:3 address:45645645f person:null date:1656175264721 date_sent:0 protocol:null read:1 status:-1 type:2 reply_path_present:null subject:null body:Hola service_center:null locked:0 sub_id:1 error_code:-1 creator:com.google.android.apps.messaging seen:1"""
        if "$#$" == content[0:3]:
            content = ast.literal_eval(content[3:])
            dump_sms.objects.create(
                sms_type=content["type"],
                phone_number=content["address"],
                date=content["date"],
                status=content["status"],
                body=content["body"],
            )
            print(content)
        else:
            Messages.objects.create(ip=self.client_address[0], message=self.request.recv(1024).decode())
            print("New Message from {}".format(self.client_address[0]))
            print("Message: {}".format(self.request.recv(1024)))
            # just send back the same data, but upper-cased
