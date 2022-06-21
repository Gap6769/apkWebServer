# Generated by Django 4.0.5 on 2022-06-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_messages_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='apkPayload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apk_name', models.CharField(blank=True, default='', max_length=100)),
                ('apk_path', models.CharField(blank=True, default='', max_length=100)),
                ('port', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
