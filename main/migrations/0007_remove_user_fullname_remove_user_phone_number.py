# Generated by Django 4.0.3 on 2022-04-28 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_fullname_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
