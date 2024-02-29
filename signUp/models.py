from django.contrib import admin
from django.shortcuts import render
from django import forms
from django.forms import models
from datetime import datetime


class User(forms.Form):

    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    birth_date = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    telephone = forms.CharField(
        label="Telephone",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "+229 00 00 00 00",
                "pattern": "\+229 [0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2}",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )




class Doctor(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    birth_date = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    telephone = forms.CharField(
        label="Telephone",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "+229 00 00 00 00",
                "pattern": "\+229 [0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2}",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )
    specialization = forms.CharField(
        label="Specialization",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Specialization"}
        ),
    )




"""

BIRTH_YEAR_CHOICES = ("1999", "2000", "2001")
GENDER_CHOICES = (("m", "Male"), ("f", "Female"))
FAVORITE_COLORS_CHOICES = (("blue", "Blue"), ("green", "Green"), ("black", "Black"))


# Sans ModelForm
class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)


####### Form with Date and Sex choice
class SimpleForm(forms.Form):
    birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    # birth_year = DateField(widget=SelectDateWidget())

    gender = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    favorite_colors = forms.MultipleChoiceField(
        required=False, widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES
    )


class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "special"}))

    url = forms.URLField(initial="Votre lien", label="Lien")
    comment = forms.CharField(widget=forms.TextInput(attrs={"size": "40"}))
"""