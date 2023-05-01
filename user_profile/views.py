from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

from .forms import editProfile, deleteProfileForm

# Create your views here.

class user_profile(LoginRequiredMixin ,View):
    template = 'user_profile.html'
    
    def get(self, request):
        profile = request.user
        return render(self.request, self.template, {'profile': profile})
    
    
#edit profile view CBVs
class edit_user_profile(LoginRequiredMixin, View):
    edit_form = editProfile
    template = 'edit_user_profile.html'
    
    def get(self, request):
        form = self.edit_form(instance=request.user)
        
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.edit_form(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            
            return redirect('profile')
        
        return render(request, self.template, {'form': form})
    
    
#user delete profile view CBVs
class delete_profile(LoginRequiredMixin, View):
    delete_form = deleteProfileForm
    template = 'delete_profile.html'
    
    def get(self, request):
        form = self.delete_form()
        
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        user = request.user
        user.delete()
        
        return redirect('signup')