from back.models import Messages
import socketserver
from celery import shared_task


@shared_task
def start_socket():
    HOST, PORT = "0.0.0.0", 9999
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
        Messages.objects.create(ip=self.client_address[0], message=self.request.recv(1024).decode())
        print("New Message from {}".format(self.client_address[0]))
        print("Message: {}".format(self.request.recv(1024)))
        # just send back the same data, but upper-cased
