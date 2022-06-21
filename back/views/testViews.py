
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from django.conf import settings
from rest_framework import permissions
import datetime
from datetime import timedelta
from rest_framework.response import Response

class ReleaseView(APIView):
    def post(self, request):
        # Get the release name from the request
        print('hello world')
        return Response({"message": "Hello, world!"})


