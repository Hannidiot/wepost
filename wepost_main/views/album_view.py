from django.http import HttpRequest
from django.shortcuts import render

from wepost_main.models import *

def trending_page(request: HttpRequest):
    return render(request, 'wepost_main/trending.html')


def explore_page(request: HttpRequest):
    return render(request, 'wepost_main/explore.html')

def load_explore_page_albums(request: HttpRequest):
    user = request.user
    if user == "AnonymousUser":
        posts = Like.objects.filter(user_id=user.id).select_related("user", "post").all()
    else:
        posts = Post.objects.select_related('user').all()
    context = {
        'post_list': posts
    }

    return render(request, 'components/album_card_list.html', context)

def load_most_liked_albums(request: HttpRequest):
    user = request.user
    if user == "AnonymousUser":
        posts = Like.objects.filter(user_id=user.id).select_related("user", "post").all()
    else:
        posts = Post.objects.select_related('user').all()
    context = {
        'post_list': posts
    }

    return render(request, 'components/album_card_list.html', context)
