from django.shortcuts import render
from .models import Post


def index(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        context = {
            'category_name': post.title,
            'post': post
        }
    except Post.DoesNotExist:
        context = {
            'category_name': 'По данному запросу ничего не найдено.',
            'posts': None
        }

    return render(request, 'posts/single.html', context)
