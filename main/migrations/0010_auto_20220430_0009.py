# Generated by Django 3.2.10 on 2022-04-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_0003_transport_booking_0008_alter_storage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='transport',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
