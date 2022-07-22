from django.shortcuts import render
from .models import Blog

def blog(request):
    
    blogs = Blogs.objects.all()

    template = 'blog/blog.html'

    return render(request, template, context)

