from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ListBookingView,ListTransportleView

urlpatterns=[
    re_path(r'^api/signup/admin/$',views.AdminSignup.as_view()),
    re_path(r'^api/signup/client/$',views.ClientSignup.as_view()),
    re_path(r'^api/storage/unit/$',views.StorageApiView.as_view()),
    re_path(r'api/login/',views.CustomAuthToken.as_view()),
    re_path(r'api/logout/',views.Logout.as_view()),
    re_path(r'api/admin/dashboard/',views.AdminOnlyView.as_view),
    re_path(r'api/client/dashboard/',views.ClientOnlyView.as_view()),
    re_path(r'api/unit/unit-id/(?P<pk>[0-9]+)/$',views.StorageDescription.as_view()),
    path('api/booking/', ListBookingView.as_view(), name="booking-all"),
    path('api/transport/', ListTransportleView.as_view(), name="transport-all"),
  
    
]


  