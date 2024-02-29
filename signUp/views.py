from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Doctor , User  # Import the Doctor form
import json 


def signUpUsers(request):
    if request.method == 'GET':
        form = User(request.GET)
        if form.is_valid():
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            birth_date = form.cleaned_data['birth_date']
            telephone = form.cleaned_data['telephone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Execute SQL queries to insert data into your database
            # Replace the placeholders with your actual SQL queries
            sql_query = f"INSERT INTO your_table (first_name, last_name, birth_date, telephone, password) VALUES ('{first_name}', '{last_name}', '{birth_date}', '{telephone}', '{password}')"
            # Execute the SQL query using your database connection
            # For example:
            # cursor.execute(sql_query)
            # connection.commit()
            
            f = open("data.txt" , "w")
            f.write( str(form.cleaned_data) ) 
            f.close()

            return HttpResponse("User signed up successfully!")  # or redirect to another page
    else:
        form = User()
        print("Un validation")
    return render(request, 'signup.html', {
            "form": form,
            "image_url": "static/img/doctor.jpg",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        })




def signUpDoctor(request):
    if request.method == 'POST':
        form = Doctor(request.POST)
        if form.is_valid():
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            birth_date = form.cleaned_data['birth_date']
            telephone = form.cleaned_data['telephone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            specialization = form.cleaned_data['specialization']


            print(first_name ,last_name , birth_date , telephone , password , confirm_password  )
            return HttpResponse("Doctor signed up successfully!")  # or redirect to another page
    else:
        form = Doctor()
    return render(request, 'signup.html', {
            "form": form,
            "image_url": "static/img/doctor.jpg",
            "date": datetime.today().strftime("%A, %B %d, %Y"),
        })


