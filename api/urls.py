from django.urls import path
from api.views import *

app_name = 'main'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('secret/', secret, name='secret'),
]