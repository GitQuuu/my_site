from datetime import date

from django.shortcuts import render

all_posts = [
   
]
# Create your views here.

def get_date(post):
    return post["date"]
def index(request):
    latest_posts = (Post.objects.all().order_by("-date")[:3])
    return render(request, "blogs/index.html", {
        "posts": latest_posts
    })

def post(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blogs/post-detail.html", {
        "post": identified_post
    } )

def posts(request):
    return render(request, "blogs/all-posts.html", {
        "all_posts": all_posts
    })

