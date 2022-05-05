from rest_framework import serializers
from main.models import Admin,Client,Storage, User,Booking, Transport


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("types_of_goods", "start_date", "exit_date","description","client_name","price")

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ("destination", "delivery_fee", "client_name", "destination_address", "description", "request_date", "delivery_date","phone_no","located")
class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Storage
        fields =['id','description','size','price','status','categories']

        
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_admin","is_client"]
class AdminSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
    class Meta:
        model = User
        fields=['username', 'email', 'password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    #changed this function
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_tm=True
        user.save()
        Admin.objects.create(user=user)
        return user
class ClientSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
    class Meta:
        model = User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    #changed this function
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_client=True
        user.save()
        Client.objects.create(user=user)
        return user