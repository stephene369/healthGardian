from django.urls import path
from . import  views

urlpatterns=[
    path("homePatient" , views.home,name='homePatient') , 
]