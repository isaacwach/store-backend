# Generated by Django 4.0.4 on 2022-04-27 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('delivery_fee', models.IntegerField()),
                ('client_name', models.CharField(max_length=100)),
                ('destination_address', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('phone_no', models.IntegerField()),
                ('located', models.CharField(max_length=100)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainclient', to='main.client')),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='main.storage')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_goods', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('exit_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='main.client')),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainstorage', to='main.storage')),
                ('transport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintransport', to='main.transport')),
            ],
        ),
    ]
