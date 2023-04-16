from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    word = 'Слово циклом'
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts,
        'word': word,
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'posts/post_detail.html'
    title = 'Страница поста под номером:'
    context = {
        'title': title,
        'pk': pk,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    title = 'Все посты группы'
    context = {
        'title': title,
        'slug': slug,
    }
    return render(request, template, context)
