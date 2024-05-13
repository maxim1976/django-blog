# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogIndex.as_view(), name="blog_index"),
    path("post/<int:pk>/", views.BlogDetail.as_view(), name="blog_detail"),
    path("category/<category>/", views.BlogCategory.as_view(), name="blog_category"),
    path("post/new/", views.AddPostView.as_view(), name="add_post"),
    path("post/featured/", views.FeaturedDetailView.as_view(), name="post_featured"),
    path("post/<int:pk>/edit/", views.UpdatePostView.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view(), name="delete_post"),
] 