from django.urls import path

from blog import views
from blog.views import posts, post

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("blogs", posts , name="all-posts"),
    path('blogs/<slug:slug>', post , name="post-detail-page"),
]