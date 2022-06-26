from django.core.management.base import BaseCommand, CommandError
from back.tasks import start_socket


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("starting socket", ending="\n")
        start_socket.delay()
        self.stdout.write("socket started", ending="\n")
