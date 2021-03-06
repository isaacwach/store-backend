# Generated by Django 4.0.3 on 2022-04-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrption', models.TextField(max_length=200)),
                ('size', models.IntegerField(blank=True, default='0')),
                ('price', models.FloatField(blank=True, default=0)),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.CharField(max_length=40)),
                ('categories', models.CharField(max_length=50)),
            ],
        ),
    ]
