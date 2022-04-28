from rest_framework import serializers
from .models import Booking, Transport


# Convert Django models to JSON objects and vice-versa. 
from rest_framework import serializers
from .models import Booking, Transport


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("types_of_goods", "start_date", "exit_date")

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ("destination", "delivery_fee", "client_name", "destination_address", "description", "request_date", "delivery_date","phone_no","located")