from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class createUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        

#form for login user view
class loginUserForm(forms.Form):
    username = forms.CharField(max_length=15, label='Username')
    password =  forms.CharField(max_length=30, widget=forms.PasswordInput, label='Password')