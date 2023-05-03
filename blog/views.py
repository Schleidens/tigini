from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    
class new_blog_post(LoginRequiredMixin, View):
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
    
    
#single blog view CBVs
class single_blog_view(View):
    blogModel = blogPost
    template = 'single_blog_view.html'
    
    def get(self, *args, **kwargs):
        blog = get_object_or_404(self.blogModel, slug=kwargs['slug'])
        
        return render(self.request, self.template, {'blog': blog})
    

#edit blog view
class edit_blog(LoginRequiredMixin, View):
    form = blogForm
    model = blogPost
    template = 'edit_blog.html'
    
    def get(self, *args, **kwargs):
        blog = get_object_or_404(self.model, slug=kwargs['slug'])
        
        if blog.author == self.request.user:
            form = self.form(instance=blog)
        else:
            return redirect('home-page')
        
        return render(self.request, self.template, {'form': form})
    
    def post(self, *args, **kwargs):
        blog = get_object_or_404(self.model, slug=kwargs['slug'])
        
        if blog.author == self.request.user:
            form = self.form(self.request.POST, self.request.FILES, instance=blog)
            
            if form.is_valid():
                form.save()
                
                return redirect('single-blog', kwargs['slug'])
                
        else:
            return redirect('home-page')
        
        return render(self.request, self.template, {'form': form})