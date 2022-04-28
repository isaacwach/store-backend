from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^api/signup/admin/$',views.AdminSignup.as_view()),
    re_path(r'^api/signup/client/$',views.ClientSignup.as_view()),
    re_path(r'^api/storage/unit/$',views.StorageApiView.as_view()),
    re_path(r'api/unit/unit-id/(?P<pk>[0-9]+)/$',views.StorageDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)