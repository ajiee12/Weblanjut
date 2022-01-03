from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from .views import *

urlpatterns= [
    path('', list_users,name='list_users'),
]