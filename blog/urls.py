from django.urls import path

from blog.views import index, posts, post

urlpatterns = [
    path("", index, name="starting-page"),
    path("blogs", posts , name="all-posts"),
    path('blogs/<slug:slug>', post , name="post-detail-page"),
]