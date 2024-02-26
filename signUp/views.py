from django.shortcuts import render
from django.forms import ModelForm, Textarea
from django import forms
from signUp.models import *



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')


def contact(request):

    #contact_form = ContactForm()
    #contact_form = ContactForm2()
    
    contact_form = ContactForm2()
    date_gender = SimpleForm()
    comment_form = CommentForm()
    
    #return render(request,'myform/conctact.html',{'contact_form':contact_form})

    return render(request,'contact.html',
                  {'contact_form':contact_form,
                   'date_gender':date_gender , 
                   'comment_form':comment_form
                   } 
                  )