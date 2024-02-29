from django import forms


class User(forms.Form):
    name = forms.CharField(
        label="Phone Number or Id",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "name"}
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 
                   "placeholder": "password", 
                   "id": "password", 
                   'type':"password" 
                   }
        ),
    )


class Doctor(forms.Form):
    name = forms.CharField(
        label="Phone Number or Id",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "name"}
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 
                   "placeholder": "password", 
                   "id": "password", 
                   'type':"password" 
                   }
        ),
    )