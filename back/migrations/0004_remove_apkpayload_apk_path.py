# Generated by Django 4.0.5 on 2022-06-21 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_apkpayload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apkpayload',
            name='apk_path',
        ),
    ]
