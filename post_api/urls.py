from django.contrib import admin
from django.urls import path
from .views.post_view import PostView


urlpatterns = [
    path('get_all_post', PostView.as_view({"get":"get_all_post"})),
    path('get_post_detail', PostView.as_view({"get":"get_post_detail"})),
    path('post_article', PostView.as_view({"post":"post_article"})),
    path('post_delete_soft', PostView.as_view({"post":"post_delete_soft"})),
]
