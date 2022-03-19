from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from signuser.models import UserProfile
from wepost_main.models import *

def trending_page(request: HttpRequest):
    return render(request, 'base.html')


def explore_page(request: HttpRequest):
    return render(request, 'wepost_main/explore.html')

def load_explore_page_albums(request: HttpRequest):
    posts = Post.objects.select_related('user').all()
    context = {
        'post_list': posts
    }

    return render(request, 'components/album_card_list.html', context)

