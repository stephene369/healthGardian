from django.contrib import admin
from django.shortcuts import render
from django.forms import ModelForm , models
from django import forms
from django.forms.fields import (DateField, ChoiceField,
                MultipleChoiceField, CharField, EmailField)
from django.forms.widgets import ( RadioSelect, CheckboxSelectMultiple, 
                SelectDateWidget)


from django.db import models 


class Contact(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)



BIRTH_YEAR_CHOICES = ('1999', '2000', '2001')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                        ('green', 'Green'),
                        ('black', 'Black'))



# Sans ModelForm
class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)



####### Form with Date and Sex choice
class SimpleForm(forms.Form):
    birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    #birth_year = DateField(widget=SelectDateWidget())
    
    gender = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    favorite_colors = forms.MultipleChoiceField(required=False,
    widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)


class CommentForm(forms.Form):
    name = forms.CharField(
                widget=forms.TextInput(attrs={'class':'special'}))
    
    url = forms.URLField(initial="Votre lien" , label="Lien" )
    comment = forms.CharField(
                widget=forms.TextInput(attrs={'size':'40'}))
    
    
