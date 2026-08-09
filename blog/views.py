from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from blog.models import Post

# Create your views here.

class StartingPageView(ListView):
    model = Post
    template_name = "blogs/index.html"
    context_object_name = "posts"
    ordering = ("-date",)

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data



def post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blogs/post-detail.html", {
        "post": identified_post,
        "post_tags" : identified_post.tags.all()
    } )

def posts(request):
    return render(request, "blogs/all-posts.html", {
        "all_posts": Post.objects.all().order_by("-date")
    })

