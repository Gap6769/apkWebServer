# Generated by Django 4.0.5 on 2022-06-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0006_alter_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(),
        ),
    ]
