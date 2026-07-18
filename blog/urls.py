from django.urls import path

from blog.views import index, posts, post

urlpatterns = [
    path("", index, name="index"),
    path("posts", posts , name="posts"),
    path('posts/<slug:slug>', post , name="post"),
]