from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from signuser.models import *


@login_required
def user_profile(request: HttpRequest, user_id):
    if request.method == "POST":

        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():

            user_form.save()
        else: print(user_form.errors)
    return render(request, "account/author_profile.html")


@login_required
def views_signuser_header_img(request):
    header_img = request.FILES['header_img']
    user_profile = request.user.userprofile
    user_profile.header_img = header_img
    user_profile.save()
    return render(request, "account/author_profile.html")


@login_required
def follow(request: HttpRequest, user_id):
    if request.method == 'POST':
        login_user = request.user
        followed_user = User.objects.get(id=user_id)

        if (login_user.id == followed_user.id): return JsonResponse({"status": "fail", "msg": "you cannot follow yourself"})

        # check if already followed this user
        is_followed = len(UserRelation.objects.filter(follower_id=login_user.id, followed_user_id=followed_user.id)) == 1
        if (is_followed): return JsonResponse({"status": "fail", "msg": "already followed this user"})

        ur = UserRelation(followed_user_id=followed_user.id, follower_id=login_user.id)
        ur.save()

        up = UserProfile.objects.get(user_id=followed_user.id)
        up.followers += 1
        up.save()

        up = UserProfile.objects.get(user_id=login_user.id)
        up.following += 1
        up.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect("index")


@login_required
def unfollow(request: HttpRequest, user_id):
    if request.method == 'POST':
        login_user = request.user
        followed_user = User.objects.get(id=user_id)

        if (login_user.id == followed_user.id): return JsonResponse({"status": "fail", "msg": "you cannot unfollow yourself"})

        # check if already followed this user
        ur = UserRelation.objects.filter(follower_id=login_user.id, followed_user_id=followed_user.id)
        is_followed = len(ur) == 1
        if (not is_followed): return JsonResponse({"status": "fail", "msg": "you have not followed this user"})

        ur.delete()

        up = UserProfile.objects.get(user_id=followed_user.id)
        up.followers -= 1
        up.save()

        up = UserProfile.objects.get(user_id=login_user.id)
        up.following -= 1
        up.save()

        return JsonResponse({"status": "success", "msg": ""})

    return redirect("index")
