from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

def about(request):
    return render(request, 'blog/about.html', {})

def readblog(request, blog_id):
    blogs = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/readblog.html', {'blogs': blogs})
