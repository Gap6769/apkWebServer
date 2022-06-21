from platform import release
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from back.views import testViews
from back.views import meterpreter_payload_views

urlpatterns = [
    path("list/", testViews.ReleaseView.as_view()),
    path("get_apk_file/<str:apk_name>/", meterpreter_payload_views.get_apk_file),
]