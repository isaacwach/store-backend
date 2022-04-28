from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Booking,Transport
from rest_framework.response import Response
from .serializer import BookingSerializer,TransportSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Booking,Transport
from rest_framework import status
# from .forms import 
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

# def new_book(request):
#     message = 'book it now'
#     return redirect(request,'booking.html',{'message':message})
# def transport(request):
#     message = 'transport'
#     return redirect(request,'transport.html',{'message':message})
class ListBookingView(APIView):

    """
    Provides a get method handler.
    """
    def get(self,request,format=None):
        queryset = Booking.objects.all()
        serializers = BookingSerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = BookingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTransportleView(APIView):
    """
    Provides a get method handler.
    """
    def get(self,request,format=None):

        queryset = Transport.objects.all()
        serializers= TransportSerializer(queryset,many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = TransportSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


