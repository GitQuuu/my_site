from multiprocessing import context

from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
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


class SinglePostView(DetailView):
    model = Post
    template_name = "blogs/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

class AllPostsView(ListView):
    model = Post
    template_name = "blogs/all-posts.html"
    context_object_name = "all_posts"
    ordering = ("-date",)

