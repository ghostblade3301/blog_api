from django.urls import path

from .views import index, post_detail, group_posts


app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('group/<slug>/', group_posts, name='group_posts'),
]
