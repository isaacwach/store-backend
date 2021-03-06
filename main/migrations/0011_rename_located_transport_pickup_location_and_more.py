# Generated by Django 4.0.4 on 2022-04-30 08:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_client_fullname_remove_client_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='located',
            new_name='pickup_location',
        ),
        migrations.AddField(
            model_name='booking',
            name='client_name',
            field=models.CharField(default='moringa', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='description',
            field=models.TextField(default='desc'),
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.FloatField(default=1000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='exit_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='storage',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
