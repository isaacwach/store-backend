from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Booking(models.Model):
    types_of_goods = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    exit_date = models.DateTimeField(auto_now_add=True)
    id_storage = models.IntegerField()
    id_client = models.IntegerField()
    id_transport = models.IntegerField()


    def __str__(self):
     return self.types_of_goods

class Transport(models.Model):
    destination = models.CharField(max_length=100)
    delivery_fee = models.IntegerField()
    client_name = models.CharField(max_length=100)
    destination_address = models.AddressField(max_length=200)
    description = models.TextField(max_length=200)
    request_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    phone_no = models.IntegerField()
    id_client = models.IntegerField()
    id_storage = models.IntegerField()
    located = models.CharField(max_length=100)



    def __str__(self):
     return self.client_name
