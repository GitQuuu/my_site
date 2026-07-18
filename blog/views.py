from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "blogs/index.html")

def post(request, slug):
    return render(request, "blogs/post.html")

def posts(request):
    return render(request, "blogs/all-posts.html")

