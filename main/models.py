from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin =models.BooleanField(default=False)
    is_client =models.BooleanField(default=False)  

    def __str__(self):
        return self.username

class Admin(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='employee')
    username =models.CharField(max_length=50)
    email =models.EmailField(max_length=100)
    password =models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Client(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,related_name='client')
    username =models.CharField(max_length=50)
    fullname =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    password =models.CharField(max_length=50)
    phone_number = PhoneField(max_length=15, blank=True)

    def __str__(self):
        return self.username
    
