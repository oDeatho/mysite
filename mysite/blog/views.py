from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', { 'posts': posts})

