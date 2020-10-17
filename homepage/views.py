from django.shortcuts import render
from posts.models import Post
from .models import Slider


def index(request):
    try:
        posts = Post.objects.order_by('-id')[:8]
        context = {
            'is_homepage': True,
            'category_name': 'Последние релизы',
            'posts': posts,
        }
    except IndexError:
        context = {
            'is_homepage': True,
            'category_name': 'Последние релизы',
            'posts': None
        }

    slides = Slider.objects.all()
    context['slides'] = slides

    return render(request, 'category/index.html', context)
