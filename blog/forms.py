from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput, CheckboxInput
from .models import blogPost


class blogForm(forms.ModelForm):
    
    class Meta:
        model =  blogPost
        fields = ['cover', 'title', 'content', 'draft']
        
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
            }),
            
            'draft' : CheckboxInput(attrs={
                'class' : 'form-check-input'
            })
        }
        
        
#form for draft button
class draftForm(forms.Form):
    draft = forms.BooleanField(widget=forms.HiddenInput, initial=True)
        
        
class deleteBlogForm(forms.Form):
    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)