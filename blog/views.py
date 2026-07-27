from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blogs/index.html", {
        "posts": latest_posts
    })

def post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blogs/post-detail.html", {
        "post": identified_post
    } )

def posts(request):
    return render(request, "blogs/all-posts.html", {
        "all_posts": Post.objects.all().order_by("-date")
    })

