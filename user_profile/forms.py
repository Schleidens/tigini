from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput
from django.contrib.auth.forms import PasswordChangeForm

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
        

#change password form
class changePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(changePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your old password'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your new password'})
        

class deleteProfileForm(forms.Form):
    delete_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True)
        
