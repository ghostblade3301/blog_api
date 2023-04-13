from django.urls import path

from .views import index, post_detail, group_posts


urlpatterns = [
    path('', index),
    path('posts/<int:pk>/', post_detail),
    path('group/<slug>/', group_posts),
]
