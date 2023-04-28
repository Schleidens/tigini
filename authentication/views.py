from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from authentication.forms import createUserForm

# Create your views here.


#view for signup CBVs
class user_creation_view(View):
    form = createUserForm
    template = 'user_creation_view.html'
    
    def get(self, request):
        form = self.form()
        
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.form(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home-page')
        return render(request, self.template, {'form': form})