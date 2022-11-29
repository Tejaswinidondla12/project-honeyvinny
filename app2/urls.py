from django.urls import path
from app2.views import *
app_name='vinny'
urlpatterns = [
    path('app2first/',app2first,name='app2first'),
    path('app2second/',app2second,name='app2second')
]