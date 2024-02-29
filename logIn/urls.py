from django.urls import path
from . import  views

urlpatterns=[
    path("logInUsers" , views.logInUsers,name='logInUsers') , 
    path("logInDoctors" , views.logInDoctors,name='logInDoctors')     
]