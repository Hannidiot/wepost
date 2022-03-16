from django.http import HttpRequest
from django.shortcuts import render


def trending_page(request: HttpRequest):
    return render(request, 'base.html')


def explore_page(request: HttpRequest):
    return render(request, 'wepost_main/explore.html')
