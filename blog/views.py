from django.shortcuts import render
from .models import Blog

def blog(request):
    
    blogs = Blog.objects.all()

    template = 'blog/blog.html'

    return render(request, template)

