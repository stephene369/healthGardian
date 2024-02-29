from django.urls import path
from . import  views

urlpatterns=[
    path("signUpUsers" , views.signUpUsers,name='signupUsers') , 
    path("signUpDoctors" , views.signUpDoctor,name='signupDoctor')     
]