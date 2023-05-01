from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

# Create your views here.

class user_profile(LoginRequiredMixin ,View):
    template = 'user_profile.html'
    
    def get(self, request):
        profile = request.user
        return render(self.request, self.template, {'profile': profile})