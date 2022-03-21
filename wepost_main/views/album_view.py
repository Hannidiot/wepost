from django.http import HttpRequest
from django.shortcuts import render

from wepost_main.models import *

def trending_page(request: HttpRequest):
    return render(request, 'wepost_main/trending.html')

def explore_page(request: HttpRequest):
    return render(request, 'wepost_main/explore.html')

def load_explore_page_albums(request: HttpRequest):
    user = request.user
    posts = Post.objects.select_related('user', 'user__userprofile').all()
    if user != "AnonymousUser":
        for post in posts:
            likes = post.like_set.filter(user_id=user.id)
            post.is_liked = len(likes) != 0
    context = {
        'post_list': posts
    }

    return render(request, 'components/album_card_list.html', context)

def load_most_liked_albums(request: HttpRequest):
    user = request.user
    posts = Post.objects.select_related('user').order_by('-likes')[:5]
    if user != "AnonymousUser":
        for post in posts:
            likes = post.like_set.filter(user_id=user.id)
            post.is_liked = len(likes) != 0
    context = {
        'post_list': posts
    }

    return render(request, 'components/album_card_list.html', context)
