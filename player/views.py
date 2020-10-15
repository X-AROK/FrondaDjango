from django.shortcuts import render


def index(request, post_id):
    ajax_url = f'/api/video/{post_id}'
    context = {
        'post_id': post_id,
        'ajax_url': ajax_url
    }

    return render(request, 'player/index.html', context)
