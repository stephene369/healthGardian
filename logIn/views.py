from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Doctor
from datetime import datetime
from modules.sqlRequest import SignUp , LogIn
# Create your views here.




def logInUsers(request) : 
    if request.method == "GET":
        form = User(request.GET)
        if form.is_valid(): 
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            login = LogIn()
            if login.logIn(id_or_tel=name, password=password) :
                return HttpResponse (f"{name} accept")

            else : 
                return HttpResponse (f"{name} reject")


    else : 
        form = User()
     
    return render(
            request , 
            "login.html" , 
        {
            "form": form,
            "image_url": "static/img/user.png",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        },
    )




def logInDoctors(request) : 
    if request.method == "GET":
        form = Doctor(request.GET)
        if form.is_valid(): 
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            login = LogIn()
            if login.logIn(id_or_tel=name, password=password) :
                return HttpResponse (f"{name} accept")

            else : 
                return HttpResponse (f"{name} reject")

    else : 
        form = Doctor()

    return render(
            request , 
            "login.html" , 
        {
            "form": form,
            "image_url": "static/img/doctor.jpg",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        },
    )
