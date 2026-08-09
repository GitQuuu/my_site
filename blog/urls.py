from django.urls import path

from blog import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("blogs", views.AllPostsView.as_view() , name="all-posts"),
    path('blogs/<slug:slug>', views.SinglePostView.as_view() , name="post-detail-page"),
]