
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http  import Http404
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Admin,Client,Storage
from .serializers import AdminSignupSerializer,ClientSignupSerializer,StorageSerializer, UserSerializer
from rest_framework import status,generics 
from .permissions import IsAdminOrReadOnly,isAdminUser,isClientUser
from main import serializers

from main import permissions

# Create your views here.


class AdminSignup(generics.GenericAPIView):
    serializer_class = AdminSignupSerializer
    def post(self, request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        return Response ({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"Account created succesfully"    
        })
      

     

class ClientSignup(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer
    def post(self, request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        return Response ({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"Account created succesfully"    
        })   
            
class StorageApiView(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_storage =Storage.objects.all()
        serializers =StorageSerializer(all_storage, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = StorageSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class StorageDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_storage(self, pk):
        try:
            return Storage.objects.get(pk=pk)
        except Storage.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        unit = self.get_storage(pk)
        serializers = StorageSerializer(unit)
        return Response(serializers.data)


    def put(self, request, pk, format=None):
        merch = self.get_storage(pk)
        serializers = StorageSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        merch = self.get_storage(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']

        token, created=Token.objects.get_or_create(user=user)
        return Response({
             'token': token.key,
             'user_id': user.pk,
             'is_admin':user.is_admin,
             'is_client':user.is_client
        })
    
class Logout(APIView):
    def post (self,request,format=None):
        request.auth.delete()
        return  Response(status=status.HTTP_200_OK)

class AdminOnlyView(generics.GenericAPIView):
    permission_class =[permissions.isAdminUser]  
    serializer_class =UserSerializer

    def get_object(self):
        return self.request.user   


class ClientOnlyView(generics.GenericAPIView):
    permission_class =[permissions.isClientUser]  
    serializer_class =UserSerializer

    def get_object(self):
        return self.request.user      

