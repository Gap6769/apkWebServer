from django.contrib import admin
from back.models import Messages, apkPayload
# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('date', 'ip', 'message')
    list_filter = ('date','ip')
    search_fields = ('message', 'ip', 'date')

class apkPayloadAdmin(admin.ModelAdmin):
    list_display = ('apk_name', 'download', 'port')
    list_filter = ('apk_name','port')
    search_fields = ('apk_name', 'port')

admin.site.register(Messages, MessagesAdmin)
admin.site.register(apkPayload, apkPayloadAdmin)