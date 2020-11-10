from django.shortcuts import render
from posts.models import Post
from django.core.paginator import Paginator
from FrondaDjango.settings import DEBUG


def index(request):
    search = request.GET.get('s')
    posts = Post.objects.filter(title__contains=search)

    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        "category_name": "Поиск",
        "posts": posts
    }
    return render(request, 'category/index.html', context)
