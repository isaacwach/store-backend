
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


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


class Client(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='client')
    username =models.CharField(max_length=50,blank=True,null=True)
    fullname =models.CharField(max_length=100,blank=True,null=True)
    email =models.EmailField(max_length=100,blank=True,null=True)
    phone_number = PhoneField(max_length=15, blank=True,null=True)

    def __str__(self):
        return self.username



class Storage(models.Model):
    description =models.TextField(max_length=200)
    size =models.IntegerField(blank=True,default='0')
    price =models.FloatField(default=0, blank=True)
    image = models.ImageField(upload_to='images/')
    status =models.CharField(max_length=40)
    categories =models.CharField(max_length=50)
    
    def __str__(self):
        return self.categories


    