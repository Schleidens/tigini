from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import blogForm
from .models import blogPost

# Create your views here.


class home_page(View):
    model = blogPost
    template = 'home_page.html'
    
    def get(self, request):
        blogs = self.model.objects.order_by('-date')
        
        return render(request, self.template, {'blogs': blogs})
    
    
class new_blog_post(View):
    form = blogForm
    template = 'new_blog_post.html'
    
    def get(self, request):
        form = self.form()
        
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = self.form(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)
            
            blog.author = request.user
            blog.save()
            
            return redirect('home-page')
            
        return render(request, self.template, {'form': form})