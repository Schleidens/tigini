from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from random import randint

from .forms import blogForm, draftForm, deleteBlogForm
from .models import blogPost

# Create your views here.


class home_page(View):
    model = blogPost
    template = 'home_page.html'
    
    def get(self, request):
        blogs = self.model.objects.filter(draft=False).order_by('-created_date')
        
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
            
            return redirect('single-blog', blog.slug)
            
        return render(request, self.template, {'form': form})
    
    
#single blog view CBVs
class single_blog_view(View):
    blogModel = blogPost
    draft_form = draftForm
    delete_form = deleteBlogForm
    template = 'single_blog_view.html'
    
    def get(self, *args, **kwargs):
        blog = get_object_or_404(self.blogModel, slug=kwargs['slug'])
        
        #check if blog is not draft and if current user is the owner
        if blog.draft == True and blog.author != self.request.user:
            return redirect('home-page')
            
        draft_form = self.draft_form()
        form = self.delete_form()
        
        context = {
            'blog' : blog,
            'draft_form' : draft_form,
            'form' : form
        }
        
        return render(self.request, self.template, context=context)
    
    #for handle the delete blog request
    def post(self, *args, **kwargs):
        blog = get_object_or_404(self.blogModel, slug=kwargs['slug'])
        
        #add draft_form outside the func for scope and prevent referenced before assignment error
        draft_form = self.draft_form(self.request.POST)
        
        #only the current user can make a post request else it will be redirected
        if blog.author == self.request.user:
            
            #handle draft form request
            if 'draft' in self.request.POST:
                draft_form = self.draft_form(self.request.POST)
                
                if draft_form.is_valid():
                    blog.draft = not blog.draft
                    blog.save()
                    
                    return redirect('home-page')
            
            #handle delete form request
            if 'delete' in self.request.POST:
                form = self.delete_form(self.request.POST)
                
                if form.is_valid():
                    blog.delete()
                    
                    return redirect('home-page')
                    
        #redirect if the user trying to make a post request is not the owner            
        else:
            return redirect('home-page')
        
        context = {
            'blog' : blog,
            'draft_form' : draft_form,
        }
        
        return render(self.request, self.template, context=context)
            
    

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


#user logged in blog view CBVs
class user_blog(LoginRequiredMixin, View):
    blog_model = blogPost
    template = 'user_blog.html'
    
    def get(self, request):
        blogs = self.blog_model.objects.filter(author=request.user).order_by('-created_date')
        
        return render(request, self.template, {'blogs': blogs})