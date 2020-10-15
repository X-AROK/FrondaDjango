from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category
from posts.models import Post


def index(request, name):
    try:
        category = Category.objects.get(name=name)
        posts = Post.objects.filter(category=category).order_by('title')

        paginator = Paginator(posts, 12)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

        context = {
            'category_name': category.display_name,
            'posts': posts,
        }
    except Category.DoesNotExist:
        context = {
            'category_name': "По данному запросу ничего не найдено."
        }

    return render(request, 'category/index.html', context)
