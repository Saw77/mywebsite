from django.shortcuts import render
from .models import Blog

def blog_view(request):
    post = Blog.objects.all()
    return render(request, 'blog/blog.html',{'post':post})
