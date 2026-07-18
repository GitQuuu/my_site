from django.urls import path

from blog.views import index, posts, post

urlpatterns = [
    path("", index, name="index"),
    path("blogs", posts , name="blogs"),
    path('blogs/<slug:slug>', post , name="post"),
]