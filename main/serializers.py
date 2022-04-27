from dataclasses import fields
from rest_framework import serializers
from .models import Admin,Client,Storage

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model =Admin
        fields =('username','email','password')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Client
        fields =('username','fullname','email','phone_number','password')

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Storage
        fields =('description','size','price','image','status','categories')

