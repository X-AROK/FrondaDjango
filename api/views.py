from django.http import HttpResponse
from posts.models import Video
import json


def video(request, post_id):
    videos = Video.objects.filter(post__id=post_id).order_by('season', 'episode')
    result = {}

    for v in videos:
        player = v.player.name
        season = str(v.season)
        episode = str(v.episode)

        if player not in result:
            result[player] = {}
        if season not in result[player]:
            result[player][season] = {}

        if player.lower() == 'kodik':
            result[player][season][episode] = f'{v.url}&hide_selectors=true&only_season=true&only_episode=true'
        else:
            result[player][season][episode] = v.url

    json_obj = json.dumps(result)
    return HttpResponse(json_obj)
