from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ListBookingView,ListTransportleView

urlpatterns=[
    path('api/booking/', ListBookingView.as_view(), name="booking-all"),
    path('api/transport/', ListTransportleView.as_view(), name="transport-all"),
  
    
]


  