from django.urls import path
from app1.views import *
app_name='honey'
urlpatterns = [
    path('app1first/',app1first,name='app1first'),
    path('app1second/',app1second,name='app2second'),
]