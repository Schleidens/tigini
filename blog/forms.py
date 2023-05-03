from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput
from .models import blogPost


class blogForm(forms.ModelForm):
    
    class Meta:
        model =  blogPost
        fields = ['cover', 'title', 'content']
        
        widgets = {
            'cover' : ClearableFileInput(attrs={
                'class' : 'form-control',
                'multiple' : False
            }),
            
            'title' : TextInput(attrs={
                'placeholder' : 'Blog title',
                'class' : 'form-control'
            }),
            
            'content' : Textarea(attrs={
                'placeholder' : 'Write your blog content here',
                'class' : 'form-control'
            })
        }