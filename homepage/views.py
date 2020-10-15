from django.shortcuts import render
from posts.models import Post


def index(request):
    try:
        posts = Post.objects.order_by('-id')[:8]
        context = {
            'category_name': 'Последние релизы',
            'posts': posts
        }
    except IndexError:
        context = {
            'category_name': 'Последние релизы',
            'posts': None
        }

    return render(request, 'category/index.html', context)
