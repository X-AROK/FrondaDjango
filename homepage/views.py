from django.shortcuts import render
from django.db.models import Max
from posts.models import Post
from posts.models import Video
from category.models import Category
from .models import Slider


def index(request):
    categories = {}
    try:
        for category in Category.objects.all():
            if not category.show_on_homepage:
                continue

            categories[category.display_name] = Post.objects.filter(category=category).annotate(
                upload_time=Max('video__upload_time')).order_by('-upload_time')[:4]
        last_releases = Post.objects.order_by('-id')[:8]
        context = {
            'last_releases': last_releases,
            'categories': categories,
        }
    except IndexError:
        context = {
            'posts': None
        }

    slides = Slider.objects.all()
    context['slides'] = slides

    return render(request, 'homepage/index.html', context)
