

from django.contrib.auth.models import User


from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Client(models.Model):
    user =models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='client')
    username =models.CharField(max_length=50,default='felo')
    
    email =models.EmailField(max_length=100,default='kurgatfelo@gmail.com')
   
    

    def __str__(self):
        return self.username

class Storage(models.Model):

    description =models.TextField(max_length=200)
    size =models.IntegerField(blank=True,default='0')
    price =models.FloatField(default=0, blank=True)
    image = CloudinaryField('image',blank=True)

    status =models.CharField(max_length=40)
    categories =models.CharField(max_length=50)
    
    def __str__(self):

        return self.categories
      

class Transport(models.Model):
    destination = models.CharField(max_length=100)
    delivery_fee = models.IntegerField()
    client_name = models.CharField(max_length=100)
    destination_address = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    request_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField()
    phone_no = models.IntegerField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE, null=True, related_name='mainclient')
    storage = models.ForeignKey(Storage,on_delete=models.CASCADE, null=True, related_name='storage')
    pickup_location = models.CharField(max_length=100)



    def __str__(self):
     return self.client_name

class Booking(models.Model):
    types_of_goods = models.CharField(max_length=100)
    start_date = models.DateField()
    exit_date  = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE, null=True, related_name='client')
    storage = models.ForeignKey(Storage,on_delete=models.CASCADE, null=True, related_name='mainstorage')
    transport = models.ForeignKey(Transport,on_delete=models.CASCADE, null=True, related_name='maintransport')
    description= models.TextField(default="desc")
    client_name = models.CharField(max_length=100,default="moringa")
    price = models.FloatField(default=1000)


    def __str__(self):
     return self.types_of_goods





class User(AbstractUser):
    is_admin =models.BooleanField(default=False)
    is_client =models.BooleanField(default=False)
    

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance) 

class Admin(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='employee')
    username =models.CharField(max_length=50,blank=True,null=True)
    email =models.EmailField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.username







