from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.text import slugify
from random import randint

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
    blogModel = blogPost
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
            
            slug = slugify(blog.title)
            
            if self.blogModel.objects.filter(slug=slug).exists():
                unique_slug = slug + "-" + str(randint(1000, 9999))
            else:
                unique_slug = slug
            
            blog.slug = unique_slug
            blog.save()
            
            return redirect('home-page')
            
        return render(request, self.template, {'form': form})