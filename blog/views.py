from django.shortcuts import render
from blog.models import Blog

def index(request):
    return render(request, 'index.html', {})
