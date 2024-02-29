from django.shortcuts import render 

from django.http import HttpResponse
from datetime import datetime

from .models import Doctor, User  # Import the Doctor form

from modules.sqlRequest import SignUp 


def signUpUsers(request):
    if request.method == "GET":
        form = User(request.GET)
        if form.is_valid():
            # Get form data
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            birth_date = form.cleaned_data["birth_date"].strftime("%d-%m-%Y")
            telephone = form.cleaned_data["telephone"]
            password = form.cleaned_data["password"]
            specialization = 'patient'

            ## SIGNINP UP 
            signup = SignUp()
            if signup.signUp(first_name=first_name, 
                            last_name=last_name,
                            birth_date=birth_date,
                            telephone=telephone,
                            password=password,
                            specialization=specialization ) : 

                return HttpResponse("User signed up successfully!")

            else :
                return HttpResponse("This phone is already token")
            # or redirect to another page

    else:
        form = User()

    return render(
        request,
        "signup.html",
        {
            "form": form,
            "image_url": "static/img/user.png",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        },
    )




def signUpDoctor(request):
    if request.method == "POST":
        form = Doctor(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            birth_date = form.cleaned_data["birth_date"].strftime("%d-%m-%Y")
            telephone = form.cleaned_data["telephone"]
            password = form.cleaned_data["password"]
            specialization = form.cleaned_data['specialization']


            ## Sign u
            signup = SignUp()
            signup.signUp(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                telephone=telephone,
                password=password,
                specialization=specialization
            )

            return HttpResponse("User signed up successfully!")

    else:
        form = Doctor()

    return render(
        request,
        "signup.html",
        {
            "form": form,
            "image_url": "static/img/doctor.jpg",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        },
    )