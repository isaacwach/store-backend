
from wsgiref import validate
from rest_framework import serializers
from .models import Admin,Client,Storage, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model =User
        fields =['username','email','is_admin']

class AdminSignupSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model =User
        fields =['username','email','password','password2']
        extra_kwargs ={
            'password':{'write_only': True}
        }

    def save(self,**kwargs):
        user =User(
            username =self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password'],
        # password2 =self.validated_data['password2']
        # if  password !=password2:
        #     raise serializers.ValidationError({"error":"password does not match"})

        user.set_password(password) 
        user.is_admin =True 
        user.save() 
        Admin.objects.create(user=user) 
        return user
          


class ClientSignupSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model =User
        fields =['username','email','password','password2']

        extra_kwargs ={
            'password':{'write_only':True}
        }

    
    def saveClient(self,**kwargs):
        user =User(
            username =self.validated_data['username'],
            fullname=self.validated_data['fullname'],
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
        )
        password=self.validated_data['password'],
        # password2 =self.validated_data['password2']
        # if  password !=password2:
        #     raise serializers.ValidationError({"error":"password does not match"})

        user.set_password(password) 
        user.is_client =True 
        user.save() 
        Client.objects.create(user=user) 

        return user  
        
          

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Storage
        fields =['id','description','size','price','status','categories']

        

  