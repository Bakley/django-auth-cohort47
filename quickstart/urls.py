from django.urls import path
from django.urls.resolvers import URLPattern

from .views import RegistrationAPIView

app_name = 'authentication'

urlpatterns = [
    path('user/signup', RegistrationAPIView.as_view(), name='registration'),
]
