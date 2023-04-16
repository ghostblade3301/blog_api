from django.shortcuts import render, get_object_or_404
from .models import Post, Group


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
    group = get_object_or_404(Group, slug=slug)
    group_posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_posts.html'
    context = {
        'group_posts': group_posts,
        'group': group,
    }
    return render(request, template, context)
