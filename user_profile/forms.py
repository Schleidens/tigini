from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput

from django.contrib.auth import get_user_model


class editProfile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'bio', 'profile_photo']
        
        #specify widget for each input
        widgets = {
            'username' : TextInput(attrs={
                'class' : 'form-control'
            }),
            
            'first_name' : TextInput(attrs={
                'class' : 'form-control'
            }),
            
            'last_name' : TextInput(attrs={
                'class' : 'form-control'
            }),
            
            'bio' : Textarea(attrs={
                'class' : 'form-control'
            }),
            
            'profile_photo' : ClearableFileInput(attrs={
                'multiple' : False,
                'class' : 'form-control'
            })
        }
        
